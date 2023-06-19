from django.contrib import admin
# Note below is .models, not models meaning we are using our local models.py
from .models import Episode

# # Register your models here.
@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ("podcast_name", "title", "pub_date")