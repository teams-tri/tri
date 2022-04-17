import time
import numpy as np


class TimerContextManager(object):
    term = 0

    def __init__(self, kind="quicksort"):
        self.kind = kind

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        TimerContextManager.term = time.time() - self.start
        return True

    def run(self, tab):
        np.sort(tab, kind=self.kind)
