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

    def __str__(self):
        return self.name