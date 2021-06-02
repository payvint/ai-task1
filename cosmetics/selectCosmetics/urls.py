from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:age_id>/<int:cosmetics_id>', views.selectedCosmetics, name='selectedCosmetics'),
    path('select/', views.select, name='select')
]