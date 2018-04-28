"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from rest_framework import routers
from my_app import views
#from django.core.urlresolvers import reverse

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
#router.register(r'branch_detail', views.BranchDetailView)

urlpatterns = [
        url(r'^branch_detail/(?P<pk>[-\w]+)$', views.BranchDetailView.as_view(), name='branch-detail'),
        url(r'^branch_detail$', views.BranchListView.as_view(), name='branch-detail-by-param'),
        ]


#url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
