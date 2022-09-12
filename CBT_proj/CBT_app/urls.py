from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import index

urlpatterns = [
    path('Questions/', views.QuestionList.as_view()),
    path('Questions/<int:pk/>', views.QuestionList.as_view()),
    path('index/', views.index, name="index"),
]
