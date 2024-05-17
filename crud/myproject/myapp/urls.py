from django.urls import path
from .views import UserDetail, CustomUserInfo, DeletedUserDetail, LoginView,UserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("user/", UserDetail.as_view(), name='user'),
    path("user/<int:id>/", CustomUserInfo.as_view(), name="customuser-info"),
    path('deletedusers/', DeletedUserDetail.as_view()), 
    path('restore/<int:id>/', DeletedUserDetail.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/',LoginView.as_view()),
    path('users/',UserView.as_view()),
]
