from django.shortcuts import render, redirect
from .models import User, Message
from .forms import UserForm, MessageForm


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['user_id'] = user.id
            return redirect('chat')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


def chat(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('register')

    user = User.objects.get(id=user_id)
    messages = Message.objects.all().order_by('-timestamp')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = user
            message.save()
            return redirect('chat')
    else:
        form = MessageForm()
    return render(request, 'chat.html', {'messages': messages, 'form': form, 'user': user})

def edit(request, message_id):
    message = Message.objects.get(id=message_id)

    if request.method == "POST":
        form = MessageForm(request.POST, instance=message)
        if form.is_valid:
            form.save()
            return redirect('chat')
    else:
        form = MessageForm(instance=message)

    return render(request, 'edit.html', {"form": form})

def delete(request, message_id):
    message = Message.objects.get(id=message_id)
    user_id = request.session.get('user_id')

    if message.user.id == user_id:
        message.delete()

    return redirect('chat')