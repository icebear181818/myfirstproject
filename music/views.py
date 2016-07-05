from django.http import HttpResponse
from django.shortcuts import render
from music.models import Album
from django.http  import Http404
def index(request):
    all_albums=Album.objects.all()
    context={
        'all_albums':all_albums,
    }
    return render(request,'music/index.html',context)

# Create your views here.
def detail(request,album_id):
    #return HttpResponse("<h2> Details for A id:"+str(album_id)+"/<h2>")
    try:
        album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("lalallala")
    return render(request,'music/detail.html',{'album':album})