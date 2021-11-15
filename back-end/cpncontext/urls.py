from django.contrib import admin
from django.urls import path
from .views import cpncontextAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', cpncontextAPIView.as_view()),
    # path('ltlbyid',views.getLTLById)
]