from django.urls import path

from patientapp import views

urlpatterns = [
    path('register',views.register_fun,name='register'),
    path('regdata',views.reg_data),

    path('',views.log_fun,name='log'),
    path('logdata',views.log_data),

    path('index',views.index_fun,name='index'),
    path('readdata',views.read_data),

    path('display', views.display_fun, name='display'),
    path('update/<int:x>', views.update_fun, name='update'),
    path('delete/<int:y>', views.delete_fun, name='delete'),

    path('home',views.home_fun,name='home'),

    path('logout',views.logout_fun,name='logout')
]