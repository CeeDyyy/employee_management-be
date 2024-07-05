import io
import sys
import requests
from requests.exceptions import Timeout
import datetime
import time
from random import randint
from django.conf import settings
from django.utils.crypto import get_random_string
from base.logging import Logging
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
# Import for this project
from web.models.option import *
from web.models import *
import re

# Utility
def randomInt(min_val,max_val):
    return randint(min_val, max_val)

def randomString(length):
    return get_random_string(length=length, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

def getCurrentDateTime():
    return datetime.datetime.now()

def getMaxMinDateTime(start_date,end_date):
    from_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    from_date = datetime.datetime.combine(from_date, datetime.time.min)
    to_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
    to_date = datetime.datetime.combine(to_date, datetime.time.max)

    return from_date,to_date

def checkOvertime(start,minutes):
    checking_time = datetime.datetime.now() - datetime.timedelta(minutes=minutes)

    return start < checking_time

def changeDateFormat(date_str,date_format):
    dt = datetime.datetime.strptime(date_str, date_format)
    return dt

def resizeImage(image_file,quality):
    image = Image.open(image_file)
    output = io.BytesIO()
    image.save(output, format='JPEG', quality=quality)
    output.seek(0)

    resized_image = InMemoryUploadedFile(output, 'ImageField',
        image_file.name,
        'image/jpeg',
        sys.getsizeof(output), None)
    
    return resized_image

def Validators_URL(url_image):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex,url_image)

def validate_account_format(name):
    regex = re.compile(
        r'^[A-Za-z0-9]*$', re.IGNORECASE)
    return re.match(regex,name)
