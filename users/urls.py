from django.urls import path
from .views import SignUpView, ProtectedView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("protected/", ProtectedView.as_view(), name="protected"),
]
