"""palindrome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from checker.views import IndexView, PalindromeDetailView, PalindromeCreateView, FailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^palindrome/(?P<pk>\d+)$', PalindromeDetailView.as_view(), name="palindrome_detail_view"),
    url(r'^create_palindrome/$', PalindromeCreateView.as_view(), name="palindrome_create_view"),
    url(r'^fail/$', FailView.as_view(), name="fail_view")
]
