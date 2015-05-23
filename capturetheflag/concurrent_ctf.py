from random import randint
from threading import Thread, Lock
import time

lock = Lock()

class Flag():

    def __init__(self):
        self._captured = False
        self._available = False

    @property
    def captured(self):
        return self._captured

    @property
    def available(self):
        return self._available

    def set_captured(self):
        self._captured = True

    def set_available(self):
        self._available = True


class Player(Thread):

    def __init__(self, name, flag):
        self._name = name
        self._flag = flag
        Thread.__init__(self)

    def run(self):
        while not self._flag.available:
            pass
        lock.acquire()
        if not self._flag.captured:
            time.sleep(randint(0,3))
            self._flag.set_captured()
            print ('{0} WIN!'.format(self._name))
        else:
            print ('{0} IS A LOSER!'.format(self._name))
        lock.release()


flag = Flag()

player_1 = Player('A', flag)
player_2 = Player('B', flag)
player_3 = Player('C', flag)

player_1.start()
player_2.start()
player_3.start()

flag.set_available()
