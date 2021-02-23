from django.urls import path
from .views import *

urlpatterns=[
    path('article/',ArticleAPIView.as_view()),
    path('article/<int:id>',ArticleDetails.as_view()),
    path('generic/article/<int:id>',GenericAPIView.as_view())
]

