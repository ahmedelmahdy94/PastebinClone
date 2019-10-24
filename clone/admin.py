from django.contrib import admin
from .models import Posts


# Register your models here.
admin.site.register(Posts)



# class PostAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         if not change:
#             obj.created_by = request.user
#         obj.save()
# admin.site.register(Posts, PostAdmin);
