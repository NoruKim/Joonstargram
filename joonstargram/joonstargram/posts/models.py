from django.db import models
from joonstargram.users.models import User

# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Post(TimeStampedModel):
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name="post_author"
    )
    image = models.ImageField(blank=False)
    caption = models.TextField(blank=True)
    image_likes = models.ManyToManyField(
        User, blank=True,
        related_name="post_image_likes"
        )

    def __str__(self):
        return f"{self.author}: {self.caption}"

class Comment(TimeStampedModel):
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name="comment_author"
    )
    posts = models.ForeignKey(
        Post,
        null=True,
        on_delete=models.CASCADE,
        related_name="comment_post"
    )
    content = models.TextField(blank=True)

    def __str__(self):
        return f"{self.author}: {self.content}"
