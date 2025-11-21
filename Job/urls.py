from django.urls import path
from . import views

app_name = "Job"

urlpatterns = [
    path("", views.job_list, name="job_list"),
    path("<int:pk>/", views.job_detail, name="job_detail"),
    path("create/", views.create_job, name="create_job"),
    path("<int:pk>/edit/", views.edit_job, name="edit_job"),
    path("<int:pk>/delete/", views.delete_job, name="delete_job"),
]
