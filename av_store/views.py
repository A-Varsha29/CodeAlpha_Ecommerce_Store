from django.shortcuts import render, get_object_or_404, redirect
from av_store.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    products = Product.objects.all()
    return render(request, 'av_store/home.html',{'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'av_store/product_detail.html', {'product': product})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, 'av_store/register.html', {'form': form})
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    # Convert ID to string because session JSON keys must be strings
    pid_str = str(product_id)

    if pid_str in cart:
        cart[pid_str] += 1
    else:
        cart[pid_str] = 1

    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=int(product_id))
        subtotal = product.price * quantity
        total_price += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'av_store/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })
            