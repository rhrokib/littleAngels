from django.contrib import admin
from .models import Vet


def approve(modeladmin, request, queryset):
    queryset.update(approved=True)


approve.short_description = "Approve"


def disapprove(modeladmin, request, queryset):
    queryset.update(approved=False)


disapprove.short_description = "Disapprove"


class VetApproval(admin.ModelAdmin):
    list_display = ['vet_name', 'approved']
    ordering = ['approved']
    actions = [approve, disapprove]


admin.site.register(Vet, VetApproval)
