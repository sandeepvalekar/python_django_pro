from django.db import models


class client(models.Model):
  id=models.AutoField(primary_key=True)
  client_name=models.CharField(max_length=50)
  created_at=models.DateTimeField(auto_now=True)
  created_by=models.CharField(max_length=50)

  #project model
  
def __str__(self):
        return self.name 

class project(models.Model):
    project_name=models.CharField(max_length=50)
   

    client=models.ForeignKey(client,on_delete=models.CASCADE)