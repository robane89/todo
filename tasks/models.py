from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
   
    def update_task(self, title, description, completed):
        self.title = title
        self.description = description
        self.completed = completed
        self.save()
    class Meta:
        app_label = 'tasks'

    def __str__(self):
        return self.title
