from django.urls import path
from .views import ContactListView,ContactDetailView

urlpatterns = [
    path('contacts/<int:pk>',ContactDetailView.as_view(),name='contact_detail'),
    path('', ContactListView.as_view(), name='home'),
]