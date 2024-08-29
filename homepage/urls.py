from django.urls import path, include
from rest_framework import routers

from homepage.views import CRUDService, CRUDIdeas, CRUDProcessStep

url_patterns = [
    # path('service/', include(router.urls)),

    ### Service
    path('service/post-service', CRUDService.as_view({'post': 'create'})),
    path('service/getlist-service', CRUDService.as_view({'get': 'list'})),
    path('service/put-service', CRUDService.as_view({'put': 'update'})),
    path('service/patch-service', CRUDService.as_view({'patch': 'partial_update'})),
    path('service/get-service/<int:pk>', CRUDService.as_view({'get': 'retrieve'})),
    path('service/delete-service', CRUDService.as_view({'delete': 'destroy'})),

    ### Ideas
    path('service/post-ideas', CRUDIdeas.as_view({'post': 'create'})),
    path('service/getlist-ideas', CRUDIdeas.as_view({'get': 'list'})),
    path('service/put-ideas', CRUDIdeas.as_view({'put': 'update'})),
    path('service/patch-ideas', CRUDIdeas.as_view({'patch': 'partial_update'})),
    path('service/get-ideas/<int:pk>', CRUDIdeas.as_view({'get': 'retrieve'})),
    path('service/delete-ideas', CRUDIdeas.as_view({'delete': 'destroy'})),

    ### ProcessStep
    path('service/post-processstep', CRUDProcessStep.as_view({'post': 'create'})),
    path('service/getlist-processstep', CRUDProcessStep.as_view({'get': 'list'})),
    path('service/put-processstep', CRUDProcessStep.as_view({'put': 'update'})),
    path('service/patch-processstep', CRUDProcessStep.as_view({'patch': 'partial_update'})),
    path('service/get-processstep/<int:pk>', CRUDProcessStep.as_view({'get': 'retrieve'})),
    path('service/delete-processstep', CRUDProcessStep.as_view({'delete': 'destroy'})),
]


