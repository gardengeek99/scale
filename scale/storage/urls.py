"""Defines the URLs for the RESTful storage services"""
from django.conf.urls import url

import storage.views as views

urlpatterns = [
    url(r'^files/$', views.FilesView.as_view(), name='files_view'),
    url(r'^workspaces/$', views.WorkspacesView.as_view(), name='workspaces_view'),
    url(r'^workspaces/(\d+)/$', views.WorkspaceDetailsView.as_view(), name='workspace_details_view'),
    url(r'^workspaces/validation/$', views.WorkspacesValidationView.as_view(), name='workspaces_validation_view'),
]
