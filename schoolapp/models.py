from django.db import models
from django.utils import timezone

# Create your models here.

class Teacher_login_informa(models.Model):
    Teacher_ID = models.CharField(max_length=50)
    Teacher_Name = models.CharField(max_length=255)
    Teacher_pass = models.CharField(max_length=255)

    def __str__(self):
        return self.Teacher_ID

    @staticmethod
    def matching_loging_teacher(userID):
        try:
            return Teacher_login_informa.objects.get(Teacher_ID=userID)
        except:
            return False


class store_email_teach_new(models.Model):
    Teacher_ID = models.CharField(max_length=100)
    Teacher_email = models.CharField(max_length=30)

    def __str__(self):
        return self.Teacher_ID

    @staticmethod
    def matching_show_teacher(userID):
        try:
            return store_email_teach_new.objects.get(Teacher_ID=userID)
        except:
            return False


class Student_courses_with_Teacher_name(models.Model):
    course = models.CharField(max_length=200)
    Teacher_ID = models.ForeignKey(Teacher_login_informa, on_delete=models.CASCADE)

    def __str__(self):
        return self.course


class Student_login_informatn(models.Model):
    Student_ID = models.CharField(max_length=50)
    Student_Name = models.CharField(max_length=255)
    course = models.ForeignKey(Student_courses_with_Teacher_name, on_delete=models.CASCADE)
    Student_pass = models.CharField(max_length=255)

    def __str__(self):
        return self.Student_ID

    @staticmethod
    def matching_loging_stu(userID):
        try:
            return Student_login_informatn.objects.get(Student_ID=userID)
        except:
            return False


class store_email_stu_new(models.Model):
    Student_ID = models.CharField(max_length=100)
    Student_email = models.CharField(max_length=30)

    def __str__(self):
        return self.Student_ID

    @staticmethod
    def matching_show_stu(userID):
        try:
            return store_email_stu_new.objects.get(Student_ID=userID)
        except:
            return False


class Teacher_Assignment_upload_File(models.Model):
    Assignment_name = models.CharField(max_length=500)
    course = models.CharField(max_length=500)
    date = models.DateField(default=timezone.now, blank=True)
    due_date = models.DateField(default=timezone.now, blank=True)
    title = models.CharField(max_length=500)
    Details = models.TextField(max_length=500)
    attachment = models.CharField(max_length=1000)
    resource = models.CharField(max_length=500)
    posts = models.CharField(max_length=500)
    Out_Of_Grade = models.CharField(max_length=500)

    def __str__(self):
        return self.Assignment_name


class Student_Submit_Assignment_pro(models.Model):
    attachment = models.CharField(max_length=1000)
    course = models.CharField(max_length=1000)
    Student_ID = models.CharField(max_length=1000)
    Assignment_name = models.CharField(max_length=1000)


class Grade_Student(models.Model):
    Student_ID = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    Assignment_name = models.CharField(max_length=200)
    Grade = models.CharField(max_length=200)
    Out_Of_Grade = models.CharField(max_length=200)

    def __str__(self):
        return self.Student_ID


class Assignment_Comments(models.Model):
    serial_no = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    postID = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    time_comment = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.comment[0:12] + ".... " + " by " + self.user




class Employee(models.Model):
    EMPLOYEE_TYPES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
    )

    EMPLOYEE_STATUSES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    employee_id = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    hire_date = models.DateField()
    employee_type = models.CharField(max_length=20, choices=EMPLOYEE_TYPES, default='full_time')
    status = models.CharField(max_length=20, choices=EMPLOYEE_STATUSES, default='active')
    roles = models.ManyToManyField('Role', through='EmployeeRole')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.employee_id}"

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class EmployeeRole(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee} - {self.role}"
