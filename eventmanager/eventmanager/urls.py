"""eventmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from .router import router
import meetings 
#from rest_framework_jwt.views import obtain_jwt_token
from django.views.static import serve
from django.conf import settings
from accounts_register.views import UserViewSetPaid



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('meetings/', include('meetings.urls')),
    #path('paid_user/',UserViewSetPaid.as_view()),
    #path('login/',obtain_jwt_token),
    path('chat/', include('chat.api.urls', namespace='chat')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
    #path('paid_user/',UserViewSetPaid.as_view())

]
