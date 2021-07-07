from django.shortcuts import render, redirect
from .models import newpost, comment
# Create your views here.
def index(request):
    new = newpost.objects.all()
    content = {'new': new}
    return render(request,'one/index.html', content)

def new(request):
    users = newpost.objects.all()
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('image')
        for img in images:
            post = newpost.objects.create(
                name = data['name'],
                email = data['email'],
                description = data['description'],
                location = data['location'],
                image = img
            )
        return redirect('home')
    return render(request, 'one/newpost.html')

def view(request, pk):
    post = newpost.objects.get(id=pk)
    commentdb = comment.objects.all()
    if request.method == 'POST':
        commentvalue = request.POST
        contents = request.POST.getlist('content')
        print('commentvalue: ',commentvalue)
        print('comnts:',contents)
        for cmnt in contents:
            newcomment = comment.objects.create(
                content = commentvalue['content']
            )
        
    contents = {'post': post, 'commentdb': commentdb}
    return render(request, 'one/view.html', contents)

def login(request):
    return render(request, 'one/login.html')

def register(request):
    return render(request, 'one/register.html')