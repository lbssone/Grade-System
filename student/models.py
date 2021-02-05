from django.db import models
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from student.Exceptions import GradeExistedError, GradeNotFoundError

def validatePhone(value):
    if not value.isnumeric():
        raise ValidationError("Phone should be numeric.")
    elif len(value) != 10:
        raise ValidationError("Phone should be exactly 10 digits.")
    elif not value.startswith("09"):
        raise ValidationError("Phone should start with '09'")

def validateGrade(value):
    if not 0 <= value <= 100:
        raise ValidationError("Grade should be between 0 and 100.")    
    
class Student(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    phone = models.CharField(unique=True, max_length=20, validators=[validatePhone])

    def __str__(self):
        return self.fullName

    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"

    def save(self):
        self.firstName = self.firstName.capitalize()
        self.lastName = self.lastName.capitalize()
        super().save()

    def get_absolute_url(self):
        return reverse("student:detail", kwargs={"pk": self.pk})

    def getGrades(self):
        grades = Grade.objects.filter(student__id=self.pk)
        return grades

    def addGrade(self, testNo, chinese, english, math):
        obj, created = Grade.objects.get_or_create(testNo=testNo, student=self, defaults={"chinese": chinese, "english": english, "math": math})
        if not created:
            # TODO: fix validation
            raise GradeExistedError()
        return obj, created

    # def deleteGrade(self, testNo):
    #     grade = Grade.objects.get(Q(student=self) & Q(testNo=testNo))
    #     if grade:
    #         grade.delete()
    #     else:
    #         raise GradeNotFoundError
    #     return grade

class Grade(models.Model):
    testNo = models.PositiveIntegerField(blank=True)
    chinese = models.DecimalField(max_digits=5, decimal_places=2, validators=[validateGrade])
    english = models.DecimalField(max_digits=5, decimal_places=2, validators=[validateGrade])
    math = models.DecimalField(max_digits=5, decimal_places=2, validators=[validateGrade])
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.student}: #{self.testNo}"

    @property
    def total(self):
        return self.chinese + self.english + self.math
    
    @property
    def average(self):
        return round(self.total / 3, 2)

    @property
    def allSubjects(self):
        return [self.chinese, self.english, self.math]

    def get_absolute_url(self):
        return reverse("student:detail", kwargs={"pk": self.student.pk})

