from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('branches/', views.BranchesAPIView.as_view(), name='branches'),
    path('branch/<int:pk>/', views.BranchDetailAPIView.as_view(), name='branch-detail'),
    path('banks/', views.BanksAPIView.as_view(), name='banks'),
    path('bank/<int:pk>/', views.BankDetailAPIView.as_view(), name='bank-detail'),
    path('create_account/', views.CreateAccountAPIView.as_view(), name='create-account'),
    path('accounts/', views.AccountListAPIView.as_view(), name='accounts'),
]