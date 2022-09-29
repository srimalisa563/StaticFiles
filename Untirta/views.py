from django.shortcuts import render

def index(request):
    context = {
        'judul' : 'Universitas Sultan Ageng Tirtayasa',
        'subjudul' : 'Welcome to Jawara University',
    }
    return render(request,'index.html',context)