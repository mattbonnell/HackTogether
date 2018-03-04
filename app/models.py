from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, default=datetime.today())
    modified_date = models.DateTimeField(auto_now=True, default=datetime.today())

    class Meta:
        abstract = True


class Skill(BaseModel):
    name = models.CharField(max_length=200)
    experience_level = models.CharField(max_length=200)
    years_of_experience = models.IntegerField(max_length=200)

    def __str__(self):
        return self.name


class Interest(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    word = models.CharField(max_length=35)
    slug = models.CharField(max_length=250)

    def __str__(self):
        return self.word


class UserProfile(BaseModel):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=200, default='John')
    last_name = models.CharField(max_length=200, default='Doe')
    age = models.IntegerField(max_length=200, default=99)
    skills = models.ManyToManyField(Skill, null=True)
    interests = models.ManyToManyField(Interest, null=True)


    def __str__(self):
        return self.user.username


class Role(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Domain(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    owner = models.ForeignKey(User, related_name='projects_owned')
    team = models.ManyToManyField(User, related_name='projects_involved_in')
    completion_deadline = models.DateField(null=True, blank=True)
    talentNeeded = models.ManyToManyField(Role)
    domains = models.ManyToManyField(Domain)
    beginners_welcome = models.BooleanField(default=True)
    complexity = models.CharField(max_length=200)
    estimated_duration = models.IntegerField(max_length=200)
    github_link = models.CharField(max_length=200, default='')
    tags = models.ManyToManyField(Tag, related_name='projects')

    def __str__(self):
        return self.name