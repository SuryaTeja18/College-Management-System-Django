"""classproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls import include, url  # For django versions before 2.0
from django.urls import include, path  # For django versions from 2.0 and up
from onlineApp.views import *


urlpatterns =[
    path('admin/',admin.site.urls),
    #path('hello/', include('onlineApp.urls')),
    # path('onlineapp/get_my_college/',get_my_college),
    # path('onlineapp/get_all_colleges/',get_all_colleges),
    # path('sampletemplate/',get_sample_template),
    # path('onlineapp/college_student_info/:id',get_college_student_info)
    path('',include('onlineApp.urls')),
    #path('^api/',include('onlineApp.rest_urls'))
]

# urlpatterns = [
#     path('admin/',admin.site.urls),
#     path('hello/',hello),
#     path('helloHtml/',renderHelloHtml),
#     path('onlineapp/get_my_college',get_my_college)
# ]

if(settings.DEBUG):
    import debug_toolbar
   #
    urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns