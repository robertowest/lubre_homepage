from django.contrib.auth.views import (LoginView, LogoutView, 
                                       PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
                                       PasswordChangeView, PasswordChangeDoneView)
from django.urls import include, path

from . import views

# accounts/ login/ [name='login']
# accounts/ logout/ [name='logout']
# accounts/ password_change/ [name='password_change']
# accounts/ password_change/done/ [name='password_change_done']
# accounts/ password_reset/ [name='password_reset']
# accounts/ password_reset/done/ [name='password_reset_done']
# accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/ reset/done/ [name='password_reset_complete']

urlpatterns = [
     path('', views.LoginRedirect, name='redirect'),

     path('login/', views.login_view, name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),

     # path('redirect/', views.LoginRedirect, name='redirect'),
     path('signup/', views.signup, name='signup'),
     path('profile/', views.profile, name='profile'),

     path('password/reset/', 
          PasswordResetView.as_view(template_name='accounts/password_reset.html'), 
          name='password_reset'),
     path('password/reset/done/', 
          PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),
          name='password_reset_done'),

     path('password/change/<uidb64>/<token>/', 
          PasswordChangeView.as_view(template_name='accounts/password_change.html'),
          name='password_change'),
     path('password/change/done/', 
          PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
          name='password_change_done'),

     # esta estrada es para las redes sociales
     path('oauth/', include('social_django.urls', namespace='social')),
]
