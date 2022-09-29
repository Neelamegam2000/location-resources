"""location1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from resources import views

urlpatterns = [ 
	url(r'^$', views.login1, name='login1'),
    url(r'^editdetails',views.editdetails,name="editdetails"),
    url(r'^home',views.home,name="home"),
	url(r'^user/$',views.user,name='user'),
    url(r'^user/details',views.details,name='details'),
	url(r'^user/direction',views.direction,name='direction'),
    url(r'^user/review',views.review,name="review"),
    url(r'^forgetpass',views.forgetpass,name="forget_pass"),
    url(r'^status',views.resourcestatus,name="status"),
	url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

