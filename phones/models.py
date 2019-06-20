from django.db import models


class Phone(models.Model):
    CHOICE_OS = {
        ('ios','ios'),
        ('windows', 'windows'),
        ('android', 'android')
            }
    name = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)
    op_s = models.CharField(max_length=50, choices=CHOICE_OS)
    brand = models.TextField(default='-')
    ram = models.IntegerField(default=0)
    pixels = models.IntegerField(default=0)
    cam2 = models.BooleanField(default=False)

    def __str__(self):
        return 'Модель - {0}, Стоимость - {1}, Операционная система = {2}, Дополнительно = {3}'.format(self.name,
                                                                                                       self.cost,
                                                                                                       self.op_s,
                                                                                                       self.brand)

class Prod(models.Model):
    feature = models.CharField(max_length=50, blank=True, default='-')
    phone = models.ForeignKey(Phone, null=True, on_delete=models.SET_NULL, related_name='features')

    def __str__(self):
        return self.feature


