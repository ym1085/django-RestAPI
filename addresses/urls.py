from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('addresses/', views.address_list),
    path('addresses/<int:pk>', views.address),
    path('login/', views.login),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]