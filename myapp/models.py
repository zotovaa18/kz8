from datetime import date

from django.db import models
from django.contrib.postgres.fields import ArrayField
from multiselectfield import MultiSelectField
from django.urls import reverse


# Create your models here.

class Preferences(models.Model):
    review = models.CharField(max_length=1000)


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


class Tinder(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)

    type = models.CharField(max_length=200, choices=(('active', 'Активный'), ('culture', 'Культурно-познавательный'),
                                                     ('health', 'Оздоровительный'),
                                                     ('beach', 'Пляжный'),))
    prefered_activities = MultiSelectField(choices=activities)
    person_details = MultiSelectField(choices=person)

    about_me = models.CharField(max_length=300)
    about_second = models.CharField(max_length=300)


class Type(models.Model):
    """Тип тура"""
    name = models.CharField("Название тура", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Tour(models.Model):
    """Тур"""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="tours/")
    place = models.CharField("Место", max_length=30)
    type_active = models.ManyToManyField(Type, verbose_name="типы")
    date_start = models.DateField("Дата выезда", default=date.today)
    date_finish = models.DateField("Дата окончания", default=date.today)
    price = models.PositiveIntegerField("Стоимость", default=0)
    list_of_things = ArrayField(models.CharField(max_length=200), blank=True)
    complexity = models.CharField("Сложность", max_length=200, choices=(('basic', 'Базовый'),
                                                                        ('average', 'Средний'),
                                                                        ('advanced', 'Продвинутый'),
                                                                        ('hard', 'Сложный'),
                                                                        )
                                  )
    type_of_item = models.CharField("Тип выбора", max_length=200, choices=(('tours', 'Туры'),
                                                                           ('directions', 'Направления'),
                                                                           ('excursions', 'Экскурсии'),
                                                                           ('museums', 'Музеи'),
                                                                           )
                                    )
    comfort = models.CharField("Комфорт", max_length=200, choices=(('basic', 'Базовый'),
                                                                   ('simple', 'Простой'),
                                                                   ('average', 'Средний'),
                                                                   ('above_average', 'Выше среднего'),
                                                                   ('high', 'Высокий'),
                                                                   )
                               )
    people_in_group = models.PositiveIntegerField("Максимальное количество людей в группе", default=1)
    age = models.PositiveIntegerField("Минимальный возраст", default=10)
    url = models.SlugField(max_length=130, unique=True, null=True)

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"


class TourShots(models.Model):
    """Кадры из тура"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="tour_shots/")
    movie = models.ForeignKey(Tour, verbose_name="Тур", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из тура"
        verbose_name_plural = "Кадры из тура"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    #self - будет сслыкаться на запись в этой же таблице
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Tour, verbose_name="тур", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"