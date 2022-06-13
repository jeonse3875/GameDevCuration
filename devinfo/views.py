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
        is_show_all = bool(request.GET.get('is_show_all',False))
        templateData = {}
        templateData["games"] = Game.objects.all()

        try:
            targetGame = Game.objects.get(id = game_id)
        except Game.DoesNotExist:
            # 게임 선택 페이지 띄우기
            return render(request,'devinfo/home.html', templateData)

        if cur_tag in sel_tag:
            sel_tag.remove(cur_tag)
        else:
            sel_tag.append(cur_tag)
        
        sel_tag_url = ""

        for tag_id in sel_tag:
            sel_tag_url += f"&sel_tag={tag_id}"

        templateData["game"] = targetGame
        templateData["tags"] = targetGame.tags.all()
        templateData["sel_tag"] = sel_tag
        templateData["sel_tag_url"] = sel_tag_url
        templateData["is_show_all"] = is_show_all

        try:
            templateData["cur_tag"] = Tag.objects.get(id=cur_tag)
        except Tag.DoesNotExist:
            pass
        
        #print(templateData)
        return render(request,'devinfo/home.html', templateData)