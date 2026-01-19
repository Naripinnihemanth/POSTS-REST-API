from django.db import models
from django.contrib.auth.models import User

class postModel(models.Model):
    id=models.IntegerField(primary_key=True)
    post_title=models.CharField(max_length=50)
    post_image=models.ImageField(upload_to="posts/")
    createdAt=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="post")

    def __str__(self):
        return self.post_title