# from django.db import models

# Create your models here.
# from django.db import models

# class Profile(models.Model):
#     name = models.CharField(max_length=200)
#     title = models.CharField(max_length=200, default='Senior Software Engineer')
#     summary = models.TextField(blank=True)
#     phone = models.CharField(max_length=50, blank=True)
#     email = models.EmailField(blank=True)
#     location = models.CharField(max_length=200, blank=True)
#     linkedin = models.URLField(blank=True)
#     visa_status = models.CharField(max_length=200, blank=True)
#     def __str__(self):
#         return self.name

# class Skill(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name

# class Experience(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     company = models.CharField(max_length=200)
#     role = models.CharField(max_length=200)
#     start_date = models.CharField(max_length=50, blank=True)
#     end_date = models.CharField(max_length=50, blank=True)
#     description = models.TextField(blank=True)
#     def __str__(self):
#         return f"{self.role} @ {self.company}"

# class Education(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     degree = models.CharField(max_length=200)
#     institution = models.CharField(max_length=200)
#     year = models.CharField(max_length=50, blank=True)
#     def __str__(self):
#         return f"{self.degree} - {self.institution}"
