from django.contrib import admin

# Register your models here.
from home.models import Contact, Comment


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'create_at')
    list_filter = ('status', 'create_at')
    readonly_fields = ('name', 'email', 'subject', 'message')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'subject', 'message', 'rating', 'status', 'create_at') #listede görünecek alanlar
    list_filter = ('status', 'create_at')#filtrelenecek alanlar
    readonly_fields = ('product', 'user', 'subject', 'message', 'rating')#değişikli yapılamayacak alanlar
    list_display_links = ('subject', 'product',)#hangi linke tıklansın
    list_editable = ('status',)

admin.site.register(Contact,ContactAdmin)
admin.site.register(Comment,CommentAdmin)
