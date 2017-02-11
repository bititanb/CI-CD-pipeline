from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', TaskList.as_view(), {"slug": "all"}, name='tasklist'),
    url(r'^list/all/$', TaskList.as_view(), {"slug": "all"}, name='tasklist_all'),
    url(r'^list/uncategorized/$', TaskList.as_view(), {"slug": "uncategorized"}, name='tasklist_uncategorized'),
    url(r'^list/by-category/(?P<pk>\d+)-(?P<slug>[-\w\d]+)/$', TaskList.as_view(), name='tasklist_by_category'),
    url(r'^categories/create$', CategoryCreate.as_view(), name='categorycreate'),
    url(r'^categories/(?P<pk>\d+)-(?P<slug>[-\w\d]+)/$', CategoryUpdate.as_view(), name='categoryupdate'),
    url(r'^categories/list$', CategoryList.as_view(), name='categorylist'),
    url(r'^categories/(?P<pk>\d+)-(?P<slug>[-\w\d]+)/delete$', CategoryDelete.as_view(), name='categorydelete'),
    #url(r'^recipe/create/$', RecipeCreateView.as_view(), name='recipecreateview'),
    #url(r'^add/$', TaskAdd.as_view(), name='taskadd'),
    #url(r'^(?P<pk>\d+)/$', TaskUpdate.as_view(), name='taskupdate'),
    #url(r'^(?P<pk>\d+)/delete/$', TaskDelete.as_view(), name='taskdelete'),
]
