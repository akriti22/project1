from django.db import models

# Create your models here.


class Employee(models.Model):
    e_no = models.IntegerField()
    e_name = models.CharField(max_length=64)
    e_sal = models.FloatField()
    e_addr = models.CharField(max_length=64)

    def __str__(self):
        return self.e_name


class Manager(models.Model):
    m_no = models.IntegerField()
    m_name = models.CharField(max_length=65)
    m_sal = models.FloatField()
