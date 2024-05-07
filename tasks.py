from datetime import timedelta
from celery import Celery
from celery.schedules import crontab

"""
0 sunday
1 monday
2 tuesday
3 wednesday
4 thursday
5 friday
6 saturday

configuring the schedule
crontab(minute=0, hour=0, day_of_week=0)
crontab(minute=0, hour=0, day_of_week='sunday')
crontab(minute=0, hour=0, day_of_week='sun')
crontab(minute=0, hour=0, day_of_week=7)
crontab(minute=0, hour=0, day_of_week='*')
crontab(minute=0, hour=0, day_of_week='mon-fri')
crontab(minute=0, hour=0, day_of_week='monday-friday')
crontab(minute=0, hour=0, day_of_week='*/2')
crontab(minute=0, hour=0, day_of_week='monday,wednesday')
crontab(minute=0, hour=0, day_of_week='mon,wed')
crontab(minute=0, hour=0, day_of_week='mon,wed,fri')
crontab(minute=0, hour=0, day_of_week='monday,wednesday,friday')
crontab(minute=0, hour=0, day_of_week='monday,wednesday,friday,sunday')

"""

app = Celery('celery', broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': timedelta(seconds=30),
    },
    'mul-every-30-seconds': {
        'task': 'tasks.mul',
        'schedule': 30.0,
        'args': (4, 4)
    },
    'mul-every-5-seconds': {
        'task': 'tasks.mul',
        'schedule': 5.0,
        'args': (4, 4)
    }
}


@app.task
def add():
    print("30 seconds Task is running")
    print("5 seconds Task is running")


add.apply_async((), countdown=5)


@app.task
def mul(x, y):
    return x * y
