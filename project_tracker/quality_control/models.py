from django.db import models
from tasks.models import Project, Task

class BugReport(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    PRIORITY_CHOICES = [
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='reports', 
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='reports',
        on_delete=models.SET_NULL,
        null=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New'
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('Review'   , 'Рассмотрение'),
        ('Accepted' , 'Принято'),
        ('Declined' , 'Отклонено'),
    ]
    PRIORITY_CHOICES = [
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='features',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='features',
        on_delete=models.SET_NULL,
        null=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Review'
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title