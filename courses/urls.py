from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^courses/$', views.ListCreateCourse.as_view(), name='course_list'),
    url(r'^courses2/$', views.ListCreateCourse2.as_view(), name='course_list2'),
    url(r'(?P<pk>\d+/$', views.RetrieveUpdateDestroyCourse.as_view(), name='course_detail'),

]