from django.urls import path
from django.contrib.auth import views as auth_views
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course, name='course'),
    path('contact/', views.contact, name='contact'),
    path('single/<int:pk>/', views.singleCourse, name='single'),
    path('signup/', views.signUp, name='signup'),
    path('login/', views.signIn, name='login'),
    path('logout', views.signOut, name='logout'),
    path('new/', views.addBook, name='add'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='forgot.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password-sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='confirm-password.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password-complete.html'), name='password_reset_complete'),




    path('retrieve_&_create/', views.BookAPIView.as_view(), name="create_book"),
    path('update_book/<int:pk>/', views.EditAPIView.as_view(), name="update"),
]