from django.views.generic import ListView
from .models import Course

# Create your views here.
class CoursesListView(ListView):
    queryset = Course.objects.order_by('name')
    template_name = 'courses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Courses'
        return context