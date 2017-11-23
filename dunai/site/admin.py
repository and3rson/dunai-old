from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from .models import Feature


class FeatureAdmin(OrderedModelAdmin):
    list_display = ('__str__', 'move_up_down_links')


admin.site.register(Feature, FeatureAdmin)

