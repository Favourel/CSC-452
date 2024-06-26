"""
URL configuration for CSC452 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users.middlewares import LogoutCheckMiddleware

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path('', LogoutCheckMiddleware(auth_views.LoginView.as_view(template_name='users/login.html')), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('users.urls')),
    path('', include('feed.urls')),

    # path('djrichtextfield/', include('djrichtextfield.urls'))
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'feed.views.error_404'
handler500 = 'feed.views.error_500'
# handler403 = 'blog.views.error_403'
# handler400 = 'blog.views.error_400'

