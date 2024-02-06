from backend.enquiries.forms import EnquiryForm
from .models import *
from frontend.blog.models import *
from backend.images.models import *
from backend.courses.models import *
from backend.authuser.models import *
from backend.enquiries.models import *


def frontendContextProcessor(request):
    return {
        'form_eq': EnquiryForm,
        'blogs': Blog.objects.all(),
        'staff': Staff.objects.all(),
        'gallery': Image.objects.all(),
        'aboutus': About.objects.all(),
        'courses': Course.objects.all(),
        'students': Student.objects.all(),
        'services': Service.objects.all(),
        'enquiries': Enquiry.objects.all(),
        'site_info': SiteInfo.objects.all(),
        'our_contact': Contact.objects.all(),
        'socials': Social.objects.all().first(),
        'instructors': Instructor.objects.all(),
        'testimonial': Testimonial.objects.all(),
        'blog_comment': BlogComment.objects.all(),
        'fronendStaff': FrontendStaff.objects.all(),
        'site_infos': SiteInfo.objects.all().first(),
        'course_articles': CourseArticle.objects.all(),
        'course_category': CourseCategory.objects.all(),
        'sliders': Slider.objects.all().order_by('index'),
    }
