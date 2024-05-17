from django.db import models
from myapp.models import CustomUser

class Blog(models.Model):
    author=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE,related_name='blog_post')
    created_at=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    edited_at=models.DateTimeField(auto_now=True)
    is_deleted=models.BooleanField(default=False)
    desc=models.CharField(max_length=300)

    def __str__(self):
        return self.title
    

    

