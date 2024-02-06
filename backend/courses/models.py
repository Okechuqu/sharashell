from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Course(models.Model):
    courseTitle = models.CharField(
        max_length=100, blank=True, null=True)
    numStudents = models.IntegerField(blank=True, null=True)
    durationHours = models.FloatField(blank=True, null=True)
    courseShortDescription = RichTextField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    courseImage = models.ForeignKey(
        'images.Image', related_name='course_image', on_delete=models.PROTECT, blank=True, null=True)

    instructorName = models.ForeignKey(
        'page.Instructor',  on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.courseTitle


class CourseArticle(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    article = RichTextField()
    banner = models.ForeignKey(
        'images.Image', on_delete=models.PROTECT, blank=True, null=True)
    youtubeVideoLink = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = ("Course Article")
        verbose_name_plural = ("Course Article")

    def __str__(self):
        return self.course.courseTitle


class CourseCategory(models.Model):
    img = models.ForeignKey('images.Image', on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.title


