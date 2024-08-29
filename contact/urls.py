from django.urls import path, include
from rest_framework import routers
from contact.views import *

router = routers.SimpleRouter()
urlpatterns = [
    path('contact/', include(router.urls)),

    path('contact/post-contact', CRUDContact.as_view({'post': 'create'})),
    path('contact/getlist-contact', CRUDContact.as_view({'get': 'list'})),
    path('contact/get-contact/<int:pk>', CRUDContact.as_view({'get': 'retrieve'})),
    path('contact/delete-contact', CRUDContact.as_view({'delete': 'destroy'})),
]