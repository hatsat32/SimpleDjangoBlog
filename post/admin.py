from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    
    # admin panelinde görünecek alanlar.
    list_display = [
        "title",
        "publishing_date",
        "slug",
    ]

    # hangi alanlarda link gösterileceği
    list_display_links = [
        "title", # list_editable la eklenirse kaldırılmalı !!!
        "publishing_date",
    ]

    # aramayı kolaylaştırmak için hangi alanlar için filtreleme ekleneceği
    list_filter = [
        "publishing_date",
    ]

    # hangi alanlarda arama yapılacak
    search_fields = [
        "title",
        "content",
    ]

    # post admin sayfasından hızlıca düzenleme yapmak için
    # bu alandaki öğeler link olarak kullanılamaz
    list_editable = [
        #"title", #eklenirse link olarak kullanılamaz.
    ]

    class Meta: # hangi model olduğunu belirt
        model = Post


#admin paneline eklendi
admin.site.register(Post, PostAdmin)