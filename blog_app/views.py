from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog_app/post_list.html'
    context_object_name = 'posts'


    def get_queryset(self):
        # Фильтруем только опубликованные статьи (is_published=True)
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_app/post_detail.html'
    context_object_name = 'post'


def get_object(self, queryset=None):
    # Получаем объект стандартным способом
    obj = super().get_object(queryset)

    # Увеличиваем счётчик в памяти
    obj.views_count += 1
    # Сохраняем в БД
    obj.save(update_fields=['views_count'])

    return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog_app/post_form.html'
    fields = ['title', 'content', 'preview_image', 'is_published']
    success_url = reverse_lazy('blog_app:post_list')

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog_app/post_form.html'
    fields = ['title', 'content', 'preview_image', 'is_published']


    def get_success_url(self):
        return reverse_lazy('blog_app:post_detail', kwargs={'pk': self.object.pk})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog_app/post_confirm_delete.html'
    success_url = reverse_lazy('blog_app:post_list')