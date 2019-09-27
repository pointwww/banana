from django.urls import path
from players.views import IndexView

app_name = 'players'

urlpatterns = [
    # /players/
    path('', IndexView.as_view(), name='index'),
]
