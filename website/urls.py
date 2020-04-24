from django.urls import path
from. import views
urlpatterns = [
    path('', views.home, name="home"),
    path('response.html', views.response, name="response"),
]
