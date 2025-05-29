from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name



class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    serving = models.IntegerField()
    serving_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)#campo de true e false
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null= True, blank=True, default=None) #para caso a categoria seja deletada ela seja nula nessa tabela.
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None) 

    def __str__(self):
        return self.title
