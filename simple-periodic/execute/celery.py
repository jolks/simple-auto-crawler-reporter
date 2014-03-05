from __future__ import absolute_import

from celery import Celery
from datetime import timedelta

celery = Celery('execute.celery',
                backend='amqp',
                broker='amqp://localhost//',
                include=['execute.tasks'])

# Optional configuration, see the application user guide.
celery.conf.update(
#    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERYBEAT_SCHEDULE = {
    'runs-every-3600-seconds': {
        'task': 'execute.tasks.crawl',
        'schedule': timedelta(seconds=3600),
        #'args': ('/home/ubuntu/mining/estate', 'stproperty')}}
        'args': ('../estate', 'stproperty')}}
)

if __name__ == '__main__':
    celery.start()
