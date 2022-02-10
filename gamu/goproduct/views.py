from django.shortcuts import render, get_object_or_404, redirect
import random
from django.contrib import messages

from django.db.models import Q
from .forms import AddToCartForm

from cart.cart import Cart


from .models import Go_category, Go_product


def search(request):
    query = request.GET.get('query', '')
    products = Go_product.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'search.html', {'products': products, 'query': query})


def goproduct(request, category_slug, product_slug):

    cart = Cart(request)

    product = get_object_or_404(
        Go_product, category__slug=category_slug, slug=product_slug)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            cart.add(product_id=product.id,
                     quantity=quantity, update_quantity=False)

            messages.success(request, 'The product was added to the cart')

            return redirect('goproduct', category_slug=category_slug, product_slug=product_slug)

    else:
        form = AddToCartForm()

    similar_products = list(product.category.goproducts.exclude(id=product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)

    return render(request, 'product.html', {'form': form, 'product': product, 'similar_products': similar_products})


def gocategory(request, category_slug):
    category = get_object_or_404(Go_category, slug=category_slug)

    return render(request, 'category.html', {'category': category})
