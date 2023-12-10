# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Tag
from .forms import PostForm, TagForm


def post_list(request):
    # Redirige a la página de creación de post si el parámetro 'create' está presente en la URL
    if 'create' in request.GET:
        return redirect('create_post')
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Incrementa el contador de visitas cada vez que se visualiza el post
    post.visit_count += 1
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post})


def home(request):
    return render(request, 'home.html')


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            # Guardar tags asociados al post
            tags = request.POST.getlist('tags')  # Asumiendo que los tags son una lista de IDs en tu formulario
            post.tags.set(tags)

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


def create_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = TagForm()
    return render(request, 'blog/create_tag.html', {'form': form})