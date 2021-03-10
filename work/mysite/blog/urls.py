from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from blog import views
from .views import PostUpdateView, PostDeleteView, AddCommentView

urlpatterns=[
    path("", views.index, name='index'),

    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post"),
    path("post/create", views.PostCreate.as_view(), name="post_create"),
    path("fav/<int:id>/", views.favourite_post, name="favourite_post"),
    path("profile/favourites", views.favourite_list, name="favourite_list"),
    path("profile/mypost", views.blog_list, name="blog_list"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:pk>/comment/", views.AddCommentView.as_view(), name="add_comment"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)