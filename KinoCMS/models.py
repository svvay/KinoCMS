from django.db import models
from django.urls import reverse
from datetime import date


class Category(models.Model):
    name = models.CharField(max_length=160)
    description = models.TextField()
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Movie(models.Model):
    title = models.CharField('Название фильма', max_length=160)
    description = models.TextField('описание')
    short_description = models.TextField('Краткое описание', blank=True, null=True, default=None)
    poster = models.ImageField('Постер', upload_to='movies/')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=100, unique=True)
    is_active = models.BooleanField(default=False)
    price_per_film = models.PositiveIntegerField(default=0, help_text='указываем цену')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class MoviShots(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField()
    image = models.ImageField(upload_to='movies_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Фильмы', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадры из фильма'
        verbose_name_plural = 'Кадры из фильмов'


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'


class Rating(models.Model):
    ip = models.CharField(max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм')

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Cinema(models.Model):
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    address = models.TextField(blank=True, null=True, default=None)
    contact_phone = models.CharField(max_length=48, blank=True, null=True, default=None)

    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name = 'Кинотеатр'
        verbose_name_plural = 'Кинотеатры'


class News(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    publication = models.PositiveIntegerField(default=2020, help_text='Публикация')
    date_info = models.DateField('Акция стартует', default=date.today)
    cinema = models.ForeignKey(Cinema, verbose_name='Кинотеатр', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
