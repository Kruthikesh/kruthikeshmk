from django.conf.urls import url
from . import views


app_name='basic_app'


urlpatterns = [url('register',views.register,name='register')]
