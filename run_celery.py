from celery_tasks.tasks.tasks import test, end_task


if __name__ == '__main__':
    print("__name__ == '__main__'")
    test.delay()
    end_task.delay()
