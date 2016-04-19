from django.db import models
from django.utils import timezone
# Create your models here.
#inherit Model class from Django
class Post(models.Model):
    #all fields are accessible as methods on models module from Django
    text = models.TextField()
    #we want author to represent a specific user of web app
    #use foreign key to represent another table in same database
    #each user is a row inside another table in the database
    #user has multiple properties
    #auth.User is a built-in module of Django
    author = models.ForeignKey('auth.User')
    #specify maxlength in characters so no title can be over 200 chars
    title = models.CharField(max_length=200)
    #two other class variables we want ~ created/started and published
    #use date-time fields, make sure to import timezone from django.utils
    #django looks at this object we're passing it, and can tell it's
    #a callable object. same as callback function in js
    #checks when we run - what is the time right now?
    #we're not calling this function. We're passing it as an object to
    #be executed later on as datetimefield
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
        #Since date is string and not object, we want to leave it as null
        #Define a method for when we do publish it
    def publish(self):
            #this is when we call it
        self.publish_date = timezone.now
        self.save()
        #create string dunder (double underscore)
    def __str__(self):
            #string representation of this object
        return self.title

#we've just defined in code, but we need to actually create database table that #this model represents. Go to terminal...
