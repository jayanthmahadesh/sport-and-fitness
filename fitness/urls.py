from django.urls import path
from .views import Login, SignUp, Index,outdoor,Indoor,timing,Success
from .views import timing_all,Success_Custom,Logout
from django.conf.urls.static import static
from django.conf import settings
from fitness import views
urlpatterns = [
    path('', views.Index, name='indexpage'),
    path('login', views.Login, name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('signup', views.SignUp, name='signup'),
    path('outdoor',views.outdoor,name='outdoor'),
    path('Indoor',views.Indoor,name='Indoor'),
    path('timing',views.timing,name='timing'),
    path('timing_all',views.timing_all,name='timing_all'),
    path('success', views.Success, name='success'),
    path('success_custom', views.Success_Custom, name='success'),
    path('register',views.register,name = 'register')
]