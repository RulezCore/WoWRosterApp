from frontend.views import home
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# API VIEWS
from api import views

# ROUTER
router = routers.DefaultRouter()
router.register('raid', views.ProjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls))
]


# FRONTEND VIEWS
urlpatterns += [
    path('', home),
]
