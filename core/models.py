from django.db import models
from django.contrib.auth.models import AbstractUser
from event.models import Events


class Profile(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    # budget = models.IntegerField(null=True)

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Comment(models.Model):
    post = models.ForeignKey(Events, on_delete=models.CASCADE)
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return "Comment by {} on {}".format(self.name, self.post)
