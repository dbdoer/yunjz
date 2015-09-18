#coding=utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yunjz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #将accounts模块的请求，转给accounts模块的urls去处理
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
)
