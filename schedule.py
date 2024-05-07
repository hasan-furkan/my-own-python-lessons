import sched
import time
s = sched.scheduler(time.time, time.sleep)


def print_time(a='default'):
    print("From print_time", time.time(), a)


def print_some_times():
    s.enter(10, 1, print_time, argument=('10 seconds 1 priority',))
    s.enter(15, 1, print_time, kwargs={'a': '15 seconds 1 priority'})
    s.enter(15, 2, print_time, argument=('15 seconds 2 priority',))
    s.enter(20, 5, print_time, argument=("20 seconds 5 priority",))
    s.enter(20, 8, print_time, argument=("20 seconds 8 priority",))
    s.enter(20, 10, print_time, argument=("20 seconds 10 priority",))
    s.run()


print_some_times()
