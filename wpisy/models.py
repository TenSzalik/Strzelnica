from django.db import models
from django.utils import timezone
from django.db.models import Max

class Wpis(models.Model):
    ZAWODNICY = (
        ('Gracjan', 'Gracjan'),
        ('Konrad', 'Konrad'),
        ('Bestia', 'Bestia'),
        ('Hampyl', 'Hampyl'),
    )

    strzelec = models.CharField(max_length=15, choices=ZAWODNICY)
    punkty = models.IntegerField(default = 10)
    oddane_strzaly = models.IntegerField()
    dystans = models.IntegerField(default = 10)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)

    def wynik(self):
        x = self.punkty * self.dystans / self.oddane_strzaly
        return round(x, 2)
        

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #def __str__(self):
    #    return self.title
    #Przez to są problemy z id, jakbyś zamienił title na np. dystans, to by działało :)


#https://docs.djangoproject.com/en/2.2/topics/db/models/
#https://www.youtube.com/watch?v=gzzC9YVw3q4&list=PLTzyz9rD2A3taEZybRceWYXKceTevc2zT&index=6