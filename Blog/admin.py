from django.contrib import admin
from Blog.models import Categoria, Post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')    # con esta instrucción de solo lectura hago que los campos created y updated se reflejen en el panel de administración

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)