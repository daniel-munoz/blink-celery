from celery import Celery

app = Celery('blink_celery', broker='amqp://', backend='amqp://', include=['blink_celery.blink.tasks'])

if __name__ == '__main__':
    app.start()
