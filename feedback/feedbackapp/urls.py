from django.urls import path

from .views import *

urlpatterns = [
    path('main/', FeedbackHome.as_view(), name='home'),
    path('add_page', AddPage.as_view(), name='add_page'),
    path('feedback/<slug:slug_feed>/', FeedbackDetail.as_view(), name='feed'),
    path('category/<slug:slug_category>/', FeedbackCategory.as_view(), name='category'),
    path('update-feedback/<slug:slug_feed>', UpdatePage.as_view(), name='update_view'),
    path('delete-feedback/<slug:slug_feed>', DeletePage.as_view(), name='delete_feed'),
]

