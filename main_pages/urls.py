from django.urls import path
from . import views

urlpatterns = [
    path('create_post/', views.PostCreate.as_view()),
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('<int:pk>/add_comment/', views.add_comment),
    # path('tag/<str:slug>/', views.tag_page),
    path('update_post/<int:pk>/',views.PostUpdate.as_view()),
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    # 태그 내 문자열로 들어가면
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
    # path('', views.index),
    # path('', views.index)
]