from celery import Celery

celery_app = Celery(
    "montecarlo_cloud",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/1",
    include=["app.tasks"],
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="America/Sao_Paulo",
    enable_utc=True,
    worker_prefetch_multiplier=1,
    task_track_started=True,
)