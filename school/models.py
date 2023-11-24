from django.db import models
import uuid

# Create your models here.


class Department(models.Model):
    department_id = models.UUIDField(default=uuid.uuid4, editable=False)
    department_name = models.CharField(max_length=100)
    role = models.TextField()
    head_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class Subject(models.Model):
    subject_id = models.UUIDField(default=uuid.uuid4, editable=False)
    subject_name = models.CharField(max_length=100)
    subject_description = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name


class Tutor(models.Model):
    tutor_id = models.UUIDField(default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100)
    subjects = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    STATUS = (
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    )
    status = models.CharField(max_length=100, choices=STATUS)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.full_name
    
class Employees(models.Model):
    employee_id = models.UUIDField(default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100)
    STATUS = (
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    )
    status = models.CharField(max_length=100, choices=STATUS)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.full_name


class ClassRoom(models.Model):
    class_id = models.UUIDField(default=uuid.uuid4, editable=False)
    class_name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Tutor, on_delete=models.DO_NOTHING)
    grade = models.CharField(max_length=100)
    Capacity = models.IntegerField()
    STATUS = (
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    )
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.class_name


class Students(models.Model):
    student_id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.DO_NOTHING)
    parent_name = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=100)
    parent_email = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ClassAttendance(models.Model):
    attendance_id = models.UUIDField(default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.DO_NOTHING)
    date = models.DateField()
    STATUS = (
        ("Present", "Present"),
        ("Absent", "Absent"),
    )
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.status


class SchoolAttendance(models.Model):
    attendance_id = models.UUIDField(default=uuid.uuid4, editable=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date = models.DateField()
    time_of_arrival = models.DateTimeField()
    STATUS = (
        ("Present", "Present"),
        ("Absent", "Absent"),
    )
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.status




class Curriculum(models.Model):
    curriculum_id = models.UUIDField(default=uuid.uuid4, editable=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    curriculum_name = models.CharField(max_length=100)
    curriculum_description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.curriculum_name


class TimeTable(models.Model):
    timetable_id = models.UUIDField(default=uuid.uuid4, editable=False)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.class_room} - {self.subject}"
    

class StudentFee(models.Model):
    fee_id = models.UUIDField(default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.amount}"
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(amount__gte=0), name="fees_amount_gte_0"
            )
        ]


class SalaryPayment(models.Model):
    payment_id = models.UUIDField(default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.BooleanField(default=False)
    date_paid = models.DateField()

    def __str__(self):
        return f"{self.employee.full_name} - {self.amount}"
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(amount__gte=0), name="salary_amount_gte_0"
            )
        ]
  
class SchoolExpense(models.Model):
    expense_id = models.UUIDField(default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    isAuthorised = models.BooleanField(default=False)
    auth_by = models.CharField(max_length=100, default="", blank=True, null=True)


    def __str__(self):
        return f"{self.description} - {self.amount}"
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(amount__gte=0), name="expense_amount_gte_0"
            )
        ]