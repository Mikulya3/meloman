from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    title = models.SlugField(max_length=30, primary_key=True, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True,related_name='children')

    def save(self,*args,**kwargs):
        self.title = self.title.lower()
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Film(models.Model):
    GENRE_CHOICES = (
        ('comedy', 'Комедия'),
        ('drama', 'Драма'),
        ('horror', 'Ужасы'),
    )

    title = models.CharField(max_length=50)
    descriptions = models.TextField(null=True, blank=True)
    genre = models.CharField(choices=GENRE_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='films')
    created_at = models.DateField(auto_created=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField(upload_to='image/')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='images')






