from django.urls import path
from .views_ui import (
    student_list_ui,
    add_student_ui,
    delete_student_ui,
    update_student_ui,
)
from .views import StudentListCreateAPIView, StudentDetailAPIView

urlpatterns = [
    # API endpoints
    path("students/", StudentListCreateAPIView.as_view()),
    path("students/<int:id>/", StudentDetailAPIView.as_view()),

    # UI views
    path("students-ui/", student_list_ui, name="student_list_ui"),
    path("students-ui/add/", add_student_ui, name="add_student_ui"),
    path("students-ui/update/<int:student_id>/", update_student_ui, name="update_student_ui"),
    path("students-ui/delete/<int:student_id>/", delete_student_ui, name="delete_student_ui"),
]
