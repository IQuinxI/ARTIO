
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
urlpatterns = [
    path('api/', include('Artapp.urls')),
    path('admin/', admin.site.urls),

]

# urlpatterns += [
#     path('auth/', include('djoser.urls')),
#     path('auth/', include('djoser.urls.jwt'))
# ]
#
# urlpatterns += [
#     re_path(r'^.*', TemplateView.as_view(template_name='index.html'))
# ]
urlpatterns += [
    path('api-auth', include('rest_framework.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#EMAIL
# Artio.App1@gmail.com
# artio123
#Apppsswrd: iumhgrftksmadloz

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'Artio.App1@gmail.com'
# EMAIL_HOST_PASWORD = 'iumhgrftksmadloz'
# EMAIL_USE_TLS = True