from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'recordstudio', settings.ROOT_URLCONF, name='main_host'),
    host(r'about', 'about.urls', name='about'),

)
