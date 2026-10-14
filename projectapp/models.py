from django.db import models

class About(models.Model):
    sarlavha = models.CharField(max_length=50)
    qisqa_tavsif = models.TextField()
    fon_rasmi = models.ImageField()

class Company(models.Model):
    korxona_nomi = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    logo = models.ImageField()
    korxona_tarixi = models.CharField(max_length=255)
    tajriba = models.CharField(max_length=255)
    xizmatlar = models.CharField(max_length=255)
    mahsulotlar = models.CharField(max_length=255)
    asosiy_korsatkichlar=models.CharField(max_length=255)

class Mijozlar(models.Model):
    company = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    fikri = models.CharField(max_length=255)

class Contact(models.Model):
    email_company = models.CharField(max_length=255)
    telefon = models.CharField(max_length=50)
    manzil = models.CharField(max_length=255)
    ijtimoiy_tarmoqlar = models.CharField(max_length=255)


