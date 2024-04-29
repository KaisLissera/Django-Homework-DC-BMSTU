from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    #FBV
    # path('', views.index, name = 'index'),
    # path('bugs/', views.bug_list, name = 'bug_list'),
    # path('bugs/<int:bug_id>/', views.bug_detail, name = 'bug_detail'),
    # path('bugs/create/', views.create_bug, name='create_bug'),
    # path('bugs/<int:bug_id>/update/', views.update_bug, name='update_bug'),
    # path('bugs/<int:bug_id>/delete/', views.delete_bug, name='delete_bug'),

    # path('features/', views.feature_list, name = 'feature_list'),
    # path('features/<int:feature_id>/', views.feature_detail, name = 'feature_detail'),
    # path('features/create/', views.create_feature, name='create_feature'),
    # path('features/<int:feature_id>/update/', views.update_feature, name='update_feature'),
    # path('features/<int:feature_id>/delete/', views.delete_feature, name='delete_feature'),

    #CBV
    path('', views.IndexView.as_view(), name = 'index'),
    path('bugs/', views.BugReportListView.as_view(), name = 'bug_list'),
    path('bugs/<int:bug_id>/', views.BugReportDetailView.as_view(), name = 'bug_detail'),
    path('bugs/new/', views.BugReportCreateView.as_view(), name = 'create_bug'),
    path('bugs/<int:bug_id>/update/', views.BugReportUpdateView.as_view(), name='update_bug'),
    path('bugs/<int:bug_id>/delete/', views.BugReportDeleteView.as_view(), name='delete_bug'),

    path('features/', views.FeatureRequestListView.as_view(), name = 'feature_list'),
    path('features/<int:feature_id>/', views.FeatureRequestDetailView.as_view(), name = 'feature_detail'),
    path('features/new/', views.FeatureRequestCreateView.as_view(), name = 'create_feature'),
    path('bugs/<int:feature_id>/update/', views.FeatureRequestUpdateView.as_view(), name='update_feature'),
    path('features/<int:feature_id>/delete/', views.FeatureRequestDeleteView.as_view(), name='delete_feature'),

]