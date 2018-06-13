from .callee import Callee
from threading import Thread, Semaphore, Condition
import logging
from collections import defaultdict

"""A pool of workers, uniformly preassigned to job_types, which can change assignment in case some job_types are overloaded
"""

class VariablePool():

    def __init__(self, job_types, pool_size):
        self.__job_types = job_types
        self.__pool_size = pool_size
        self.__callee_pool = []
        self.__pool_distribution = defaultdict(int)
        self.__callees = {}
        self.__available_callees = {}
        self.__unavailable_callees = {}
        self.__semaphores = {}
        self.__conditions = {}

        for job_type in self.__job_types:
            self.__pool_distribution[job_type] = pool_size
            self.__available_callees[job_type] = set( range(job_type*pool_size , job_type*pool_size +pool_size))
            logging.debug("Adding callees to job_type {} : {}".format(job_type, self.__available_callees[job_type]))
            self.__callees[job_type] = { callee_id : Callee(job_type) for callee_id in self.__available_callees[job_type]}
            self.__unavailable_callees[job_type] = set()
            self.__semaphores[job_type] = Semaphore(pool_size)
            self.__conditions[job_type] = Condition()

    def get_first_free(self):
        free_pool = sorted([(job_type, len(available)) for job_type, available in self.__available_callees.items() if len(available) > self.__pool_size / 2],
                           reverse=True, key=lambda x: x[1])
        if (len(free_pool) > 0):
            return free_pool[0]
        else:
            return None, None

    def exec_job(self, job, job_type):
        self.__semaphores[job_type].acquire()
        next_available = self.__available_callees[job_type].pop()
        logging.debug("Acquired worker {} of job_type {} : available {}".format(next_available, job_type,  len(self.__available_callees[job_type])))
        self.__unavailable_callees[job_type].add(next_available)
        callee = self.__callees[job_type][next_available]
        thread = Thread(target=self.exec_callee, args=((job_type, next_available, callee, job)))
        thread.start()
        return thread

    def exec_callee(self, job_type, next_available, callee, job):
        callee.process_job(job)
        self.__unavailable_callees[job_type].remove(next_available)
        self.__available_callees[job_type].add(next_available)
        logging.debug("Releasing worker {} of job_type {} : available {}".format(next_available, job_type, len(self.__available_callees[job_type])))

        if (len(self.__available_callees[job_type])) <= 1:
            logging.info("job_type {} has few available".format(job_type))
            first_free, how_many = self.get_first_free()
            if (first_free and first_free != job_type):
                logging.warning("Switching worker  from job_type {} to job_type {}".format( first_free, job_type))
                free_available = self.__available_callees[first_free].pop()
                self.__semaphores[first_free].acquire()
                logging.warning("Now job_type {} has {}".format(first_free, self.__available_callees[first_free]))

                self.__available_callees[job_type].add(free_available)
                self.__callees[job_type][free_available] = self.__callees[first_free][free_available ]
                self.__callees[first_free][free_available] = None
                self.__callees[job_type][free_available].switch_job_type(job_type)
                self.__semaphores[job_type].release()

        self.__semaphores[job_type].release()
