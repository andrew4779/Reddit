from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, 
    on_delete=models.CASCADE,)    # To refer to models defined in another application we can use Foreign Key
    votes_total = models.IntegerField(default=0)
    