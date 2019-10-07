
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# API VIEWS
from api import views

# FRONTEND VIEWS
from frontend.views import home, raids, members, logout

# ROUTER
router = routers.DefaultRouter()
router.register('raid', views.ProjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('logout', logout, name='logout')
]


# FRONTEND VIEWS
urlpatterns += [
    path('', home, name="home"),
    path('raids/', raids, name="raids"),
    path('members/', members, name="members")
]
