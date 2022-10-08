"""ecom_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path , include
from rest_framework import routers
from product import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

#router = routers.DefaultRouter()

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Posts API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('allproducts/',views.ProductList.as_view()),
    path('getproduct/<int:pk>',views.ProductRetrieve.as_view()),
    path('createproduct/',views.ProductCreate.as_view()),
    path('updateproduct/<int:pk>',views.ProductUpdate.as_view()),
    path('deleteproduct/<int:pk>',views.ProductDestroy.as_view()),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),



]
