from django.contrib import admin

from wiki.models import WikiBase, WikiContent

# Register your models here.
admin.site.register(WikiBase)
admin.site.register(WikiContent)