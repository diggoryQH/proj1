from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from httpcore import request
from books.models import Book
from .models import Cart, CartItem


@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # LẤY HOẶC TẠO CART CHO USER
    cart, created = Cart.objects.get_or_create(user=request.user)

    # LẤY HOẶC TẠO CART ITEM
    item, created = CartItem.objects.get_or_create(
        cart=cart,
        book=book
    )

    if not created:
        item.quantity += 1
    item.save()

    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    return render(request, 'cart_detail.html', {
    'cart': cart,
    'items': items
})

