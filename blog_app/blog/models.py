from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField()
    author = models.ForeignKey('auth.user', on_delete= models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title 