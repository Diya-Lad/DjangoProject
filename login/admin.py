from django.contrib import admin
from login.models import login
from login.models import importantDocuments

# Register your models here.
admin.site.register(login)
admin.site.register(importantDocuments)