from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detial',kwargs={'pk':self.pk}) 


class Comment(models.Model): 
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
    		return '%s - %s' % (self.post.title, self.author.username)

    def get_absolute_url(self):
        return reverse('post-detial',kwargs={'pk':self.post.pk}) 
