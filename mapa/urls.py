from django.urls import path
from . import views

urlpatterns = [
    path('ilha/<int:ilha_id>/', views.detalhe_ilha, name='detalhe_ilha'),
    path('ilha/<int:ilha_id>/<str:categoria>/', views.detalhe_ilha_categoria, name='detalhe_ilha_categoria'),
    path('ilhas/', views.lista_ilhas, name='lista_ilhas'),
]
