from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', TaskList.as_view(), {"slug": "all"}, name='tasklist'),
    url(r'^list/all/$', TaskList.as_view(), {"slug": "all"}, name='tasklist_all'),
    url(r'^list/uncategorized/$', TaskList.as_view(), {"slug": "uncategorized"}, name='tasklist_uncategorized'),
    url(r'^list/by-category/(?P<pk>\d+)-(?P<slug>[-\w\d]+)/$', TaskList.as_view(), name='tasklist_by_category'),
    url(r'^categories/list$', CategoryList.as_view(), name='categorylist'),
]
