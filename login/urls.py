from django.urls import path

from . import views

urlpatterns=[
    path('',views.register,name='register'),
    path('register',views.register,name='register'),
    path('verify',views.register,name='register'),
    path('login',views.login1,name='login'),
    path('home',views.home,name="home"),
    path('importantDocument',views.importantDocument,name="importantDocument"),
    path('addDocument',views.addDocument,name="addDocument"),
]