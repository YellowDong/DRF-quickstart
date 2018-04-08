from django.db import models

# Create your models here.


class Music(models.Model):
    song = models.CharField(max_length=20)
    singer = models.CharField(max_length=20)
    last_modify_date = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'music'
