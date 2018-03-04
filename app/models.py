from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Language(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tool(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    word = models.CharField(max_length=35)
    slug = models.CharField(max_length=250)

    def __str__(self):
        return self.word


class Domain(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Speciality(BaseModel):
    name = models.CharField(max_length=200)
    is_developer_speciality = models.BooleanField(default=False)
    is_designer_speciality = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_developer = models.BooleanField(default=False)
    is_designer = models.BooleanField(default=False)
    age = models.IntegerField()
    specialties = models.ManyToManyField(Speciality)
    interested_in_domains = models.ManyToManyField(Domain, blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    tools = models.ManyToManyField(Tool, blank=True)

    def __str__(self):
        return self.user.username

class Project(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=10000)
    owner = models.ForeignKey(User, related_name='projects_owned', on_delete=models.CASCADE)
    team = models.ManyToManyField(User, related_name='projects_involved_in')
    completion_deadline = models.DateField(null=True, blank=True)
    are_members_needed = models.BooleanField(default=True)
    specialities_needed = models.ManyToManyField(Speciality)
    designer_needed = models.BooleanField(default=True)
    developer_needed = models.BooleanField(default=True)
    domains = models.ManyToManyField(Domain)
    beginners_welcome = models.BooleanField(default=True)
    complexity = models.CharField(max_length=200)
    estimated_duration = models.IntegerField()
    github_link = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='projects', blank=True)

    def __str__(self):
        return self.name
