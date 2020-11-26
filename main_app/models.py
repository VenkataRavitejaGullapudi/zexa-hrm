from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=150)
    total_employees = models.IntegerField(default=0)
    def __str__(self):
        return self.name
class Role(models.Model):
    role = models.CharField(max_length=200)
    def __str__(self):
        return self.role

class Employee(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    GENDER_CHOICES = (
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE"),
        ("OTHER", "OTHER")
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,default='MALE')
    title = models.ForeignKey(Role,on_delete=models.SET_NULL, verbose_name='Position', null=True)
    salary = models.FloatField()
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True)
    # department = models.CharField(max_length=150)
    EMPLOYEE_STATUSES=(
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("retired", "Retired"),
        ("fired", "Fired")
    )
    status = models.CharField(max_length=15, choices=EMPLOYEE_STATUSES,default='active')
    reports_to = models.ForeignKey("self",on_delete=models.SET_NULL, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,editable=False)
    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()
        dept = Department.objects.get(id=self.department.id)
        dept.total_employees+=1
        dept.save()
    def delete(self, using=None, keep_parents=False):
        dept = Department.objects.get(id=self.department.id)
        dept.total_employees -= 1
        dept.save()
        super().delete()


class Department_Manager(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    manager = models.ForeignKey(Employee,on_delete=models.CASCADE)
    assigned_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.department.name


class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    payment_amount = models.FloatField()
    timestamp_of_payment = models.DateTimeField(default=timezone.now)
    recorded_by = models.ForeignKey(User, on_delete=models.CASCADE,editable=False)

    def __str__(self):
        return str(self.employee.id)

