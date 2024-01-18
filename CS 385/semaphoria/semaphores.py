# semaphores.py -- an implementation of semaphores using Python
#                  thread library.
# by: Andrew Poock

import _thread

class Semaphore:
    
    def __init__(self, value = 0):
        self.count = value
        self.queue = []
        self.mutex = _thread.allocate_lock()

    def wait(self):
        self.mutex.acquire()
        self.count = self.count - 1
        if self.count < 0:
            wlock = _thread.allocate_lock()
            wlock.acquire()
            self.queue.append(wlock)
            self.mutex.release()
            wlock.acquire()
        else:
            self.mutex.release()

    def post(self):
        self.mutex.acquire()
        self.count = self.count + 1
        if self.count <= 0:
            wlock = self.queue[0]
            del self.queue[0]
            wlock.release()
        self.mutex.release()

    def getStatus(self):
        return self.count
        #print(f"Count: {self.count}, Number Waiting: {len(self.queue)}")
