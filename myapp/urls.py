from django.urls import path
from . import views

urlpatterns = [
    path('preference', views.index, name="index"),
    path('tinder', views.tindef_from, name="tindef_from"),
    path('review/<int:review_id>', views.review_by_id, name='review_by_id'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('map', views.map, name="map"),
    path('insurance', views.insurance, name="insurance"),
    path('tours', views.tours, name="tours"),
    path('routes_excursions', views.routes_excursions, name="routes_excursions"),
    path('tinder_review', views.tinder_review, name="tinder_review"),
    path('contact_us', views.contactus_form, name="contact_us"),
    path('popular_derictions', views.popular_destinations, name="popular_derictions"),
    path('', views.main_page, name="main_page"),
    path('<slug:slug>', views.TourDetailView, name="tour_detail"),

]