from django.shortcuts import render
from .models import Blog
# Create your views here.
def layout(request):
    return render(request, 'blog/layout.html')
def main(request):
    return render(request, 'blog/main.html')
def board(request):
    suho = Blog.objects
    return render(request, 'blog/board.html',{'blogs':suho})