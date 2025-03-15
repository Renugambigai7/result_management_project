from django.urls import path 

from . import views 

urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('bca',views.bca,name='bca'),
    path('bsccs',views.bsccs,name='bsccs'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('result',views.result,name='result'),
    path('score',views.score,name='score'),
    path('admin',views.admin,name='admin'),
    path('register_form_submission',views.register_form_submission,name='register_form_submission'),
    path('login_form_submission',views.login_form_submission,name='login_form_submission'),
   
]

