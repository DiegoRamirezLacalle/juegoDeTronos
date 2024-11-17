from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('characters/', views.characters_list, name='characters_list'),
    path('characters/<int:character_id>/', views.character_detail, name='character_detail'),
    path('houses/', views.houses_list, name='houses_list'),
    path('houses/<int:house_id>/', views.house_detail, name='house_detail'),
    path('seasons/', views.seasons_list, name='seasons_list'),
    path('seasons/<int:season_id>/', views.season_detail, name='season_detail'),
    path('', views.index, name='index'),  # Ruta principal para la vista "index"
]
