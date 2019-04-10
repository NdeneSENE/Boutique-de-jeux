from django.urls import path, include
from rest_framework import routers                    # add this
from shop import views                            # add this

router = routers.DefaultRouter()                      # add this
router.register(r'games', views.GameView, 'shop')     # add this
from . import views

app_name = 'shop'

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path("loguser", views.login_user, name="loguser"),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/error', views.payment_error, name='payment_error'),
    path('payment/cancel', views.payment_cancel, name='payment_cancel'),
    path('catalog', views.catalog_view, name='catalog'),
    path('games/<int:game_id>/info', views.game_info, name='game_info'),
    path('games/<int:game_id>/play', views.play_game, name='play_game'),
    path('developer', views.developer_view, name='developer'),
    path('search', views.search, name='search'),
    path('developer/publish', views.publish_page_view, name='publish'),
    path('developer/publish_game', views.create_game, name='publish_game'),
    path('developer/mygames', views.developer_games, name='developer_games'),
    path('developer/games/<int:game_id>/edit', views.edit_game, name='editgame'),
    path('developer/games/<int:game_id>/update', views.edit_game_update, name='updategame'),
    path('developer/games/<int:game_id>/delete', views.edit_game_delete, name='deletegame'),
    path('facebook', views.facebook_handler, name='facebook_handler'),

]