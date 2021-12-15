from django.contrib import admin
from django.urls import path
from .views import cpncontextAPIView
from cpncontext import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', cpncontextAPIView.as_view()),
    path('cpncontextbyid', views.getCPNcontextById),
    # path('ltlbyid',views.getLTLById)
]