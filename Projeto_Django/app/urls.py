"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from PCs.views import cadastro_view,DesktopCreateView, PCs_view, DesktopDetailView, DesktopUpdateView, DesktopDeleteView, sobre_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('PCs/',PCs_view, name='PCs'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('sobre/', sobre_view, name='sobre'),
    path('new_desktop/', DesktopCreateView.as_view(), name='new_desktop' ),
    path('desktop/<int:pk>/', DesktopDetailView.as_view(), name='desktop_detail' ),
    path('desktop/<int:pk>/update/', DesktopUpdateView.as_view(), name = 'desktop_update'),
    path('desktop/<int:pk>/delete/', DesktopDeleteView.as_view(), name = 'desktop_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




