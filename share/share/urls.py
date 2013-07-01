from django.conf.urls import patterns, include, url
from share_app import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home),
    url(r'^home$', views.home),
    url(r'^profile$', views.profile),
    url(r'^login$', views.login_user),
    url(r'^logout$', views.logout_user),
    url(r'^submitlogin$', views.submitlogin),
    url(r'^signup$', views.signup),
    # url(r'^$', 'share.views.home', name='home'),
    # url(r'^share/', include('share.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
