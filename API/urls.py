from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),

    path('api/projects/', ProjectListAPIView.as_view(), name="Project-list"),
    path('api/projects/<int:pk>/', ProjectDetailAPIView.as_view(), name="Project-detail"),
    
    path('api/tags/', TagListAPIView.as_view(), name="Tag-list"),
    path('api/tags/<int:pk>/', TagDetailAPIView.as_view(), name="Tag-detail"),

    path('api/category/', CategoryListAPIView.as_view(), name="Category-list"),
    path('api/category/<int:pk>/', CategoryDetailAPIView.as_view(), name="Category-detail"),

    path('api/status/', StatusListAPIView.as_view(), name="Status-list"),
    path('api/status/<int:pk>/', StatusDetailAPIView.as_view(), name="Status-detail"),

]
   