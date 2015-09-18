from django.conf.urls import url, patterns

urlpatterns = patterns('hello',
    url(r'^$', 'views.index', name='index')
)