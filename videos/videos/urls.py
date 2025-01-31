from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from rest_framework import  routers
from webvideos.views import Userview, Videoview

router = routers.DefaultRouter()
router.register(r'users', Userview)
router.register(r'videos', Videoview)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('videos/', include('webvideos.urls')),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('', include(router.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
