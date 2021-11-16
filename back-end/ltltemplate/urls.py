from django.urls import path
from .import views
from .views import ltltemplateAPIView

urlpatterns = [
    path('api',views.ltltemplateAPIView.as_view()),
    path('ltltemplatebyid',views.getLTLTemplateById),
    # path('ltlbyid',views.getLTLById)
]