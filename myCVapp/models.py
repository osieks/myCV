from django.db import models

# Create your models here.

class Education(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    ordering = ['-end_date']
    
    def __str__(self):
        return self.title
    
class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    ordering = ['-end_date']
    
    def __str__(self):
        return f'{self.title}: {self.description}, {self.start_date} - {self.end_date}'
    
class Language(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    
    ordering = ['-level']
    
    def __str__(self):
        return f'{self.name} = {self.level}'

class Interest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} : {self.description}'

    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name} = {self.level}'
    
    
class Certificate(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    
    ordering = ['date']
    
    def __str__(self):
        return self.name