from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import employees

router = DefaultRouter()

# router.register(r'', views.employees, basename='employee')

urlpatterns = [
    # path('', include(router.urls)),
    path('', employees, name='emp'),
]

