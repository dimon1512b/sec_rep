import time
from celery import Celery

import async_test

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1

# broker_url = 'redis://{}:{}/{}'.format(REDIS_HOST, REDIS_PORT, REDIS_DB)

app = Celery()

# app.conf.broker_url = broker_url


@app.task
def test():
    print('GO!!!')
    time.sleep(5)
    async_test.run_as_imported()
    time.sleep(5)
    print('END!!!')


@app.task
def end_task():
    print('GO END TASK')
    time.sleep(1)
    print('MAKING SOMETHING FOR THE END OF ALL TASKS')
    time.sleep(1)
    print('END END TASK')


'''
I don't know why this not working...
'''
