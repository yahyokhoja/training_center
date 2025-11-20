from django.urls import path
from . import views

app_name = "candidates"

urlpatterns = [
    path("create/", views.cv_create, name="cv_create"),
    path("detail/", views.cv_detail, name="cv_detail"),
    path("edit/", views.cv_edit, name="cv_edit"),

    # Skills
    path("skill/add/", views.skill_add, name="skill_add"),
    path("skill/delete/<int:skill_id>/", views.skill_delete, name="skill_delete"),
]
