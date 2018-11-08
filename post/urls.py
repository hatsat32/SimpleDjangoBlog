from django.urls import path
from .views import *

# url lere uygulama ismi üzerinden erişmek için
app_name = "post"

urlpatterns = [
    # statik url ler
    path("index/", post_index, name="index"),
    path("create/", post_create, name="create"),

    # dinamik url ler
    path("<str:slug>/detail/", post_detail, name="detail"),
    path("<str:slug>/delete/", post_delete, name="delete"),
    path("<str:slug>/update/", post_update, name="update"),
]