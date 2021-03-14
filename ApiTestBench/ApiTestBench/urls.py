"""ApiTestBench URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from MyApp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome),
    path('home/', home),
    path('project_list/', project_list),
    path('delete_project/', delete_project),
    path('add_project/', add_project),
    re_path(r"^child/(?P<eid>.+)/(?P<oid>.*)/(?P<ooid>.*)/$", child),
    path('login/', login),
    path('login_action/', login_action),
    path('register_action/', register_action),
    path('accounts/login/', login),
    path('logout/', logout),
    path('tucao/', tucao),
    path('help/', api_help),
    re_path(r'^apis/(?P<id>.*)/$', open_apis),
    re_path(r'^cases/(?P<id>.*)/$', open_cases),
    re_path(r'^project_set/(?P<id>.*)/$', open_project_set),
    re_path(r'^save_project_set/(?P<id>.*)/$', save_project_set),
    re_path(r'^project_api_add/(?P<Pid>.*)/$', project_api_add),
    re_path(r'^project_api_del/(?P<id>.*)/$', project_api_del),
    path('save_bz/', save_bz),
    path('get_bz/', get_bz),
    path('Api_save/', Api_save),
    path('get_api_data/', get_api_data),
    path('Api_send/', Api_send),
    path('copy_api/', copy_api),
    path('error_request/', error_request),
    path('Api_send_home/', Api_send_home),
    path('get_home_log/', get_home_log),
    path('get_api_log_home/', get_api_log_home),
    re_path(r'^home_log/(?P<log_id>.*)/$', home),
    re_path(r'^add_case/(?P<eid>.*)/$', add_case),
    re_path(r'^del_case/(?P<eid>.*)/(?P<oid>.*)/$', del_case),
    re_path(r'^copy_case/(?P<eid>.*)/(?P<oid>.*)/$', copy_case),
    path('get_small/', get_small),
    path('user_upload/', user_upload),
    path('add_new_step/', add_new_step),
    re_path(r'^delete_step/(?P<eid>.*)/$', delete_step),
    path('get_step/', get_step),
]
