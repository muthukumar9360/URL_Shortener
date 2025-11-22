from django.shortcuts import render, redirect, get_object_or_404
import random, string
from .forms import URLForm
from .models import URL

def generate_shortcode(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def home(request):
    form = URLForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.short_code = generate_shortcode()
        instance.save()
        return render(request, 'success.html', {
            'short_url': request.build_absolute_uri('/') + instance.short_code
        })
    return render(request, 'home.html', {'form': form})

def list(request):
    urls = URL.objects.all()
    return render(request, 'view.html', {'urls': urls})

def redirect_short_url(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    return redirect(url.long_url)
