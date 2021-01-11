from django.shortcuts import render
from django.contrib.auth.models import User
from reviews.models import Review
from courses.models import Course
from about.models import Company


def index(request):

    context = {
        'page_title': 'Home',
        'reviews': Review.objects.all()[:4],
        'teachers': User.objects.all()[:4],
        'courses': Course.objects.all()[:4],
        'company': Company.objects.first(),
        'number_of_teachers': len(User.objects.all()),
        'number_of_courses': len(Course.objects.all())
    }

    return render(request, 'index.html', context=context)