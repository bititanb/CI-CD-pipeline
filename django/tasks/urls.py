from django.conf.urls import url

from tasks import views

urlpatterns = [
    url(r'^category/(?P<slug>[-\w\d]+)/$', views.TaskList.as_view(), name='tasklist'),
    url(r'^recipe/create/$', views.RecipeCreateView.as_view(), name='recipecreateview'),
    url(r'^add/$', views.TaskAdd.as_view(), name='taskadd'),
    url(r'^(?P<pk>\d+)/$', views.TaskUpdate.as_view(), name='taskupdate'),
    url(r'^(?P<pk>\d+)/delete/$', views.TaskDelete.as_view(), name='taskdelete'),
]
