from django.contrib import admin
from .models import Post

# Register your models here.
#takes model we defined for blog post and registers for admin interface
#so it shows up on admin section of website
#this is a pre-existing module!
admin.site.register(Post)
