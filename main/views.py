from django.shortcuts import render, redirect
from .models import Blog, BlogImg, BlogVideo, Comment, SocialLinks, User


def blogs(request):
    posts = Blog.objects.all()
    # for post in posts:
    #     post.img = models.BlogImg.objects.filter(blog__id = post.id).last().img
    context = {"posts": posts}
    return render(request, "blogs.html", context)


def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    social_links = SocialLinks.objects.get(user=blog.author)
    # comment_count = models.Comment.objects.filter(blog=blog).count()
    comments = Comment.objects.filter(blog=blog)
    context = {
        "blog": blog,
        "social_links": social_links,
        # 'comment_count':comment_count,
        "comment_count": comments.count(),
        "comments": comments,
    }
    return render(request, "blog-detail.html", context)


def comment_create(request):
    message = request.POST["message"]
    blog_id = request.POST["blog_id"]
    Comment.objects.create(author=request.user, body=message, blog_id=blog_id)
    return redirect("blog_detail", blog_id)


# def social_links(request):
#     user = request.user
#     social_links = SocialLinks.objects.filter(user=user)

#     return redirect("blog_detail", social_links)
