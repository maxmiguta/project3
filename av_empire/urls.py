"""
av_empire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from home import views
from accounts import views as accounts_views
from products import views as products_views
from cart.views import view_cart, add_to_cart, adjust_cart
from checkout.views import checkout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.get_index, name='index'),
    url(r'^about/$', views.get_about),
    url(r'^products/categories/$', products_views.products),
    url(r'^products/audio/$', products_views.audio),
    url(r'^products/control/$', products_views.control),
    url(r'^products/interactive/$', products_views.interactive),
    url(r'^products/visual/$', products_views.visual),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^contact/$', views.get_contact),
    url(r'^cart/$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
    url(r'^checkout/$', checkout, name='checkout'),
]
