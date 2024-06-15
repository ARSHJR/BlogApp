from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField() #Makes use of the rich text editor
    date = models.DateField(auto_now_add=True) #Auto sets the date to current date
    author = models.ForeignKey(User, on_delete=models.CASCADE) #If we delete the user, all the relationships to these are also deleted
    featured = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='likes', blank=True) #Blank=True makes it so that this field isn't required