from django.shortcuts import render
from .models import CvStructure
import requests


def home(request):
    city = CvStructure.objects.filter(name="Irmantas")[0].city
    print(city)

    # vardas = obj.order_by('city')
    # print(vardas)

    cvbankas = requests.get("https://www.cvbankas.lt/?miestas=" + city + "&padalinys%5B%5D=&keyw=Python")
    link1 = "https://www.cvbankas.lt/?miestas=" + city + "&padalinys%5B%5D=&keyw=Python"
    link2 = "https://www.cvbankas.lt/?miestas=" + 'Kaunas' + "&padalinys%5B%5D=&keyw=Python"
    cvonline = requests.get("https://www.cvonline.lt/")
    cvbankas_status = cvbankas.status_code
    cvonline_status = cvonline.status_code

    context = {'info': [{'status': cvbankas_status, 'link': link1}, {'status': cvbankas_status, 'link': link1}]}
    return render(request, 'base.html', context=context)
