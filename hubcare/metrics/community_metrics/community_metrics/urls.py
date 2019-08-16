"""community_metrics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('community/admin/', admin.site.urls),
    path('community/code_of_conduct/', include('code_of_conduct.urls')),
    path('community/contribution_guide/', include('contribution_guide.urls')),
    path('community/issue_template/', include('issue_template.urls')),
    path('community/license/', include('license.urls')),
    path('community/pull_request_template/', include('pull_request_template.urls')),
    path('community/release_note/', include('release_note.urls')),
    path('community/readme/', include('readme.urls')),
    path('community/description/', include('description.urls')),
]
