from django.conf import settings
from storages.backends.s3boto3 import S3BOto3Storage

class StaticStorage(S3Boto3Storage):
    location = setings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = setings.MEDIAFILES_LOCATION