from django.db import models
from django.core.validators  import RegexValidator,MinValueValidator

class Counter(models.Model):
    name = models.CharField(max_length=20,primary_key=True,unique=True)
    count = models.IntegerField(validators=[MinValueValidator(0)],default=0,blank=True)
    
    def nextCounter(name):
        try:
            r = Counter.objects.get(name=name)
        except:
            r = Counter.objects.create(name=name,count=0)
        
        r.count = r.count + 1
        r.save()
        return r.count
    
    def getObject(name):
        try:
            r = Counter.objects.get(name=name)
        except:
            r = Counter.objects.create(name=name,count=0)

        r.save()
        return r.count