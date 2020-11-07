from django_currentuser.db.models import CurrentUserField
from django.conf import settings
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from django.db.models.signals import post_save
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# from graphene_django import DjangoObjectType
# import graphene


# Create your models here.
def post_save_receiver(sender, instance, created, **kwargs):
    pass


post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)


class Note(models.Model):
    #
    STATUS_CHOICES = (
        ('new', 'New'),
        ('actual', 'Actual'),
        ('archive', 'Archive'),
    )

    title = models.CharField(max_length=250)
    created_by = CurrentUserField(editable=False)
    body = RichTextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES, default='new')

    class Meta:
        verbose_name = _('note')
        verbose_name_plural = _('notes')
        ordering = ('-publish', )

    def __str__(self):
        return '{} (#{})'.format(self.title, self.pk)


# class Note(DjangoObjectType):
#     class Meta:
#         model = Note
