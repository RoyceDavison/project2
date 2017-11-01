from django.db import models
from PIL import Image
import uuid
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 20, help_text = "Enter your name.")
    #comment = models.ManyToManyField("Comment",help_text = "Write your comment for the post.")
    email = models.EmailField(max_length = 50,help_text = "Enter your e-mail:")
    password = models.CharField(max_length = 20, help_text = "Create a password.")
    description = models.TextField(help_text = "Please describe yourself so other can know you.", blank =True)
    time = models.DateTimeField(auto_now_add = True)

    YEAR_IN_SCHOOL_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
    )

    grade = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, default='FRESHMAN')
    major = models.CharField(max_length = 20, help_text="Please enter your major.",blank=False)

    class Meta:
        ordering = ["username"]

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])
    
    def __str__(self):
        return '%s, %s' % (self.username,self.time)

    
# Required for unique comment instances
class Comment(models.Model):
    context = models.TextField(help_text ="Write your comment.",blank = True)
    #picture = models.ImageField(upload_to = 'photo')
    video = models.URLField(blank=True)
    time = models.DateTimeField(auto_now_add = True)
    comment = models.ForeignKey('Post', null=True) 
    class Meta:
        ordering = ["time"]

    # Methods
    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return '%s, %s' % (self.context,self.time)

class Post(models.Model):
    title = models.CharField(max_length = 20, help_text ="Your post title.",blank = True)
    context = models.TextField(help_text ="What is in your mind?",blank = True)
    time = models.DateTimeField(auto_now_add = True)
    #picture = models.ImageField(upload_to = 'photo')
    video = models.URLField(blank=True)
    user = models.ForeignKey('User', null=True) 

    TYPE_OF_POST = (
        ("---","---"),
        ('clubinfo', 'ClubInfo'),
        ('courseinfo', 'CourseInfo'),
        ('lookforride', 'FreeRide'),
        ('tutor', 'TutorInfo'),
        ('rent', 'RentInfo')
    )
    grade = models.CharField(max_length=10, choices=TYPE_OF_POST, default='---')

    class Meta:
        ordering = ["time"]
    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return '%s, %s, %s' % (self.title,self.context,self.time)
