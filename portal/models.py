from django.db import models

class Event(models.Model):
    CATEGORY = (
        ('fire', 'Fire'),
        ('earth', 'Earth'),
        ('water', 'Water'),
        ('storm', 'Storm'),
        ('disease', 'Disease'),
        ('industrial', 'Industrial')
    )

    SEVERITY = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    )

    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, default=None, blank=True)
    location = models.CharField(max_length=200)
    severity = models.CharField(max_length=10, choices=SEVERITY,
                                default='medium')
    category = models.CharField(max_length=10, choices=CATEGORY,
                                default='fire')

    def __str__(self):
        return "{} [{}] at {}".format(
            self.name, self.severity, self.location)


class PersonStatus(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100, null=True, default=None, blank=True)
    status = models.ForeignKey(PersonStatus, on_delete=models.SET_NULL, blank=True, null=True, related_name='status')
    id_number = models.IntegerField(null=True, default=None, blank=True, unique=True)
    dob = models.DateField(null=True, default=None, blank=True)
    mobile = models.CharField(max_length=20, null=True, default=None, blank=True)
    email = models.EmailField(null=True, default=None, blank=True)
    description = models.CharField(max_length=300)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)



