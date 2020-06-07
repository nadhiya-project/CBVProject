from django.conf.urls import url
from basic_app import views

app_name="basic_app"

urlpatterns=[
#url(r'^home/',views.HomeView.as_view(),name="home"),
url(r'^$',views.SchoolListView.as_view(),name="list"),
url(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name="detail"),

]
