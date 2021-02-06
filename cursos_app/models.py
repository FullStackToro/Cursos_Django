from django.db import models

class Curso_admin(models.Manager):
    def validacion(self, postData):
        error = {}
        largo_data = [5, 15]

        if len(postData['nombre']) < largo_data[0]:
            error['nombre'] = f"El nombre del curso debe ser de al menos {largo_data[0]} caracteres"

        if len(postData['form_desc']) < largo_data[1]:
            error['form_desc'] = f"La descripción debe poseer al menos {largo_data[1]} caracteres"

        return error

class Description(models.Model):
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Curso(models.Model):
    name=models.CharField(max_length=255)
    desc = models.ForeignKey(Description, related_name="course", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects= Curso_admin()





















# Create your models here.
