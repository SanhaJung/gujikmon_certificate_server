from django.urls import path
from . import views
urlpatterns=[
    path('login/kakao/',views.kakao_account),
    path('login/google/',views.google_account),
    path('withdrawal/',views.user_Withdrawal),
]