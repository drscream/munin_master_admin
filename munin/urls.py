from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='munin/main.html'), name='main'),
    path('groups/', GroupList.as_view(), name='group_list'),
    path('groups/add', GroupCreate.as_view(), name='group_create'),
    path('groups/<int:pk>/delete', GroupDelete.as_view(), name='group_delete'),
    path('hosts/', HostList.as_view(), name='host_list'),
    path('hosts/add', HostCreate.as_view(), name='host_create'),
    path('hosts/<int:pk>/delete', HostDelete.as_view(), name='host_delete'),
]
