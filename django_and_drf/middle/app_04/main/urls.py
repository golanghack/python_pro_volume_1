from django.urls import path
from main.views import (index, other_page, AppLoginView,
                        profile, AppLogoutView, ChangeUserInfoView,
                        AppPasswordChangeView, RegisterUserView,
                        RegisterDoneView)

app_name = 'main'
urlpatterns = [
    path('accounts/register/done/', RegisterDoneView.as_view(),
                                            name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), 
                                            name='register'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), 
                                            name='change_user_info'),
    path('accounts/logout/', AppLogoutView.as_view(), name='logout'),
    path('accounts/password/change', AppPasswordChangeView.as_view(), 
                                            name='password_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', AppLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]