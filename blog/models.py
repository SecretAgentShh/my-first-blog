from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):   #defines model aka sweetie this our object named Post
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) #fk link to another model
    title = models.CharField(max_length=200)
    text = models.TextField()  #limitless textbox
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title   #return title of post as a string
