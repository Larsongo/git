"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from blog import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/index/',views.index,name='index'),
    url(r'^blog/add1/',views.add1,name='add1'),
    url(r'^blog/add2/(\d+)/(\d+)/$',views.add2,name='add2'),
    url(r'^blog/daily_log/',views.daily_log,name='daily_log'),
    url(r'^blog/Plus/',views.plus,name='plus')
]
