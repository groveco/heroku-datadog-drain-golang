import os
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=5)
def timed_job():
os.system('heroku logs -n 1500 --app vast-cove-11097  >> heroku-dd.txt')


sched.start()
