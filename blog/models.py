from django.db import models


# Create your models here.
class Post(models.Model):
    Post_ID = models.PositiveSmallIntegerField(primary_key=True)
    stitle = models.CharField(max_length=100)
    sbody = models.TextField()
    PicImg = models.ImageField('blog_pictures')
    dDate = models.DateTimeField(auto_now_add=True)
    sAuthor = models.CharField(max_length=100)

    def __str__(self):
        return self.stitle
