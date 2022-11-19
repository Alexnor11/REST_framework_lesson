from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from demo.views import DemoView, WeaponView, CommentViewSet

r = DefaultRouter()
r.register('comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', DemoView.as_view()),
    path('weapon/<pk>/', WeaponView.as_view()),
] + r.urls
