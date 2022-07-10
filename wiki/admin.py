from django.contrib import admin

from wiki.models import WikiBase, WikiContent, WikiFolder

# Register your models here.
admin.site.register(WikiFolder)
admin.site.register(WikiBase)
admin.site.register(WikiContent)