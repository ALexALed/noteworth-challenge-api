from django.urls import path

from . import views

urlpatterns = [
    path(
        r"employees", views.EmployeeViewSet.as_view({"get": "list"}), name="employees"
    ),
]
