from threading import Thread, Condition
import time
import random

condition = Condition()
queue = []

class DishDryer(Thread):

    def __init__(self, name, washer):
        self._name = name
        self._washer = washer
        Thread.__init__(self)

    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print (
                    "{0} says: Nothing to dry, I'm waiting".format(self._name)
                )
                if not self._washer.ended:
                    condition.wait()
                if self._washer.ended:
                    condition.release()
                    print "{0} says: Bye!".format(self._name)
                    break
                print (
                    "{0} says: Looks like there's something to dry!".format(self._name)
                )
            if queue:
                num = queue.pop(0)
                print ("{0} says: {1} dryed!".format(self._name, num))
            condition.release()
            time.sleep(random.random())


class DishWasher(Thread):

    def __init__(self, name):
        self._name = name
        self._ended = False
        Thread.__init__(self)

    def run(self):
        nums = range(5)
        global queue
        for i in range(10):
            condition.acquire()
            num = random.choice(nums)
            queue.append(num)
            print ("{0} says: Washed {1}".format(self._name, num))
            condition.notifyAll()
            condition.release()
            time.sleep(random.random())
        condition.acquire()
        self._ended = True
        condition.notifyAll()
        condition.release()

    @property
    def ended(self):
        return self._ended


emanuela = DishWasher('Emanuela')
andrea = DishDryer('Andrea', emanuela)
ambra = DishDryer('Ambra', emanuela)

emanuela.start()
andrea.start()
ambra.start()
