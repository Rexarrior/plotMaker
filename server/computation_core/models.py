from django.db import models
from django.contrib.postgres.fields import JSONField


class Expression(models.Model):
    READY = "RE"
    FAILED = "FA"
    COMPUTING = "CO"
    STATUS_CHOICES = [(READY, 'Ready'),
                      (FAILED, 'Failed'),
                      (COMPUTING, 'Computing'),
                      ]
    text = models.CharField(max_length=150)
    status = models.CharField(max_length=2,
                              choices=STATUS_CHOICES,
                              default=COMPUTING)
    name = models.CharField(max_length=150)
    user_id = models.IntegerField()


class Variable(models.Model):
    expr_fk = models.ForeignKey(Expression, on_delete=models.CASCADE,)
    name = models.CharField(max_length=50)
    min = models.FloatField()
    max = models.FloatField()
    step = models.FloatField()


class Result(models.Model):
    expr_fk = models.ForeignKey(Expression, on_delete=models.CASCADE)
    args = JSONField()
    result = models.FloatField()


class User(models.Model):
    user_id = models.IntegerField(auto_created=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class WorkNode:
    vmid = models.IntegerField(unique=True)
    is_free = models.BooleanField(default=True)
    expr_pk = models.IntegerField(default=-1)
