from django.views.generic import ListView
from django.contrib.auth.models import User

# Create your views here.
class StaffListView(ListView):
    queryset = User.objects.order_by('-last_name')
    template_name = 'staff.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Staff'
        return context