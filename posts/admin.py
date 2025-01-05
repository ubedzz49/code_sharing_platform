from django.contrib import admin
from .models import Post,Soln
# Register your models here.

admin.site.register(Post)
admin.site.register(Soln)
from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'timestamp')  # Customize fields displayed in the admin list view
    search_fields = ('user__username', 'content')   # Allow searching by username or message content
    list_filter = ('timestamp',)                    # Add filtering options by timestamp
