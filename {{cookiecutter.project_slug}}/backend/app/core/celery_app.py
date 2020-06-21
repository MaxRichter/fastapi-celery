from celery import Celery

celery_app = Celery(
    "worker",
    broker="amqp://admin:mypass@rabbit:5672",
    backend="redis://redis:6379/0",
)
