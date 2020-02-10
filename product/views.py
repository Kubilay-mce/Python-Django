from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from home.models import Comment
from product.models import Product, ProductImage


def detail(request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        productimage = ProductImage.objects.filter(product_id=product_id)
        comments = Comment.objects.filter(product=product_id, status=1).order_by('-id')
        #cform = CommentForm()
        context = {'product': product,
                    'productimage': productimage,
                    'comments': comments,
                    #'cform': cform,
        }

        return render(request, 'detail.html', context)