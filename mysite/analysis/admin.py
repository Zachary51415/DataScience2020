from django.contrib import admin

# Register your models here.
from .models import User,Question,Result,Upload

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Result)
admin.site.register(Upload)