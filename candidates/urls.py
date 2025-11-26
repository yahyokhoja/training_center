from django.urls import path
from . import views

app_name = "candidates"

urlpatterns = [
    # CV CRUD
    path("create/", views.cv_create, name="cv_create"),
    path("<int:pk>/", views.cv_detail, name="cv_detail"),
    path("<int:pk>/edit/", views.cv_edit, name="cv_edit"),
    path("<int:pk>/delete/", views.cv_delete, name="cv_delete"),

    # Skills CRUD
    path("<int:cv_pk>/skill/add/", views.skill_add, name="skill_add"),
    path("skill/<int:pk>/delete/", views.skill_delete, name="skill_delete"),
]
