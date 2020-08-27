from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    content_presentation = models.CharField(max_length=100, default='SOME STRING')
    creation_date = models.DateField()
    creator = models.CharField(max_length=42)
    description = models.TextField(null=True)
    photo = models.ImageField(upload_to="galery", default='')

    class Meta:
        verbose_name = "Compagnies"

    def __str__(self):

        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100,unique=True)
    content_presentation = models.CharField(max_length=100, default='SOME STRING')
    description = models.TextField(null=True)
    photo = models.ImageField(upload_to="galery", default='')
    company = models.ForeignKey(Company, on_delete=models.CASCADE) 

    class Meta:
        verbose_name = "Products"

    def __str__(self):

        return self.name


  

      





# class Article(models.Model):
#     titre = models.CharField(max_length=30)
#     fabricant = models.ForeignKey('Fabricant', on_delete=models.CASCADE)
#     class Meta:
#             verbose_name = "article"
#     def __str__(self):

#         return self.titre
# <!-- Department.objects.get(password = password, department_name = department_name) -->
# nt = Article(titre = "crafty+", fabricant = Fabricant_id.objects.get(nom=Storkz))
