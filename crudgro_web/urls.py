from django.urls import path, include
from crudgro_web.views import all_articles
urlpatterns = [
    path('test/', all_articles)
]
