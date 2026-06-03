from django.urls import path
from .views import (
    ContactListView,
    ContactDetailView,
    ContactCreateView,
    ContactUpdateView,
    ContactDeleteView
                    )

urlpatterns = [
    path('contacts/<int:pk>/delete/',
        ContactDeleteView.as_view(),name='contact_delete'),
    path('contacts/<int:pk>/edit/',
        ContactUpdateView.as_view(),name='contact_edit'),
    path('contacts/new/',ContactCreateView.as_view(),name='contact_new'),
    path('contacts/<int:pk>',ContactDetailView.as_view(),name='contact_detail'),
    path('', ContactListView.as_view(), name='home'),
]