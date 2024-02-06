from django.shortcuts import render, redirect
from .forms import ImageForm


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm(request.user)
    return render(request, 'upload_image.html', {'form': form})
