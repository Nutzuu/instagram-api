from django.db import models

from insta_clone.users.models import User


class Post(models.Model):
    resource_url = models.CharField(max_length=512)
    # Should have thumbnail here
    description = models.CharField(max_length=512)
    location = models.CharField(max_length=128)

    users_whom_liked = models.ManyToManyField(User, related_name='liked_posts')
    # Comments

    @property
    def likes(self):
        return self.users_whom_liked.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, null=True)
    parent_comment = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True)

    description = models.CharField(max_length=128)
    likes = models.PositiveIntegerField(default=0)
