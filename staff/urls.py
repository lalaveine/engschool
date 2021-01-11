from django.urls import path
from .views import StaffListView

urlpatterns = [
    path('', StaffListView.as_view()),
]
