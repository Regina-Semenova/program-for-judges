from django.urls import path
from law_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("q/new", views.create_new, name="query_new"),
    path("q/<int:qid>", views.edit, name="query_edit"),
]