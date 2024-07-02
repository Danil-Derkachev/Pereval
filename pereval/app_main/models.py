from django.db import models


class User(models.Model):
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(verbose_name='Номер телефона', max_length=11)
    surname = models.CharField(verbose_name='Фамилия', max_length=256)
    name = models.CharField(verbose_name='Имя', max_length=256)
    patronym = models.CharField(verbose_name='Отчество', max_length=256)

    def __str__(self):
        return f'{self.pk} {self.surname} {self.name} {self.patronym}'


class Coords(models.Model):
    latitude = models.FloatField(verbose_name='Широта', max_length=256)
    longitude = models.FloatField(verbose_name='Долгота', max_length=256)
    height = models.IntegerField(verbose_name='Высота над уровнем моря')

    def __str__(self):
        return f'latitude:{self.latitude} longitude:{self.longitude} height:{self.height}'


class Pereval(models.Model):
    NEW, PENDING, ACCEPTED, REJECTED = 'NE', 'PE', 'AC', 'RE'
    STATUS_CHOICES = [
        (NEW, 'new'),
        (PENDING, 'pending'),
        (ACCEPTED, 'accepted'),
        (REJECTED, 'rejected')
    ]
    status = models.CharField(verbose_name='Статус', max_length=2, choices=STATUS_CHOICES, default=NEW)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)
    beauty_title = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    other_titles = models.CharField(max_length=256)
    connect = models.TextField(blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    level_spring = models.CharField(verbose_name='Уровень сложности весной', max_length=5, blank=True)
    level_summer = models.CharField(verbose_name='Уровень сложности летом', max_length=5, blank=True)
    level_autumn = models.CharField(verbose_name='Уровень сложности осенью', max_length=5, blank=True)
    level_winter = models.CharField(verbose_name='Уровень сложности зимой', max_length=5, blank=True)

    def __str__(self):
        return f'{self.pk} {self.beauty_title} {self.title}'


class Image(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images')
    image = models.BinaryField(blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(verbose_name='Уточнение к фотографии', max_length=256, blank=True)
