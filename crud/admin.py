from django.contrib import admin
from .models import user
# Register your models here.


@admin.register(user)
class AuthorAdmin(admin.ModelAdmin):
    list_display=['id','name','email','password'] 