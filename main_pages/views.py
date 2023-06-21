from unicodedata import category

from .forms import CommentForm
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload']



class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            tags = self.request.POST.getlist('tags')

            # 해시태그 추가
            for tag in tags:
                tag = tag.strip()
                if tag.startswith('#'):
                    tag = tag[1:]  # 해시태그 기호(#) 제거
                if tag != '':
                    form.instance.tags.add(tag)

            return super().form_valid(form)
        else:
            return redirect('/main_pages/')


class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        # context['no_Hashtag_count'] = Post.objects.filter(category=None).count()
        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        # context['no_Hashtag_count'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        return context


# def categories_page(request, slug):
#     if slug == 'no-category':
#         category = '미분류'
#         post_list = Post.objects.filter(category=None)
#     else:
#         category = Category.objects.get(slug=slug)
#         post_list = Post.objects.filter(category=category)
#
#     context = {
#         'category': category,
#         'categories': Category.objects.all(),
#         'post_list': post_list,
#         'no_category_count': Post.objects.filter(category=None).count()
#     }
#     return render(request, 'main_pages/post_list.html', context)


# tag_cloud_view.html을 보여주겠다.
class TagCloudTV(TemplateView):
    template_name = 'taggit/tag_cloud_view.html'

# 태그가 있으면 태그를 보여주겠다.
class TaggedObjectLV(ListView):
    template_name = 'taggit/tag_with_post.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context



def add_comment(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        comment_temp = comment_form.save(commit=False)
        comment_temp.post = post
        comment_temp.author = request.user
        comment_temp.save()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionError

