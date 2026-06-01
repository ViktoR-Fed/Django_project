from django.urls import path

from blog import views
from blog.apps import BlogConfig

app_name = BlogConfig.name


urlpatterns = [
    path("blogs/", views.BlogListView.as_view(), name="blog_list"),
    path("blogs/<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("blog/create/", views.BlogCreateView.as_view(), name="blog_create"),
    path("blog/update/<int:pk>/", views.BlogUpdateView.as_view(), name="blog_update"),
    path("blog/delite/<int:pk>/", views.BlogDeleteView.as_view(), name="blog_delite"),
]
