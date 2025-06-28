from django.db import models

# Create your models here.
class StaffBase(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
        
class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} (Manager)"
    
class intern(StaffBase):
    mentor = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, related_name='interns')
    internship_end = models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} (intern)"
    
    
    
