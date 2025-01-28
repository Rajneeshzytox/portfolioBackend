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

    categories = models.ManyToManyField(Category, blank=True, related_name="projects")
    tags = models.ManyToManyField(Tag, blank=True, related_name="projects")
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, blank=True, null=True, related_name="projects")


    def __str__(self):
        return f"{self.id} {self.title}"


class SocialLink(models.Model):
    title = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="social_icons/", null=True, blank=True)
    url = models.URLField()

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    icon = models.ImageField(upload_to="experience_icons/", null=True, blank=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    icon = models.ImageField(upload_to="education_icons/", null=True, blank=True)

    def __str__(self):
        return self.title

class AwardAndHonor(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    icon = models.ImageField(upload_to="award_icons/", null=True, blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="skill_icons/", null=True, blank=True)

    def __str__(self):
        return self.title

class Resume(models.Model):
    url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}"

class ResumeData(models.Model):
    img = models.ImageField(upload_to="profile_pics/")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField()
    about = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    
    social_links = models.ManyToManyField(SocialLink)
    experiences = models.ManyToManyField(Experience)
    education = models.ManyToManyField(Education)
    awards_and_honors = models.ManyToManyField(AwardAndHonor)
    skills = models.ManyToManyField(Skill)
    resumes = models.ManyToManyField(Resume)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"