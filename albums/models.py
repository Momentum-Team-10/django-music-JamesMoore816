from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, blank=True, null=True)
    # artist = models.ForeignKey(
    #     'Album', on_delete=models.CASCADE, default=None,)
    year_published = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name