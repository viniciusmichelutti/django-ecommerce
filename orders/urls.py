from django.conf.urls import url

from orders import views

urlpatterns = [
    url(r'^create/$', views.create_order, name='create_order'),
]