from django.urls import path
from code_of_conduct.views import CodeOfConductView


urlpatterns = [
    path(
        '<str:owner>/<str:repo>/<str:token_auth>/',
        CodeOfConductView.as_view()
    )
]
