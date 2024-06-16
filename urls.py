from django.urls import path

import views

# In this example, we've separated out the views.py into a new file
urlpatterns = [
    path('', views.index),
    path('table', views.game_info),
    path('pricing', views.game_discount),
    path('ratings', views.game_ratings)
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

