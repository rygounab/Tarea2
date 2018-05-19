from django.shortcuts import render, redirect
from basket.models import Player
from django.http import HttpResponse
from basket.forms import PlayerForm


def index(request):
    data = {}

    data['saludar'] = 'Hola dsfs'

    # SELECT * FROM player
    data['object_list'] = Player.objects.all()

    template_name = 'player/list_player.html'
    return render(request, template_name, data)


def detail(request, player_id):

    data = {}
    template_name = 'player/detail_player.html'

    # SELECT * FROM player WHERE id = player_id
    data['player'] = Player.objects.get(pk=player_id)
    # import pdb;pdb.set_trace()

    return render(request, template_name, data)

def agregar(request):
    if request.method=='POST':
        print("post")
        form=PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar:player_listar')
        else:
            print(form.errors)
    else:
        print("no post")
        form=PlayerForm()

    template_name='player/agregar.html'
    return render(request,template_name,{'form':form})


def listar(request):
    data={}
    data['object_list'] = Player.objects.all()
    template_name='player/listar.html'
    return render(request, template_name,data)
