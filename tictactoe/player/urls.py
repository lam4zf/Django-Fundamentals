from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, new_invitaiton

urlpatterns = [
    url(r'home$', home, name="player_home"),
    url(r'login',
        LoginView.as_view(template_name="player/login_form.html"),
        name="player_login"),
    url(r'logout',
        LogoutView.as_view(),
        name="player_logout"),
    url(r'new_invitation',
        new_invitaiton,
        name="player_new_invitation"),
]