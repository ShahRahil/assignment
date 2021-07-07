from django.contrib import admin
from .models import newpost, comment
# Register your models here.
admin.site.register(newpost)
admin.site.register(comment)