from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    context = {'phones': phones
               }

    for phone in phones:
        features = phone.features.all()
        for feature in features:
            print(feature)

    return render(
        request,
        template,
        context
    )
