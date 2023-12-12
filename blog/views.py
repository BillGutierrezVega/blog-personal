# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from twilio.rest import Client

from .models import Post, Comentario
from .forms import PostForm, TagForm, ComentarioForm


def post_list(request):
    # Redirige a la página de creación de post si el parámetro 'create' está presente en la URL
    if 'create' in request.GET:
        return redirect('create_post')
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = Comentario.objects.filter(post=post)

    # Aumentar el contador de visitas solo en solicitudes GET
    if request.method == 'GET':
        post.visit_count += 1
        post.save()
    # Incluye el formulario en el contexto
    form = ComentarioForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comentarios': comentarios, 'form':form})

def add_comentario(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.author = request.user
            comentario.post = post
            comentario.save()

    return redirect('post_detail', pk=pk)




# def send_twilio_message(post_title, commenter_name, author_name, phone_number):
#     # Configura tu cuenta de Twilio
#     account_sid = 'TU_TWILIO_ACCOUNT_SID'
#     auth_token = 'TU_TWILIO_AUTH_TOKEN'
    # client = Client(account_sid, auth_token)

    # Cuerpo del mensaje
    # message_body = f"{post_title}\n\nNombre del post ({author_name})\n\n{comentario}\n\nEste post tiene un nuevo comentario de {commenter_name}"

    # Cambia los números por los valores adecuados
    # from_whatsapp_number = 'whatsapp:+14155238886'
    # to_whatsapp_number = f'whatsapp:{phone_number}'

    # Envía el mensaje
    # message = client.messages.create(
    #     body=message_body,
    #     from_=from_whatsapp_number,
    #     to=to_whatsapp_number
    # )



def toggle_like(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST' and 'like' in request.POST:
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            post.visit_count -= 1
        else:
            post.likes.add(request.user)
            post.visit_count -= 1

        post.save()

    return redirect('post_detail', pk=pk)


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