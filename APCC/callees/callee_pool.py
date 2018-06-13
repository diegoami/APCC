
from .callee import Callee
from threading import Thread, Semaphore
import logging



"""A fixed pool of callees to manage the scenario of a limited number of workers
"""
class CalleePool():


    def __init__(self, job_type, pool_size=10):
        self.__job_type = job_type
        self.__pool_size = pool_size
        self.__callees = [Callee(job_type)] * pool_size
        self.__available_callees = set(range(0,pool_size))

        self.__unavailable_callees = set()
        self.__semaphore = Semaphore(pool_size)

    def exec_job(self, job):
        self.__semaphore.acquire()
        next_available = self.__available_callees.pop()
        logging.debug("Acquired worker {} of job_type {}".format(next_available, self.__job_type))
        self.__unavailable_callees.add(next_available)
        callee = self.__callees[next_available]
        thread = Thread(target=self.exec_callee, args= ((next_available, callee, job)))
        thread.start()
        return thread

    def exec_callee(self, next_available, callee, job):
        callee.process_job(job)
        self.__unavailable_callees.remove(next_available)
        self.__available_callees.add(next_available)
        logging.debug("Releasing worker {} of job_type {}".format(next_available, self.__job_type))
        self.__semaphore.release()


