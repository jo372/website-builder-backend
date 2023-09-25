import boto3
from enum import StrEnum

def get_s3_buckets():
    return boto3.resource('s3').buckets.all()

class DevelopmentEnvironment(StrEnum):
    DEV = 'development'
    STAGING = 'staging'
    PROD = 'production'