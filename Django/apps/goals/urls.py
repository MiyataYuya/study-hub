from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.GoalListView.as_view(), name='goal_list'),
    path('goal/<int:pk>/', views.GoalDetailView.as_view(), name='goal_detail'),
    path('goal/create/', views.GoalCreateView.as_view(), name='goal_create'),
    path('goal/<int:pk>/update/', views.GoalUpdateView.as_view(), name='goal_update'),
    path('goal/<int:pk>/delete/', views.GoalDeleteView.as_view(), name='goal_delete'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # ログインページ

]

