from django.shortcuts import render
from django.http import HttpResponse
from .models import Preferences, Tinder_review_2, all_client_trips, Tour
from .forms import PrefFrom, TinderForm, ContactUs, Tinder_Review_Form, all_clients
from .openai import where_to_go


def main_page(request):
    return render(request, 'main.html')


def tours(request):
    tour_list = Tour.objects.all()
    print(tour_list)
    return render(request, 'tours.html', {'tour_list': tour_list})


def index(request):
    form = PrefFrom()
    if request.method =="POST":
        print(request.POST)
        form = PrefFrom(request.POST)
        if form.is_valid():
            print(form.cleaned_data['review'])
            answer = where_to_go(form.cleaned_data['review'])
            context = {'answer':answer, 'title':'Умный подбор'}
            #form.save()
            return render(request, 'preference_form_answer.html', context)


    context = {'form':form}
    return render(request, 'preferences_form.html', context)


def contactus_form(request):
    form = ContactUs
    if request.method == "POST":
        print('responses are here!')
        print(request.POST)
        form = ContactUs(request.POST)

        print(form)

        context = {'answer': "Ваш запрос принят! Мы свяжемся с вами в ближайшее время", "title":"Спасибо"}
        return render(request, 'preference_form_answer.html', context)

    context = {'form': form}
    return render(request, 'contactus_form.html', context)


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


def map(request):
    return render(request, 'smart_map.html')


def insurance(request):
    return render(request, 'insurance.html')


def routes_excursions(request):
    return render(request, 'routes_excursions.html')


def tinder_review(request):
    form = Tinder_Review_Form()
    if request.method == "POST":
        print('responses are here!')
        print(request.POST['is_pair'])
        form_submitted = TinderForm(request.POST)
        print(request.POST)
        is_pair = request.POST['is_pair']
        what = request.POST['what']
        rating = request.POST['rating']
        review = request.POST['review']
        Tinder_Review = Tinder_review_2(is_pair = is_pair,what = what, rating= rating,review=review  )
        Tinder_Review.save()
        # print(form.cleaned_data['geeks_field'])
        context = {'answer': "submitted!"}
        return render(request, 'preference_form_answer.html', context)

    context = {'form': form}
    return render(request, 'tinder_review_form.html', context)


def popular_destinations(request):
    print('dashhhh 2')
    labels_cities=["Сочи", "Санкт-Петербург", "Иркутск"]
    data_cities=[0,0,0]
    labels_tours = ['Жемчужина черноморья', 'По Пушкинским местам', 'Искусство на Неве',
                    'Великолепие Байкала', 'Красная поляна', 'Байкал']
    data_tours = [0,0,0,0,0,0]
    data_price=[]
    data_days=[]
    queryset = all_client_trips.objects.order_by('-days')
    for rev in queryset:
        data_price.append(rev.price)
        data_days.append(rev.days)
        if rev.city =="Сочи":
            data_cities[0]+=1
        elif rev.city =="Санкт-Петербург":
            data_cities[1] += 1
        elif rev.city =="Иркутск":
            data_cities[2] += 1

        if rev.tour == 'Жемчужина черноморья':
            data_tours[0]+=1
        elif rev.tour == 'По Пушкинским местам':
            data_tours[1]+=1
        elif rev.tour == 'Искусство на Неве':
            data_tours[2]+=1
        elif rev.tour == 'Великолепие Байкала':
            data_tours[3]+=1
        elif rev.tour == 'Красная поляна':
            data_tours[4]+=1
        elif rev.tour == 'Байкал':
            data_tours[5]+=1
    print(labels_cities)
    print(data_cities)
    print(labels_tours)
    print(data_tours)
    print(data_price)
    print(data_days)
    return render(request, 'dashboard_tours.html', {'labels_cities': labels_cities, 'data_cities': data_cities,
                                                            "labels_tours": labels_tours, "data_tours": data_tours,
                                                            "data_price": data_price, "labels_days": data_days,
                                                            })




def all_clients_form(request):
    print('all_clients_form')
    form = all_clients()
    if request.method == "POST":
        print('responses are here!')
        print(request.POST)
        city = request.POST['city']
        tour = request.POST['tour']
        price = request.POST['price']
        days = request.POST['days']
        client = all_client_trips(city = city, tour=tour, price=price, days=days)
        client.save()
        # print(form.cleaned_data['geeks_field'])
        context = {'answer': "submitted!"}
        return render(request, 'preference_form_answer.html', context)

    context = {'form': form}
    return render(request, 'cities.html', context)


def dashboard(request):
    print('dashboard func')
    labels_rating = ["1", "2","3", "4", "5"]
    data_rating = [0,0,0,0,0]

    print('dashboard')
    queryset = Tinder_review_2.objects.order_by('-rating')
    for rev in queryset:
        print(rev)
        print(rev.rating)
        rating = int(rev.rating)
        data_rating[rating-1] += 1

    print(labels_rating)
    print(data_rating)
    labels_pairs = ['Да', 'Нет']
    data_pairs = [0,0]
    for rev in queryset:
        if rev.is_pair == "1":
            data_pairs[0]+=1
        else:
            data_pairs[1] += 1
    labels_what = ['Только общались', 'Поехали в путешествие вместе', 'Завязались отношения', 'Поженились']
    data_what = [0,0,0,0]
    for rev in queryset:
        if rev.what =='talk':
            data_what[0] += 1
        elif rev.what =='trip':
            data_what[1]+=1
        elif rev.what =='continue':
            data_what[2] += 1
        elif rev.what =='married':
            data_what[3] += 1
    print(labels_rating)
    print(data_rating)
    print(labels_pairs)
    print(data_pairs)
    print(labels_what)
    print(data_what)
    return render(request, 'dashboard_tinder_review.html', {'labels_rating':labels_rating, 'data_rating':data_rating,
                                             "labels_pairs" : labels_pairs, "data_pairs" : data_pairs,
                                       "labels_what": labels_what, "data_what": data_what,
                                            })


def tour_list(request):
    """A view of all bands."""
    tour_list = Tour.objects.all()
    print(tour_list)
    return render(request, 'test.html', {'tour_list': tour_list})


def TourDetailView(request, slug):
    """Полное описание тура"""
    tour = Tour.objects.get(url=slug)
    print(tour)
    return render(request, "tour_detail.html", {"tour": tour})



