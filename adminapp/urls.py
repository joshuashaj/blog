from django.urls import path
from adminapp import views

urlpatterns = [
    path('',views.index),
    path('login',views.login, name='login'),
    path('adminhome',views.adminhome, name='adminhome'),
    path('cus_emp',views.cus_emp, name='cus_emp'),
    path('logout',views.logout, name='logout'),
    path('adminprofile',views.adminprofile, name='adminprofile'),
    path('custable',views.custable, name='custable'),
    path('emptable', views.emptable, name='emptable'),
    path('blog',views.blog,name='blog'),
    path('blogshow',views.blogshow, name='blogshow'),
    path('blogedit/<int:id>',views.blogedit,name='blogedit'),
    path('blogdelete/<int:id>',views.blogdelete,name='blogdelete')
]
