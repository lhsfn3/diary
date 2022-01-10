from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    contexts = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.title

