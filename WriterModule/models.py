from django.db import models

# Create your models here.
class MainTextBody(models.Model) :
    body_text = models.TextField()
    last_update_date = models.DateTimeField('last update')
    author = models.CharField(max_length=512)