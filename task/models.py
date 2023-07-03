from django.contrib.auth.models import User
from django.db import models
from django.db.models.functions import Now


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True, max_length=35)
    due_date = models.DateTimeField()
    created_on = models.DateTimeField(editable=True, auto_now_add=True)

    # on_delete set to delete the data belonging to the corresponding user when user is deleted
    created_by = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    is_completed = models.BooleanField(help_text="If task is completed or past due, Please check this box.", default=False)

    # constraint added to have due_date greater than current date

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(due_date__gte=Now()),
                name='due date cannot be past date.'
            )
        ]

    def __str__(self):
        return self.name
