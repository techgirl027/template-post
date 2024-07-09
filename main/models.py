from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def last_img(self):
        return BlogImg.objects.filter(blog__id=self.id).last().img


class BlogImg(models.Model):
    img = models.ImageField(upload_to="blog-img/")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title


class BlogVideo(models.Model):
    video = models.FileField(upload_to="blog-vidos/")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} -> {self.blog.title}"


# class Network_urls(models.Model):

#     telegram = models.URLField()
#     instagram = models.URLField()
#     facebook = models.URLField()
#     linkedin = models.URLField()
#     twitter = models.URLField()
#     youtube = models.URLField()

#     urls = {
#         "telegram": telegram,
#         "instagram": instagram,
#         "facebook": facebook,
#         "linkedin": linkedin,
#         "twitter": twitter,
#         "youtube": youtube,
#     }

# def __str__(self) -> str:
#     return self


class SocialLinks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telegram = models.URLField()
    instagram = models.URLField()
    facebook = models.URLField()
    linkedin = models.URLField()
    twitter = models.URLField()
    youtube = models.URLField()
