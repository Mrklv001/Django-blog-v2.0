from django.views.generic import View
from django.shortcuts import render
# from .models import Product
from .models import Post
from django.views.generic import ListView, DetailView


class ProductList(View):

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'base/product_list.html', context)

    def post(self, request, *args, **kwargs):
        pass


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class Product(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        context = {'product': product}
        return render(request, 'base/products_detail.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context
