from django.db import models
from ckeditor.fields import RichTextField


class SiteInfo(models.Model):

    name = models.CharField(max_length=200, blank=True, null=True)

    favicon = models.ForeignKey(
        'images.Image', on_delete=models.PROTECT,related_name="Favicon", blank=True, null=True)
    bannerImg = models.ForeignKey(
        'images.Image', on_delete=models.PROTECT,related_name="Header_Image", blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    siteName = models.CharField(max_length=200, blank=True, null=True)
    siteIcon = models.CharField(max_length=200, blank=True, null=True)
    bannerName = models.CharField(max_length=200, blank=True, null=True)
    bannerNote = models.CharField(max_length=300, blank=True, null=True)
    seoKeyword = models.CharField(max_length=200, blank=True, null=True)
    seoDescrition = RichTextField(blank=True, null=True)
    aboutTitle = models.CharField(max_length=200, blank=True, null=True) 
    aboutSubTitle = models.CharField(max_length=200, blank=True, null=True)
    teamTitle = models.CharField(max_length=200, blank=True, null=True)
    teamSubTitle = models.CharField(max_length=200, blank=True, null=True)
    coursesTitle = models.CharField(max_length=200, blank=True, null=True)
    coursesSubTitle = models.CharField(max_length=200, blank=True, null=True)
    categoryTitle = models.CharField(max_length=200, blank=True, null=True)
    categorySubTitle = models.CharField(max_length=200, blank=True, null=True)
    contactTitle = models.CharField(max_length=200, blank=True, null=True)
    contactSubTitle = models.CharField(max_length=200, blank=True, null=True)
    testimonialTitle = models.CharField(max_length=200, blank=True, null=True)
    testimonialSubTitle = models.CharField(max_length=200, blank=True, null=True)
    
    

    def __str__(self):
        return f'Created'
