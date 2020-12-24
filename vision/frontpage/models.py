from django.db import models
from django.conf import settings

def user_path(instance, filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(11)]
    pid = ''.join(arr)
    extension = filename.split(".")[-1]
    return '{}.{}'.format(pid, extension)


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to=user_path)
    upload_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class CrawledData(models.Model):
    id = models.CharField(max_length=100, blank=True, primary_key=True)
    shop = models.CharField(max_length=300, blank=True, null=True)
    brand = models.CharField(max_length=300, blank=True, null=True)
    product = models.CharField(max_length=1000, blank=True, null=True)
    url = models.CharField(max_length=2000, blank=True, null=True)
    img = models.CharField(max_length=2000, blank=True, null=True)
    category = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crawled_data'