from django.contrib import admin
from core.models.rankme import Rankme
from core.models.user import CustomUser
# Register your models here.

admin.site.register(Rankme)
admin.site.register(CustomUser)
