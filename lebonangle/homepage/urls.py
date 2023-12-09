from django.urls import path
from homepage.views import ItemListView

from . import views

urlpatterns = [
    path("", ItemListView.as_view(), name="item-list"),
    path("sell", views.add_item, name="add_item"),
    path("buy/<int:item_id>", views.buy, name="buy"),
    path("your_page", views.user_page, name="user_page"),
    path("cancel/<int:item_id>", views.cancel, name="cancel"),
]
