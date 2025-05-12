from celery import Celery

app = Celery('climate_app', include=['app.tasks'])
app.config_from_object('celeryconfig')
