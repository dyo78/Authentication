from django.urls import path
from .views import BlogDetail,BlogInfo

urlpatterns=[

    path("detail/", BlogDetail.as_view(), name='blog'),
    path("detail/<int:id>/", BlogInfo.as_view()),

]