from django.shortcuts import get_object_or_404
from blog.models import ArticleModel
from django.views.generic import UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('signin')
    template_name = 'pages/update-post.html'
    fields = ('title', 'content', 'articleImage', 'categories')

    def get_object(self):
        article = get_object_or_404(
            ArticleModel,
            slug=self.kwargs.get('slug'),
            author=self.request.user
        )
        return article

    def get_success_url(self):
        return reverse('article-page', kwargs={
            'slug': self.get_object().slug
        })
