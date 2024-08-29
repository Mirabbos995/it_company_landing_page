from django.urls import path, include
from rest_framework import routers

from about.views import *

# router = routers.SimpleRouter()
# router.register(r'crudcompany', CRUDCompany, basename='company')
# router.register(r'crudteammember', CRUDTeamMember, basename='teammember')

urlpatterns = [
    # path('about/', include(router.urls)),

    ### Company
    path('about/post-company', CRUDCompany.as_view({'post': 'create'})),
    path('about/getlist-company', CRUDCompany.as_view({'get': 'list'})),
    path('about/put-company', CRUDCompany.as_view({'put': 'update'})),
    path('about/patch-company', CRUDCompany.as_view({'patch': 'partial_update'})),
    path('about/get-company/<int:pk>', CRUDCompany.as_view({'get': 'retrieve'})),
    path('about/delete-company', CRUDCompany.as_view({'delete': 'destroy'})),

    ###TeamMember
    path('about/post-teammember', CRUDTeamMember.as_view({'post': 'create'})),
    path('about/getlist-teammember', CRUDTeamMember.as_view({'get': 'list'})),
    path('about/put-teammember', CRUDTeamMember.as_view({'put': 'update'})),
    path('about/patch-teammember', CRUDTeamMember.as_view({'patch': 'partial_update'})),
    path('about/get-teammember/<int:pk>', CRUDTeamMember.as_view({'get': 'retrieve'})),
    path('about/delete-teammember', CRUDTeamMember.as_view({'delete': 'destroy'})),
]
