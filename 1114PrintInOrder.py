"""
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads.
Thread A will call first(), thread B will call second(), and thread C will call third().
Design a mechanism and modify the program to ensure that second() is executed after first(),
and third() is executed after second().
"""

from typing import Callable
from threading import Barrier, Thread, Lock, Semaphore, Event, Condition
class Foo:
    """
    First thread can print before reaching the first barrier.
    Second thread can print before reaching the second barrier.
    Third thread can print after the second barrier.
    """
    def __init__(self):
        self.first_barrier = Barrier(2)
        self.second_barrier = Barrier(2)

    def first(self, printFirst):
        printFirst()
        self.first_barrier.wait()

    def second(self, printSecond):
        self.first_barrier.wait()
        printSecond()
        self.second_barrier.wait()

    def third(self, printThird):
        self.second_barrier.wait()
        printThird()


class Foo2:
    def __init__(self):
        self.second_lock = Lock()
        self.second_lock.acquire()
        self.third_lock = Lock()
        self.third_lock.acquire()

    def first(self, printFirst):
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_lock.release()

    def second(self, printSecond):
        # printSecond() outputs "second". Do not change or remove this line.
        with self.second_lock:
            printSecond()
            self.third_lock.release()

    def third(self, printThird):
        # printThird() outputs "third". Do not change or remove this line.
        with self.third_lock:
            printThird()


class Foo3:
    def __init__(self):
        self.gates = (Semaphore(0), Semaphore(0))

    def first(self, printFirst):
        printFirst()
        self.gates[0].release()

    def second(self, printSecond):
        with self.gates[0]:
            printSecond()
            self.gates[1].release()

    def third(self, printThird):
        with self.gates[1]:
            printThird()


class Foo4:
    def __init__(self):
        self.done = (Event(), Event())

    def first(self, printFirst):
        printFirst()
        self.done[0].set()

    def second(self, printSecond):
        self.done[0].wait()
        printSecond()
        self.done[1].set()

    def third(self, printThird):
        self.done[1].wait()
        printThird()

class Foo5:
    def __init__(self):
        self.exec_condition = Condition()
        self.order = 0
        self.first_finish = lambda: self.order == 1
        self.second_finish = lambda: self.order == 2

    def first(self, printFirst):
        with self.exec_condition:
            printFirst()
            self.order = 1
            self.exec_condition.notify(2)

    def second(self, printSecond):
        with self.exec_condition:
            self.exec_condition.wait_for(self.first_finish)
            printSecond()
            self.order = 2
            self.exec_condition.notify()

    def third(self, printThird):
        with self.exec_condition:
            self.exec_condition.wait_for(self.second_finish)
            printThird()


a = Foo5()
def printFirst():  print("first", end="")
def printSecond(): print("second", end="")
def printThird():  print("third", end="")
t1 = Thread(target=a.first(printFirst))
t2 = Thread(target=a.second(printSecond))
t3 = Thread(target=a.third(printThird))
threads = [t1, t3, t2]
for t in threads:
    t.start()
for t in threads:
    t.join()




