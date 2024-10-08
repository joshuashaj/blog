from django.db import models

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    image = models.ImageField(upload_to='img/', default='img/default.jpg')  # Set a default image
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Status'


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)  # Set once when the object is created
    updated_at = models.DateTimeField(auto_now=True)      # Updated every time the object is saved

    class Meta:
        db_table = 'blog'
        ordering = ['-updated_at']
