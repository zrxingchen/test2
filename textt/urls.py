from django.urls import path
from textt import views # 导入视图文件
urlpatterns = [
    path('',views.index),# 配置访问首页的路由
]
