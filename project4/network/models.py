from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_author")
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)
    likes = models.ManyToManyField("User", related_name="liked_posts", blank=True)
    
    def __str__(self):
        return f"{self.user} posted: {self.content}, on {self.timestamp.strftime('%b %d %Y, %I:%M %p')}"
    
class Follow(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_following")
    userF = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_followed")
    
    def __str__(self):
        return f"{self.user} followed: {self.userF}"

class Like(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_that_likes")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="Post_liked")
    
    def __str__(self):
        return f"{self.user} liked: {self.post}"