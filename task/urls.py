from django.urls import path

from .views import *


urlpatterns = [ 

    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('reset-password/', PasswordResetView.as_view(), name='password-reset'),
    path('student-list/', StudentListView.as_view(), name='student-list-create'),
    path('student/', StudentView.as_view(), name='student-list')

]
