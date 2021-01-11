from django.views.generic import ListView
from .models import Company
from django.contrib.auth.models import User
from courses.models import Course

class AboutListView(ListView):
    queryset = Company.objects.first()
    template_name = 'about.html'
    context_object_name = 'company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'About'
        context['number_of_teachers'] = len(User.objects.all())
        context['number_of_courses'] = len(Course.objects.all())
        return context