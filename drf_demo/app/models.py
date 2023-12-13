from django.db import models


# Create your models here.
class Music(models.Model):
    song = models.TextField()
    singer = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"

def fun_raw_sql_query(**kwargs):
    song = kwargs.get('song')
    if song:
        result = Music.objects.raw('SELECT * FROM music WHERE song = %s', [song])
    else:
        result = Music.objects.raw('SELECT * FROM music')
    return result

