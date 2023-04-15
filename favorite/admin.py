from django.contrib import admin

from favorite.models import Favorite, Comment, Like, Rating

admin.site.register(Favorite)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Rating)
