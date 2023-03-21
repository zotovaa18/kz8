from django.shortcuts import render
from django.http import HttpResponse
from .models import Preferences
from .forms import PrefFrom, TinderForm
from .openai import where_to_go

def main_page(request):
    return render(request, 'Blank page.html')
def index(request):
    form = PrefFrom()
    if request.method =="POST":
        print(request.POST)
        form = PrefFrom(request.POST)
        if form.is_valid():
            print(form.cleaned_data['review'])
            answer = where_to_go(form.cleaned_data['review'])
            context = {'answer':answer}
            #form.save()
            return render(request, 'preference_form_answer.html', context)


    context = {'form':form}
    return render(request, 'preferences_form.html', context)


def tindef_from(request):
    form = TinderForm()
    if request.method =="POST":
        print('responses are here!')
        print(request.POST)
        form = TinderForm(request.POST)

        #print(form.cleaned_data['geeks_field'])
        context = {'answer': "submitted!"}
        return render(request, 'preference_form_answer.html', context)


    context = {'form':form}
    return render(request, 'tinder_form.html', context)


def review_by_id(request, review_id):
    review = Preferences.objects.get(pk=review_id)
    return render(request, 'review_details.html', {'review':review})


def dashboard(request):
    labels = ["1", "2","3", "4", "5"]
    data = [0,0,0,0,0]

    print('dashboard')
    queryset = Preferences.objects.order_by('-rating')
    for rev in queryset:

        data[rev.rating-1] += 1

    print(labels)
    print(data)
    return render(request, 'dashboard.html',{'labels':labels, 'data':data})

