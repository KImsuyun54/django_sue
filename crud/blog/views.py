from django.shortcuts import render, redirect ,get_object_or_404
from .models import Blog, Human
from .forms import HumanForm
from random import choice
# Create your views here.
def layout(request):
    return render(request, 'blog/layout.html')

def main(request):
    return render(request, 'blog/main.html')

def board(request):
    human = Human.objects
    return render(request, 'blog/board.html', {'posts': human})

def create(request):
    if request.method == "POST":
        form = HumanForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.habit = choice(['빨강', '주황', '노랑', '초록', '파랑', '보라'])
            form.save()
            return redirect('board')
    else:
        form = HumanForm()
        return render(request, 'blog/main.html', {'form': form})

def read(request):
    return redirect('board')

def update(request, pk):
    suho = get_object_or_404(Human, pk=pk)
    if request.method == "POST":
        form = HumanForm(request.POST, instance=suho)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('board')
    else:
        ddd = HumanForm(instance=suho)
        return render(request, 'blog/main.html', {'form':ddd})

def delete(request, pk):
    post = get_object_or_404(Human, pk=pk)
    post.delete()
    return redirect('board')