from blog.models import ArticleModel
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class DeletePostView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('signin')
    template_name = 'pages/delete-post.html'
    success_url = reverse_lazy('my-articles')

    def get_queryset(self):
        article = ArticleModel.objects.filter(
            slug=self.kwargs['slug'], author=self.request.user)
        return article
