from django.conf.urls import url
from api import views
#
# 配置私有项目转发路由
urlpatterns = [
 url(r'selectinfo',views.selectinfo),
]