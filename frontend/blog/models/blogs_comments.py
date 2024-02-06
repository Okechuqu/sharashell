from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class BlogComment(models.Model):

    blog = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, blank=True, null=True)
    userEmail = models.EmailField()
    userComment = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_comment_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("BlogComment")
        verbose_name_plural = ("BlogComments")

    def __str__(self):
        return self.blog.title


