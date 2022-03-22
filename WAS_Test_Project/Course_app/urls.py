from django.contrib import admin
from django.urls import path
from django.urls import include
from Course_app import views

app_name = 'Course_app'

urlpatterns = [

    path('', views.course, name='course'),
    path('course', views.course, name='course'),
    path('admin/', admin.site.urls),

]
