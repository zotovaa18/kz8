from django.urls import path
from . import views

urlpatterns = [
    path('preference', views.index, name="index"),
    path('tinder', views.tindef_from, name="tindef_from"),
    path('review/<int:review_id>', views.review_by_id, name = 'review_by_id'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('', views.main_page, name="main_page")

]