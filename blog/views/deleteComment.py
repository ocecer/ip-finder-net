from django.contrib.auth.decorators import login_required
from blog.models import CommentModel
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


@login_required(login_url='/')
def deleteComment(request, id):
    comment = get_object_or_404(CommentModel, id=id)
    if comment.author == request.user or comment.article.author == request.user:
        comment.delete()
        messages.success(request, "Comment deleted successfully.")
        return redirect('article-page', slug=comment.article.slug)
    return redirect('home')
