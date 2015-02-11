from django.db import models

    
class Address (models.Model):
    street = models.CharField(max_length=200)
    street_additional = models.CharField(max_length=10, blank=True)
    street_number = models.PositiveIntegerField()
    postcode = models.PositiveIntegerField()
    city = models.CharField(max_length=200)
    bundesland = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

class ZeltlagerDurchgang(models.Model):
    number = models.IntegerField(primary_key=True)
    place = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()
    capacity = models.IntegerField()
    lagerleiter = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.number) + u". " + self.place

class Participant(models.Model):
    name = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    zeltlager_durchgang = models.ForeignKey(ZeltlagerDurchgang, blank=True, default=None, null=True)
    address = models.ForeignKey(Address, blank=True, default=None)
    phone_number = models.CharField(max_length=200, blank=True)
    mobile_number = models.CharField(max_length=200, blank=True)
    jugendgruppe = models.CharField(max_length=200, blank=True)
    mail = models.EmailField(max_length=254, blank=True)
    job = models.CharField(max_length=200, blank=True)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=200)
    vegetarian = models.BooleanField(default=False)
    restrictions = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    legal_guardian = models.CharField(max_length=200)
    legal_guardian_phone_number = models.CharField(max_length=200)
    legal_guardian_mobile_number = models.CharField(max_length=200)
    insurance_company = models.CharField(max_length=200)
    insurance_number = models.PositiveIntegerField()
    main_insurant = models.CharField(max_length=200)
    main_insurant_birthdate = models.DateField()
    main_insurant_address = models.CharField(max_length=200)
    main_insurant_employer = models.CharField(max_length=200)
    tetanus_immunization = models.DateField(blank=True, null=True)
    remember_me_about_medicine = models.TextField(blank=True)
    swimming_badge = models.CharField(max_length=200, blank=True)
    allow_separation_in_groups = models.BooleanField(default=False)
    additional_participants_same_household = models.CharField(max_length=200, blank=True)
    partial_participant = models.BooleanField(default=False)
    partial_start = models.DateField(blank=True, null=True)
    partial_end = models.DateField(blank=True, null=True)
    alternative_zeltlager_durchgang = models.ForeignKey(ZeltlagerDurchgang, related_name='+', blank=True, default=None, null=True)
    preferred_work = models.TextField(blank=True)
    activities_i_liked = models.TextField(blank=True)
    things_i_can_provide = models.TextField(blank=True)
    arrival_by = models.CharField(max_length=200)

    def __unicode__(self):
        return self.firstname + u" " + self.name
