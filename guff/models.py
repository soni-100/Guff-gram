from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    photo= models.ImageField(upload_to='post/')
    caption = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering= ['-created_at']
        
        def _str_(self):
            return self.user.username

# Create your models here.
