from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField()
    author = models.CharField(max_length=30, default='anonymous')
    email = models.EmailField(blank=True)
    describe = models.TextField()

    def __str__(self):
        return self.name

    
