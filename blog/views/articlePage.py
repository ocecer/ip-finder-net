from django.shortcuts import get_object_or_404, redirect, render
from blog.models import ArticleModel
from blog.forms import CommentCreateModelForm
from django.views import View
import logging


logger = logging.getLogger('post_read')


class ArticleView(View):
    http_method_names = ['get', 'post']
    createCommentForm = CommentCreateModelForm

    def get(self, request, slug):
        article = get_object_or_404(ArticleModel, slug=slug)

        if request.user.is_authenticated:
            logger.info('post read:' + request.user.username)

        comments = article.comments.all()

        return render(request, 'pages/post.html', context={
            'article': article,
            'comments': comments,
            'createCommentForm': self.createCommentForm()
        })

    def post(self, request, slug):
        article = get_object_or_404(ArticleModel, slug=slug)
        createCommentForm = CommentCreateModelForm(data=request.POST)

        if createCommentForm.is_valid():
            comment = createCommentForm.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()

        return redirect('article-page', slug=slug)

# from django.shortcuts import get_object_or_404, render
# from blog.models import ArticleModel
# from blog.forms import CommentCreateModelForm


# def articlePage(request, slug):
#     article = get_object_or_404(ArticleModel, slug=slug)
#     comments = article.comments.all()

#     if request.method == 'POST':
#         createCommentForm = CommentCreateModelForm(data=request.POST)
#         if createCommentForm.is_valid():
#             comment = createCommentForm.save(commit=False)
#             comment.author = request.user
#             comment.article = article
#             comment.save()

#     createCommentForm = CommentCreateModelForm()

#     return render(request, 'pages/article-page.html', context={
#         'article': article,
#         'comments': comments,
#         'createCommentForm': createCommentForm
#     })
