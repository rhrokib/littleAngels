from django.contrib import admin
from .models import AdoptionPost


def approve(modeladmin, request, queryset):
    queryset.update(approved=True)
    
approve.short_description = "Approve"

def disapprove(modeladmin, request, queryset):
    queryset.update(approved=False)
    
disapprove.short_description = "Disapprove"

class AdoptionApproval(admin.ModelAdmin):
    list_display = ['title', 'approved']
    ordering = ['approved']
    actions = [approve, disapprove]
    
admin.site.register(AdoptionPost, AdoptionApproval)