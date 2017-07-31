from django.conf.urls import url

from staff import views

urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^home/$', views.HomeView.as_view(), name='home'),
    url(r'^edit/$', views.EditView.as_view(), name='edit'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]
