from django.urls import path
from . import views
urlpatterns=[
    path('kakao/',views.kakao_account),
    path('google/',views.google_account),
]