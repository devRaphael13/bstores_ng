from django.contrib import admin
from . import models as m

admin.site.register(m.Product)
admin.site.register(m.Category)