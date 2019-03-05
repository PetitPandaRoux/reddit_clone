from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/', views.sign_up, name='signup'),
    url(r'^login/', views.show_login, name='login'),
    url(r'^logout/', views.show_logout, name='logout'),
]
