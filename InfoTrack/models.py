from django.db import models
from PIL import Image
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
        """
        The final method, get_absolute_url() returns a URL that can be used to access a detail record for this model 
        (for this to work we will have to define a URL mapping that has the name book-detail, 
        and define an associated view and template).   
        """
        return reverse('user-detail', args=[str(self.id)])
    
    def __str__(self):
        return '%s, %s' % (self.username,self.time)

   """
    def display_post(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ post.title for post in self.post.all()[:5] ])
    display_genre.short_description = 'Post'
    """

import uuid # Required for unique comment instances
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
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return '%s, %s' % (self.context,self.time)

class Post(models.Model):
    title = models.CharField(help_text ="Your post title.",blank = True)
    context = models.TextField(help_text ="What is in your mind?",blank = True)
    time = models.DateTimeField(auto_now_add = True)
    #picture = models.ImageField(upload_to = 'photo')
    video = models.URLField(blank=True)
    user = models.ForeignKey('User', null=True) 

     TYPE_OF_POST = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
    )

    grade = models.CharField(max_length=2, choices=TYPE_OF_POST, default='FRESHMAN')
    class Meta:
        ordering = ["time"]
    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return '%s, %s, %s' % (self.title,self.context,self.time)
