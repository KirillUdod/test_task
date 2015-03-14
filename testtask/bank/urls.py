from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'bank.views.send_money', name='show'),
)
