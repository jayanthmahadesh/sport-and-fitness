from django.contrib import admin

from fitness.models import custom_user
from fitness.models import indoor_activities
admin.site.register(custom_user)
admin.site.register(indoor_activities)
# Register your models here.

