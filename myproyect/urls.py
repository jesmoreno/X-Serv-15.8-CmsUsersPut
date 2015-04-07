from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^nuevo_usuario$', 'cms_users_put.views.signUp'),
    url(r'^inicio_sesion$', 'cms_users_put.views.signIn'),
    url(r'^cerrar_sesion$', 'cms_users_put.views.logOut'),
    url(r'\w*', 'cms_users_put.views.authenticated'),
 
)
