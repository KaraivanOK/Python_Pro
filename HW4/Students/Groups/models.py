from django.db import models


class Group(models.Model):
    academic_subject = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    count_students = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.academic_subject} {self.first_name} {self.last_name} ' \
               f'{self.count_students} '
