# from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.generic.list import ListView
from users.models import MyUser

from .forms import ItemForm
from .models import Item


class ItemListView(ListView):
    model = Item
    paginate_by = 20

    def get_queryset(self):
        return Item.objects.filter(state=Item.POSTED).order_by("-pub_date")


def add_item(request):
    if request.user.is_authenticated:
        try:
            seller = MyUser.objects.get(username=request.user.username)
        except MyUser.DoesNotExist:
            messages.success(request, ("Please sign in with another account"))
            return redirect("login_user")
        if request.method == "POST":
            form = ItemForm(request.POST, request.FILES)
            if form.is_valid():
                item = form.save(commit=False)
                item.seller = seller
                item.state = Item.POSTED
                item.pub_date = timezone.now()
                item.save()
                return redirect("item-list")
            else:
                messages.success(request, ("Your item offer could not be posted"))
        else:
            form = ItemForm()
        return render(
            request,
            "homepage/selling_page.html",
            {"form": form, "seller": seller.username},
        )
    else:
        return redirect("login_user")


def buy(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.user.is_authenticated:
        try:
            item.buyer = MyUser.objects.get(username=request.user.username)
        except MyUser.DoesNotExist:
            item.buyer = get_object_or_404(MyUser, username="anonymous-user")
            pass
    else:
        item.buyer = get_object_or_404(MyUser, username="anonymous-user")
    item.state = item.SOLD
    item.save()
    return render(request, "homepage/purchase_success.html", {"item": item})


def user_page(request):
    if request.user.is_authenticated:
        try:
            user = MyUser.objects.get(username=request.user.username)
        except MyUser.DoesNotExist:
            messages.success(request, ("Please sign in with another account"))
            return redirect("login_user")
        return render(
            request,
            "homepage/user_page.html",
            {
                "items": {
                    "Posted": user.solditem.filter(state=Item.POSTED),
                    "Sold": user.solditem.filter(state=Item.SOLD),
                    "Cancelled": user.solditem.filter(state=Item.CANCELLED),
                },
            },
        )
    else:
        messages.success(request, ("Please log in before trying to sell objects."))
    return redirect("login_user")


def cancel(request, item_id):
    if request.user.is_authenticated:
        try:
            user = MyUser.objects.get(username=request.user.username)
        except MyUser.DoesNotExist:
            messages.success(request, ("Please sign in with another account"))
            return redirect("login_user")
        item = get_object_or_404(Item, pk=item_id)
        if user == item.seller:
            item.state = Item.CANCELLED
            item.save()
            return redirect("user_page")
        else:
            messages.success(
                request,
                (
                    "Please log in with the right account before trying to cancel objects."
                ),
            )
    else:
        messages.success(request, ("Please log in before trying to cancel objects."))
    return redirect("login_user")
