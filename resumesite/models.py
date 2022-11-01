from django.db import models
class Post(models.Model):
    name=models.CharField(max_length=200)#
    email=models.EmailField()
    field=models.CharField(max_length=200)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    skills_1=models.CharField(max_length=200)
    skills_2=models.CharField(max_length=200)
    skills_3=models.CharField(max_length=200)
    skills_4=models.CharField(max_length=200)

    experience_1_title=models.CharField(max_length=200)
    experience_1_dur=models.CharField(max_length=200)
    experience_1_desc=models.CharField(max_length=200)

    experience_2_title=models.CharField(max_length=200)
    experience_2_dur=models.CharField(max_length=200)
    experience_2_desc=models.CharField(max_length=200)

    education_1=models.CharField(max_length=200)
    education_1_dur=models.CharField(max_length=200)
    education1_score=models.CharField(max_length=200)

    education_2=models.CharField(max_length=200)
    education_2_dur=models.CharField(max_length=200)
    education2_score=models.CharField(max_length=200)
