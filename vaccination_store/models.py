from django.db import models


class Vaccination(models.Model):
    VACCINE_TYPES = [
        ('BCG', 'تطعيم المواليد - بي سي جي'),
        ('Polio_Newborn', 'تطعيم المواليد - شلل الأطفال'),
        ('Hexavalent_2Months', 'تطعيم الشهرين - الطعم السداسي'),
        ('Rotavirus_2Months', 'تطعيم الشهرين - طعم الروتا'),
        ('Hexavalent_4Months', 'تطعيم الأربعة شهور - الطعم السداسي'),
        ('Rotavirus_4Months', 'تطعيم الأربعة شهور - طعم الروتا'),
        ('Hexavalent_6Months', 'تطعيم الستة شهور - الطعم السداسي'),
        ('Rotavirus_6Months', 'تطعيم الستة شهور - طعم الروتا'),
        ('Meningococcal_9Months', 'تطعيم التسعة شهور - تطعيمة التهاب السحايا A.C.Y.W135'),
        ('Polio_9Months', 'تطعيم التسعة شهور - ال'),
        ('Pneumococcal_1Year', 'تطعيم السنة - طعتطعيمة الوقاية من شلل الأطفم الرئوي 13'),
        ('Pentavalent_1.5Years', 'تطعيم السنة والنصف - الطعم الخماسي'),
    ]

    name = models.CharField(max_length=255, verbose_name='اسم التطعيم')
    vaccine_type = models.CharField(max_length=50, choices=VACCINE_TYPES, verbose_name='نوع التطعيم')
    expired_date = models.DateField(verbose_name='تاريخ انتهاء الصلاحية')
    description = models.TextField(verbose_name='وصف التطعيم')
    available_doses = models.IntegerField(verbose_name='عدد الجرعات المتاحة')

    def __str__(self):
        return f"{self.name} - {self.vaccine_type}"



class JobPlace(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=50)
    location = models.URLField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name 

    