from django.urls import path, include
# from rest_framework import routers

from project.views import *

urlpatterns = [
    # path('project/', include(router.urls)),
    ### Project
    path('project/getlist-project', RLProject.as_view({'get': 'list'})),
    path('project/get-project/<int:pk>', RLProject.as_view({'get': 'retrieve'})),

    ### Project Details
    path('project/post-projectdetails', CRUDProjectDetails.as_view({'post': 'create'})),
    path('project/getlist-projectdetails', CRUDProjectDetails.as_view({'get': 'list'})),
    path('project/put-projectdetails', CRUDProjectDetails.as_view({'put': 'update'})),
    path('project/patch-projectdetails', CRUDProjectDetails.as_view({'patch': 'partial_update'})),
    path('project/get-projectdetails/<int:pk>', CRUDProjectDetails.as_view({'get': 'retrieve'})),
    path('project/delete-project-details', CRUDProjectDetails.as_view({'delete': 'destroy'})),

    ### Project Showcase
    path('project/getlist-project', RLProjectShowcase.as_view({'get': 'list'})),
    path('project/get-project/<int:pk>', RLProjectShowcase.as_view({'get': 'retrieve'})),

    ### Category
    path('project/post-category', CRUDCategory.as_view({'post': 'create'})),
    path('project/getlist-category', CRUDCategory.as_view({'get': 'list'})),
    path('project/put-category', CRUDCategory.as_view({'put': 'update'})),
    path('project/patch-category', CRUDCategory.as_view({'patch': 'partial_update'})),
    path('project/get-category/<int:pk>', CRUDCategory.as_view({'get': 'retrieve'})),
    path('project/delete-category', CRUDCategory.as_view({'delete': 'destroy'})),
]
