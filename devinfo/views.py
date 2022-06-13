from django.http import HttpResponse  
from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class DevInformationView(View):
    def get(self, request):
        # 뷰 로직 작성
        return render(request,'devinfo/home.html')