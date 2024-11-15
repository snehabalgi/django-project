from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib import messages
from .models import Coffee, Cart
from .forms import CoffeeForm

# View for the home page to display all coffee
def home(request):
    coffee = Coffee.objects.all()
    cart_count = Cart.objects.count()  # Get the number of items in the cart
    return render(request, 'home.html', {'coffee': coffee, 'cart_count': cart_count})

# View to add coffee to the database
def add_coffee(request):
    if request.method == 'POST':
        form = CoffeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Coffee added successfully!')
            return redirect('home')
        else:
            messages.error(request, 'There was an error adding the coffee. Please check the form.')
    else:
        form = CoffeeForm()

    return render(request, 'add_coffee.html', {'form': form})

# View to add coffee to the cart
def add_to_cart(request, coffee_id):
    coffee = get_object_or_404(Coffee, id=coffee_id)

    # Check if the coffee is already in the cart
    cart_item, created = Cart.objects.get_or_create(coffee=coffee)
    if not created:
        # If the item is already in the cart, increase the quantity
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

# View to display the cart
def cart(request):
    cart_items = Cart.objects.all()
    total_price = sum(item.coffee.price * item.quantity for item in cart_items)
    cart_count = cart_items.count()
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price, 'cart_count': cart_count})

# View to clear the cart
def clear_cart(request):
    Cart.objects.all().delete()
    messages.success(request, 'Cart cleared successfully!')
    return redirect('cart')

# View to update cart item quantity
def update_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity', 1))
        if new_quantity > 0:
            cart_item.quantity = new_quantity
            cart_item.save()
            messages.success(request, 'Cart updated successfully!')
        else:
            cart_item.delete()
            messages.success(request, 'Item removed from cart!')
    return redirect('cart')

# View to remove a specific item from the cart
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.delete()
    messages.success(request, 'Item removed from cart!')
    return redirect('cart')

def about(request):
    return render(request, 'about.html')

def coffee_detail(request, coffee_id):
    coffee = get_object_or_404(Coffee, id=coffee_id)
    return render(request, 'coffee_detail.html', {'coffee': coffee})