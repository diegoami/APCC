from .callee import Callee
from threading import Thread, Semaphore, Condition
import logging
from collections import defaultdict

class LRUPool():


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
            self.__callees[job_type] = [Callee(job_type)] * pool_size
            self.__callee_pool.extend(self.__callees[job_type])
            self.__pool_distribution[job_type] = pool_size
            self.__available_callees[job_type] = set(range(0, pool_size))
            self.__unavailable_callees[job_type] = set()
            self.__semaphores[job_type] = Semaphore(pool_size)
            self.__conditions[job_type] = Condition(pool_size)

    def exec_job(self, job, job_type):
        self.__semaphores[job_type].acquire()
        next_available = self.__available_callees[job_type].pop()
        logging.debug("Acquired worker {} of job_type {} on condition {}".format(next_available, job_type,  self.__semaphores[job_type]))
        self.__unavailable_callees[job_type].add(next_available)
        callee = self.__callees[job_type][next_available]
        thread = Thread(target=self.exec_callee, args=((job_type, next_available, callee, job)))
        thread.start()
        return thread

    def exec_callee(self, job_type, next_available, callee, job):
        callee.process_job(job)
        self.__unavailable_callees[job_type].remove(next_available)
        self.__available_callees[job_type].add(next_available)
        logging.debug("Releasing worker {} of job_type {} on condition {}".format(next_available, job_type, self.__semaphores[job_type]))
        self.__semaphores[job_type].release()


