from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "photo")
    success_url = reverse_lazy("blog:blog_list")


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"

    def get_queryset(self):
        """
        Переопределяем метод get_queryset для фильтрации статей
        Выводим только опубликованные статьи (publication_sing=True)
        """
        return Blog.objects.filter(is_publication=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "photo")
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")
