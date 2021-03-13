from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()

class TestReport(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    patientName=models.CharField(max_length=100)
    raterName=models.CharField(max_length=100)
    date_created=models.DateField(max_length=100,default='2020-12-12')
    grasp_score=models.IntegerField(null=True) 
    grip_score=models.IntegerField(null=True) 
    pinch_score=models.IntegerField(null=True) 
    gross_score=models.IntegerField(null=True) 

    