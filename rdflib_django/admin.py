"""
Defines admin options for this RDFlib implementation.
"""
from django.contrib import admin
from django.contrib.admin.widgets import AdminTextareaWidget
from . import models, fields, forms, store


class NamedGraphAdmin(admin.ModelAdmin):
    """
    Admin module for named graphs.
    """

    list_display = ('identifier', )
    ordering = ('identifier', )
    search_fields = ('identifier', )


class NamespaceAdmin(admin.ModelAdmin):
    """
    Admin module for managing namespaces.
    """
    list_display = ('store', 'prefix', 'uri')
    ordering = ('-store', 'prefix')
    search_fields = ('prefix', 'uri')
    form = forms.NamespaceForm

    def get_actions(self, request):
        return []

    def has_delete_permission(self, request, obj=None):
        """
        Default namespaces cannot be deleted.
        """
        if obj is not None and obj.identifier == store.DEFAULT_STORE:
            return False

        return super(NamespaceAdmin, self).has_delete_permission(request, obj)


class UriStatementAdmin(admin.ModelAdmin):
    """
    Admin module for URI statements.
    """
    ordering = ('context', 'subject', 'predicate')
    search_fields = ('subject', 'predicate')
    list_per_page = 100


class AdminLiteralInput(AdminTextareaWidget):

    def format_value(self, value):
        """
        Return a value as it should appear when rendered in a template.
        """
        if value is None:
            return None
        return str(value) + "^^" + str(value.language or '') + "^^" + str(value.datatype or '')

class LiteralStatementAdmin(admin.ModelAdmin):
    """
    Admin module for literal statements.
    """
    ordering = ('context', 'subject', 'predicate')
    search_fields = ('subject', 'predicate')
    list_per_page = 100
    formfield_overrides = {
       fields.LiteralField: {'widget': AdminLiteralInput()},
    }


admin.site.register(models.NamedGraph, NamedGraphAdmin)
admin.site.register(models.NamespaceModel, NamespaceAdmin)

admin.site.register(models.URIStatement, UriStatementAdmin)
admin.site.register(models.LiteralStatement, LiteralStatementAdmin)
