from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostsListView.as_view(), name='index'),

    path('posts/<int:post_id>/',
         views.PostDetailView.as_view(),
         name='post_detail'),

    path('posts/<int:post_id>/comment/', views.CommCreateView.as_view(),
         name='add_comment'),

    path('posts/<int:post_id>/edit_comment/<int:comment_id>/',
         views.CommUpdateView.as_view(),
         name='edit_comment'),

    path('posts/<int:post_id>/delete_comment/<int:comment_id>/',
         views.CommDeleteView.as_view(),
         name='delete_comment'),

    path('category/<slug:slug>/', views.CategoryListsView.as_view(),
         name='category_posts'),

    path('posts/create/', views.PostCreateView.as_view(),
         name='create_post'),

    path('posts/<int:post_id>/edit/', views.PostUpdateView.as_view(),
         name='edit_post'),

    path('posts/<int:post_id>/delete/', views.PostDeleteView.as_view(),
         name='delete_post'),

    path('profile/edit/', views.UserUpdView.as_view(),
         name='edit_profile'),

    path('profile/<str:username>/', views.UserDetailsView.as_view(),
         name='profile')

]
