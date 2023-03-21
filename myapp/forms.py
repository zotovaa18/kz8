from django.forms import ModelForm
from .models import Preferences, Tinder
from django import forms

activities = (
('sea_activities', 'Загорать и купаться'),
('walking', 'Гулять по городу'),
('for_oldies', 'Посетить санаторий/спа'),
('mountains', 'Подняться в горы'),
('for_masha', 'Сходить в поход'),
('museums', 'Посещать музеи и достопримечательности'),
('sex', 'Развлекаться')
)
person = (('smart', 'Умный'),
('funny', 'Веселый'),
('versatile', 'Разносторонний'),
('talkative', 'Общительный'),
('brave', 'Смелый')
)


class PrefFrom(ModelForm):
    class Meta:
        model = Preferences
        fields = '__all__'


class TinderForm(forms.Form):
    name = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=11)

    type = forms.ChoiceField( choices=(('active', 'Активный'), ('culture', 'Культурно-познавательный'),
                                                     ('health', 'Оздоровительный'),
                                                     ('beach', 'Пляжный'),))

    prefered_activities = forms.MultipleChoiceField(choices=activities, widget=forms.CheckboxSelectMultiple())
    person_details = forms.MultipleChoiceField(choices=person, widget=forms.CheckboxSelectMultiple())

    about_me = forms.CharField(max_length=300)
    about_second = forms.CharField(max_length=300)