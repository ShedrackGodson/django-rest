from django.db import models

class Users(models.Model):
    employee_id = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    ranking = models.FloatField()

    def upload_photo(self, photoname):
        path = "hrm/photo/{}".format(photoname)
        return path
    
    image = models.ImageField(upload_to=upload_photo)

    def upload_file(self, filename):
        path = "hrm/file/{}".format(filename)
        return path
    
    resume = models.FileField(upload_to=upload_file,null=True,blank=True)

    def __str__(self):
        return f'{self.employee_id}-{self.name}'
    