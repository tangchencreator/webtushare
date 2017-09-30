from django.conf.urls import url
import views

urlpatterns = [
    url(r'^stockbasic/$', views.stockBasic_list),
    url(r'^stockbasic/(?P<code>[0-9]+)/$', views.stockBasic_detail),
]