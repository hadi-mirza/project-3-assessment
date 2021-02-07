from django.urls import path
from . import views
# from .views import WidgetDelete

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:widget_id>/delete/', views.delete, name='widget_delete'),
]