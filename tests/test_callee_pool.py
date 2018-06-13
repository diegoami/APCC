import unittest
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)




from callees.callee_pool import CalleePool

class CallePoolTest(unittest.TestCase):

    def test_pool(self):
        callee_pool = CalleePool(job_type=1, pool_size=5)
        all_threads = []
        for i in range(0,20):
            logging.info("Starting executing job {}".format(i))
            all_threads.append(callee_pool.exec_job(i))
            logging.info("Queued job {}".format(i))

        for thread in all_threads:
            thread.join()