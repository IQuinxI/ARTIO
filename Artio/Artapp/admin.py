from django.contrib import admin
from .models import Comment, Profile, Poste
# Register your models here.

admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Poste)
