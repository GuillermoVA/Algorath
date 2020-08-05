from django.db import models

# Create your models here.


class User (models.Model):
    name = models.CharField(
        'Name', 
        max_length=80,
        unique=True
    )
    class Meta: 
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name




class Connection (models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='_user1')    
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='_user2')    

    class Meta: 
        verbose_name = "Connection"
        verbose_name_plural = "Connections"

    def __str__(self):
        return self.user1.name + ' -- ' + self.user2.name
