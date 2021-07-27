from django.urls import path
from .views import GetPairs,handler404

app_name = "app"
handler404 = handler404

urlpatterns = [
    path('get-pairs',GetPairs.as_view(),name='get-pairs')
]