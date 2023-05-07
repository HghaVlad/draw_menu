from django.contrib import admin, messages
from .models import MenuStep
# Register your models here.


@admin.register(MenuStep)
class MenuAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if change is True:
            if obj == form.cleaned_data['parent']:
                messages.error(request, "Row's parent mustn't be the same as the row")
            elif obj in form.cleaned_data['children']:
                messages.error(request, "Children mustn't consist of the parent row")
            else:
                super().save_model(request, obj, form, change)

