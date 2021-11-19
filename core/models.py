from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"Person - {self.first_name} {self.last_name}"


class ToDo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(Person, default=1, on_delete=models.CASCADE, related_name='created_todos',
                                verbose_name=_('creator'))
    maker = models.ForeignKey(Person, default=1, on_delete=models.CASCADE, related_name='made_todos',
                              verbose_name=_('maker'))

    def __str__(self) -> str:
        return f"ToDo - name:{self.name} from:{self.creator} for:{self.maker}"



