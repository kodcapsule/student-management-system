

from django.urls import path
from .import views
urlpatterns = [
   path('', views.index, name="index"),
   path('students/',views.studentlist, name="students"),
   path('student/<int:id>/',views.student, name="student")
]
