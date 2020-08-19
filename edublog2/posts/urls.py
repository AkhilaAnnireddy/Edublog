from django.urls import path
from .import  views
app_name = 'posts'
urlpatterns=[
    path('create/',views.CreatePost.as_view(), name='create'),
    path('myposts/',views.ListPost.as_view(), name='myposts'),
    path('update/<int:pk>',views.UpdatePost.as_view(), name='update'),
    path('delete/<int:pk>',views.DeletePost.as_view(), name='delete'),
    path('detail/<int:pk>',views.PostDetailView.as_view(), name='post-detail'),
    path('user/<int:pk>',views.UserPostList.as_view(),name='user-posts'),
    path('favourites/', views.post_favourite_list, name="post_favourite_list"),
    path('favourite_post/<int:pk>', views.favourite_post, name="favourite_post"),
    path('like_post/<int:pk>', views.like_post, name="like_post"),

]
