# C:\Users\Gourav Rajput\CropCareConnect\cropcare_project\__init__.py

# This will make sure the Celery app is always imported when Django starts
from .celery import app as celery_app

__all__ = ('celery_app',)
