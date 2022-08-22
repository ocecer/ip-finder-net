from msilib.schema import ListView
from django.shortcuts import get_object_or_404
from blog.models import CatagoryModel
from django.views.generic import ListView


class CategoryListView(ListView):
    template_name = 'pages/category.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        category = get_object_or_404(
            CatagoryModel, slug=self.kwargs['categorySlug'])
        return category.article.all().order_by('-id')
