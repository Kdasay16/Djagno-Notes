from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notes")
 # The first item is the model we want to create a link with. In this case, this is the User model.
 # Then, the second item is going to be the on_delete- what happens to this note if the user associated with it is deleted.
 # models.CASCADE- if a user gets deleted, we also want to delete all the notes associated with them.
 # Finally, we can say how we will identify this relationship on the user side. Related_name is going to be notes.
