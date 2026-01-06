from django.urls import path

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signupuser, name='signup'),
    path('login/', views.Loginuser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),

]
