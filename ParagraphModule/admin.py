from django.contrib import admin

from .models import Character, Paragraph, ParagraphLinks

# Register your models here.
admin.site.register(Paragraph)
admin.site.register(ParagraphLinks)
admin.site.register(Character)