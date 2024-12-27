from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=70)
    description=models.TextField(blank=True)
    is_completed=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Capitalize the name before saving
        self.description=self.description.capitalize()
        super(Task, self).save(*args, **kwargs) 

    def __str__(self):
        return self.title
    
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to="profile_pics/",default="D:\Shriya_Coding\Django_work\ToDo_Project\media\profile_pics\Default.jpg",blank=True,null=True)
    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        # Check if an instance already exists
        try:
            old_instance = UserProfile.objects.get(pk=self.pk)
            if old_instance.profile_pic != self.profile_pic:
                # Delete the old file
                old_instance.profile_pic.delete(save=False)
        except UserProfile.DoesNotExist:
            pass  # No old instance to worry about

        # Save the new instance
        super().save(*args, **kwargs)



