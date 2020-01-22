from django.shortcuts import render

from album.models import PhotoBook


def album_list(request):
    photobooks = PhotoBook.objects.all()
    context = {
        'photobooks': photobooks,
    }
    return render(request, 'show-album.html', context)
