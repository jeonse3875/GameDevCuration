from django.http import HttpResponse  
from django.shortcuts import render
from django.views.generic import View
from .models import *

# Create your views here.
class DevInformationView(View):
    def get(self, request):
        game_id = int(request.GET.get('game_id',0))
        cur_tag = int(request.GET.get('cur_tag',0))
        sel_tag = list(map(int, request.GET.getlist('sel_tag',[])))
        

        try:
            targetGame = Game.objects.get(id = game_id)
        except Game.DoesNotExist:
            # 게임 선택 페이지 띄우기
            return render(request,'devinfo/home.html')

        if cur_tag in sel_tag:
            sel_tag.remove(cur_tag)
        else:
            sel_tag.append(cur_tag)
        
        sel_tag_url = ""

        for tag_id in sel_tag:
            sel_tag_url += f"&sel_tag={tag_id}"

        templateData = {}
        templateData["game"] = targetGame
        templateData["tags"] = targetGame.tags.all()
        templateData["sel_tag"] = sel_tag
        templateData["sel_tag_url"] = sel_tag_url

        #print(templateData)
        return render(request,'devinfo/home.html', templateData)