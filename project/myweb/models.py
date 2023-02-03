from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    academic_year = models.CharField(max_length=100)
    admission_date = models.DateField()
    admission_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    course_choice = (
        ("BITAM", "bitam"),
        ("BAGES", "bages"),
        ("BSC", "bcs"),
    )
    course = models.CharField(choices=course_choice,max_length=25)
    fathers_name = models.CharField(max_length=100)
    fathers_number = models.IntegerField(unique=True)
    mothers_name = models.CharField(max_length=100)
    mothers_number = models.IntegerField()

    class Meta:
        unique_together = ["admission_id", "course"]

    def __str__(self):
        return self.name
