from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = "index.html"



class ProductListView(FilterView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 6
    #стандартное имя списка продуктов в шаблоне
    # для ListView - object_list
    filterset_class = ProductFilter

    def get_queryset(self):
        print(self.kwargs) # поле self.kwargs посмтореть что это
        category_slug = self.kwargs.get('slug')
        subcategory_slug = self.kwargs.get('subcategory_slug')
        if subcategory_slug:
            products = Product.objects.filter(is_active=True, subcategory__slug=subcategory_slug)
        elif category_slug:
            products = Product.objects.filter(is_active=True, category__slug=category_slug)
        else:
            products = Product.objects.filter(is_active=True)
        return products