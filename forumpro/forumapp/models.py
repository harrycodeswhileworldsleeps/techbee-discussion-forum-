from django.db import models
#parent model 
class forum(models.Model):
    name=models.CharField(default="anonymous",max_length=1000)
    title=models.CharField(max_length=1000)
    description=models.CharField(max_length=1000)
    email=models.CharField(max_length=1000,null=True)
    date_now=models.DateField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.title

#child model
class discussion(models.Model):
    forum=models.ForeignKey(forum,on_delete=models.CASCADE)
    discuss=models.CharField(max_length=1000)
    def __str__(self):
        return self.forum

