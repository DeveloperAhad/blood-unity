from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('post_list')
        print(form.errors)

    context = {'posts': posts, 'form': form}
    return render(request, 'portal/index.html', context)
