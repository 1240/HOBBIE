from django.db import models

# Create your models here.


class Regions(models.Model):
    class Meta():
        db_table = 'regions'

    region_name = models.CharField(max_length=100, verbose_name="Название области")
    region_id = models.CharField(max_length=100, verbose_name="ИД региона")
    region_title = models.CharField(max_length=100, verbose_name="Заголовок")
    region_url = models.CharField(max_length=100, verbose_name="Ссылка")
    is_west = models.BooleanField(verbose_name="Западная часть?")


class Cities(models.Model):
    class Meta():
        db_table = 'cities'

    city_name = models.CharField(max_length=100, verbose_name="Название города")
    city_id = models.CharField(max_length=100, verbose_name="ИД города")
    city_title = models.CharField(max_length=100, verbose_name="Заголовок")
    city_url = models.CharField(max_length=100, verbose_name="Ссылка")
    city_region = models.ForeignKey(Regions)