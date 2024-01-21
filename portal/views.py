from django.shortcuts import render, redirect

from notification.utlitys import create_news_create_notification_for_all_users, create_blood_request_notifications, \
    create_blood_bank_notifications
from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            if form.instance.post_type == 'news':
                create_news_create_notification_for_all_users(form.instance.id)
            if form.instance.post_type == 'blood_request':
                create_blood_request_notifications(form.instance.id, form.instance.blood_group, form.instance.district)
                create_blood_bank_notifications(form.instance.id, form.instance.blood_group, form.instance.district)
            return redirect('post_list')

    context = {'posts': posts, 'form': form}
    return render(request, 'portal/index.html', context)

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'portal/single.html', context)