from django.contrib import admin
from recipes.models import Category, Recipe

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)#outra forma de colocar no site admin
class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category,CategoryAdmin)
