from django.conf.urls import url

from src.api.v1.views.userview import UserView
from src.api.v1.views.tokenview import TokenView


urlpatterns = [
     url(r'^test/user/$', UserView.as_view()),
     url(r'^test/login/$', TokenView.as_view()),
     ]

