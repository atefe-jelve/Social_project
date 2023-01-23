from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.ListPostView.as_view(), name='posts_list'),
    path('detail_post/<int:post_id>/<slug:post_slug>', views.DetailPostView.as_view(), name='post_detail'),
    path('delete/<int:post_id>', views.DeletePostView.as_view(), name='post_delete'),
    path('update/<int:post_id>', views.UpdatePostView.as_view(), name='post_update'),
    path('create/', views.CreatePostView.as_view(), name='post_create'),
    path('reply/<int:post_id>/<int:comment_id>', views.PostAddReplyView.as_view(), name='add_reply'),
    path('like/<int:post_id>/', views.PostLikeView.as_view(), name='post_like'),

]
