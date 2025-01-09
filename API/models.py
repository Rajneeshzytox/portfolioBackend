from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
 

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    source = models.URLField(blank=True, null=True)
    demo = models.URLField(blank=True, null=True)
    site = models.URLField(blank=True, null=True)

    categories = models.ManyToManyField(Category, blank=True, null=True, related_name="projects")
    tags = models.ManyToManyField(Tag, blank=True, null=True, related_name="projects")
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f"{self.id} {self.title}"