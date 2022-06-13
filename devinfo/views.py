from django.http import HttpResponse  
from django.shortcuts import render
from django.views.generic import View
from .models import *

# Create your views here.
class DevInformationView(View):
    def get(self, request):
        game_id = request.GET.get('game_id',0)
        tag_id = request.GET.get('tag_id',0)

        try:
            targetGame = Game.objects.get(id = game_id)
        except Game.DoesNotExist:
            return render(request,'devinfo/home.html')
        
        templateData = {}
        templateData["game"] = targetGame
        templateData["tags"] = targetGame.tags.all()

        print(templateData)
        return render(request,'devinfo/home.html', templateData)