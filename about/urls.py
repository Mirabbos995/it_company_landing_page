from django.urls import path, include
from rest_framework import routers

from about.views import *

router = routers.SimpleRouter()
router.register(r'crudcompany', CRUDCompany, basename='company')
router.register(r'crudteammember', CRUDTeamMember, basename='teammember')

urlpatterns = [
    path('about/', include(router.urls)),
]
