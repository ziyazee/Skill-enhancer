from django.db import models


class clasyear(models.Model):
    choice=[('2nd-year','2'),('3rd-year','3'),('4th-year','4')]
    year=models.CharField(choices=choice,max_length=100)
    name=models.CharField(max_length=30,unique=True)
    description=models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.name

 
class filest(models.Model):
    fname=models.FileField()
    def get_absolute_url(self):
        return reverse('files:detail',kwargs={'pk':self.pk})
    fdescription=models.CharField(max_length=50,blank=True)
    usn=models.CharField(max_length=50)

    categorie = models.ForeignKey(clasyear,to_field='name',
    on_delete=models.CASCADE,
    )     
   
# class files(models.Model):
#     filename=models.FileField()  
#     def get_absolute_url(self):
#         return reverse('files:detail',kwargs={'pk':self.pk})  
#     fdescription=models.CharField(max_length=50,blank=True)
#     categorie = models.CharField(max_length=50,blank=True)
       
# class classyear(models.Model):
#     year=models.CharField(max_length=5)
# class subjects(models.Model):
#     choice=[('1','Second year'),('2','Thrird year'),('3','Fourth year')]
#     year=models.CharField(choices=choice,max_length=1)
#     name=models.CharField(max_length=20)
#     description=models.CharField(max_length=50,blank=True)


# class livings(models.Model):
#     type=[('a','animals'),('b','birds')]
#     types=models.CharField(choices=type,max_length=1,blank=True)
#     name=models.CharField(max_length=20)
#     age=models.IntegerField()
#     legs=models.IntegerField()

# class Myinfo(models.Model):
#     SEX=[('f','female'),('m','male')]
#     name=models.CharField(max_length=100)
#     age= models.CharField(max_length=100)
#     gender= models.CharField(choices=SEX,max_length=1,blank=True)
#     submission=models.DateField()
#     myjob=models.ManyToManyField('Myjob',blank=True)
# class title(models.Model):
#     job=models.CharField(max_length=50)
#     exp=models.IntegerField() 
# class child(models.Model):
#     age=models.IntegerField()
#     name=models.CharField(max_length=20)    
# class Myjob(models.Model):
#     name=models.CharField(max_length=50)    
    
#     def __str__(self):
#         return self.name

 