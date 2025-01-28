from django.contrib import admin
from django.apps import apps
from .models import *  

# Automatically register all models in the app
app = apps.get_app_config('API')  
for model in app.get_models():
    admin.site.register(model)