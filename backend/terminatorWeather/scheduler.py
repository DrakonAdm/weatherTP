from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, DjangoMemoryJobStore
import sys

# This is the function you want to schedule - add as many as you want and then register them in the start() function
# below
from .scripts import *


def activate_scripts():
    check_and_move_forecast()
    updateForecastToday()
    # createMonth()
    updateForecastThirtySecondDay()
    update_Abnormal()
    print("Good activate228")


def start():
    job_defaults = {
        'coalesce': False,
        'max_instances': 1
    }
    scheduler = BackgroundScheduler(job_defaults=job_defaults)
    # scheduler.add_jobstore(DjangoMemoryJobStore(), "default")
    # run this job every 24 hours
    scheduler.add_job(activate_scripts, 'interval', hours=24, name='refreshWeather', jobstore='default')
    # next_run_time=datetime.now()
    register_events(scheduler)
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)
