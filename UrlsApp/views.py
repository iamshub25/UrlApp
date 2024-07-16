from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .forms import URLForm

# Create your views here.


def shorten_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save()
            return render(request, 'success.html', {'short_code': url.short_code})
    else:
        form = URLForm()
    return render(request, 'index.html', {'form': form})

def redirect_original(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    url.click_count += 1
    url.save()
    return redirect(url.original_url)

def show(request):
    data = URL.objects.all()
    context={'data': data}
    return render(request,'urls.html',context)