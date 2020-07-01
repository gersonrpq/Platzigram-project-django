"""Post admin clases"""

# Django
from django.contrib import admin

# Models
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin"""

    list_display = ('pk','title','user','photo','created', 'user')
    list_display_links = ('pk','title')

    search_fields = (
        'title',
        'user',
        'pk')

    list_filter = (
        'created',
        'user',
        )

    fieldsets = (
        ('Content',{
            'fields':(
                ('title','photo'),
            )
        }),
        ('Register',{
            'fields':(
                ('user','created'),
                ('profile','modified')
            )
        })
    )

    readonly_fields = ('created','profile','modified','user')
  