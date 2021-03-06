"""Vapthy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
# from django.views.generic import RedirectView
# from django.conf.urls import url
from django.views.generic.base import RedirectView


urlpatterns = [
    # url(r'^favicon.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    # url(r'^favicon.ico$', RedirectView.as_view(url='/static/image/favicon.ico')),
    path('favicon.ico/', RedirectView.as_view(url='/static/image/favicon.ico')),
    path('admin/', admin.site.urls),
    path('home/', include(('home.urls'))),
    path('', include(('accounts.urls'))),
    path('', include(('contact.urls'))),
    path('post/', include(('post.urls'), namespace='post')),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
