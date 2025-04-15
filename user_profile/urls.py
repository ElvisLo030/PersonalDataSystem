from django.urls import path
from . import views
from . import views_api

app_name = 'user_profile'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/cities/', views.get_cities, name='get_cities'),
    path('api/towns/<str:city_id>/', views.get_towns, name='get_towns'),
    path('api/submit/', views.submit_form, name='submit_form'),
    path('api/external/submit/', views_api.api_submit_form, name='api_external_submit'),
] 