from celery import Celery

celery_app = Celery(
    "worker",
    broker="amqp://{{cookiecutter.rabbitmq_user}}:{{cookiecutter.rabbitmq_password}}@rabbit:{{cookiecutter.rabbitmq_port}}",
    backend="redis://redis:6379/0",
)
