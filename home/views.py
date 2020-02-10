from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from home.models import ContactForm, Contact, CommentForm, Comment
#from order.models import ShopCart
from order.models import ShopCart
from product.models import Category, Product


def index(request):
    category = Category.objects.all()
    products = Product.objects.all()[:4]
    products2 = Product.objects.all()[4:]

    current_user = request.user
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()

    context = { 'page': 'home',
                'category': category,
                'products': products,
                'products2': products2}
    return  render(request, 'index.html', context)

def login_form(request):
    if request.method=="POST":
        next_url = request.POST['next']

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if next_url:
                return redirect(next_url)
            else:
                return redirect('/')
        else:
            context = {'hata': 'Username or password incorrect',
                       }
            return render(request, "login.html",context)
    else:
        return render(request, "login.html")

def login_out(request):
    logout(request)
    return redirect('/')


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contactdata =Contact()
            contactdata.name = form.cleaned_data['name']
            contactdata.email = form.cleaned_data['email']
            contactdata.subject = form.cleaned_data['subject']
            contactdata.message = form.cleaned_data['message']
            contactdata.save()
            
            messages.success(request, "Your message has been sent. Thank you for you interest ")
            return HttpResponseRedirect('/contact')
    else:
        form = ContactForm()

        return render(request, 'contact.html', {'form': form})

@login_required(login_url='/login')
def comment_add(request,proid):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            current_user = request.user
            data = Comment()
            data.product_id = proid
            data.user_id = current_user.id
            data.subject = form.cleaned_data['subject']
            data.rating = form.cleaned_data['rating']
            data.message = form.cleaned_data['message']
            data.save()

            messages.success(request, "Your review has been sent. Thank you for you interest ")
            return HttpResponseRedirect(url)
    else:
        return HttpResponseRedirect(url)

@login_required(login_url='/login')
def comment_list(request):
    current_user = request.user
    comments = Comment.objects.filter(user=current_user.id).order_by('-id')
    context = {'page': 'comments',
               'comments': comments,
            }

    return render(request, "comment_list.html", context)

@login_required(login_url='/login')
def comment_delete(request,id):
    url = request.META.get('HTTP_REFERER')
    Comment.objects.filter(id=id).delete()
    messages.success(request, "Comment successfully deleted ...")
    return HttpResponseRedirect(url)