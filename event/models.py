from django.db import models

# from core.models import Comment


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# class Information(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     name_event = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.name_event


class Place(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    event = models.CharField(max_length=50)
    name_place = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)

    def __str__(self):
        return str(self.event)


class Events(models.Model):
    title = models.OneToOneField(Place, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField(null=True)
    value = models.IntegerField()
    age_limit = models.CharField(max_length=5)
    # place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/%Y/%m/%d/")
    # comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
