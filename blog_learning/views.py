from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from blog_learning.forms import PostForm
from blog_learning.models import Post




def lista_posts(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog_learning/lista_posts.html', {'page_obj': page_obj, 'creador': request.user})



def filtrar_por_fecha(request):
    orden = request.GET.get('orden', 'reciente')

    if orden == 'reciente':
        posts = Post.objects.order_by('-fecha_publicacion')
    elif orden == 'antigua':
        posts = Post.objects.order_by('fecha_publicacion')
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog_learning/lista_posts.html', {'page_obj': page_obj})


@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.creador = request.user
            post.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'blog_learning/crear_post.html', {'form': form})



def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog_learning/detalle_post.html', {'post': post, 'creador': request.user})


@login_required
def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalle_post', post_id=post_id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog_learning/editar_post.html', {'form': form, 'post': post})


@login_required
def eliminar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('lista_posts')

def about(request):
    return render(request, 'blog_learning/about.html')
