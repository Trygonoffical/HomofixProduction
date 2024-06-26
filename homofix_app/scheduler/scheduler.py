from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore,register_events
from django.core.management import call_command
import contextlib

def db_backup():
    with contextlib.suppress(Exception):
        call_command('dbbackup')


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(),"default")
    scheduler.add_job(db_backup,'interval',weeks=1,jobstore="default",id="weekly_backup",replace_existing=True)
    register_events(scheduler)
    print("testing running")
    scheduler.start()
    # scheduler.add_job(db_backup,'interval',weeks=1)
