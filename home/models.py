# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Questionnaire(models.Model):

    #__Questionnaire_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField()
    slug = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Questionnaire_FIELDS__END

    class Meta:
        verbose_name        = _("Questionnaire")
        verbose_name_plural = _("Questionnaire")


class Question(models.Model):

    #__Question_FIELDS__
    text = models.TextField(max_length=255, null=True, blank=True)
    question_type = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    visualization_library = models.CharField(max_length=255, null=True, blank=True)
    visualization_config = models.TextField(max_length=255, null=True, blank=True)
    static_image = models.TextField(max_length=255, null=True, blank=True)
    instruction = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    questionnaire_id = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)

    #__Question_FIELDS__END

    class Meta:
        verbose_name        = _("Question")
        verbose_name_plural = _("Question")


class Answerchoice(models.Model):

    #__Answerchoice_FIELDS__
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(max_length=255, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    is_correct = models.BooleanField()
    explanation = models.TextField(max_length=255, null=True, blank=True)

    #__Answerchoice_FIELDS__END

    class Meta:
        verbose_name        = _("Answerchoice")
        verbose_name_plural = _("Answerchoice")


class Participant(models.Model):

    #__Participant_FIELDS__
    session_id = models.CharField(max_length=255, null=True, blank=True)
    age_group = models.CharField(max_length=255, null=True, blank=True)
    profession = models.CharField(max_length=255, null=True, blank=True)
    experience_level = models.CharField(max_length=255, null=True, blank=True)
    education_level = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    completed_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Participant_FIELDS__END

    class Meta:
        verbose_name        = _("Participant")
        verbose_name_plural = _("Participant")


class Response(models.Model):

    #__Response_FIELDS__
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(AnswerChoice, on_delete=models.CASCADE)
    selected_choices = models.TextField(max_length=255, null=True, blank=True)
    response_time = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Response_FIELDS__END

    class Meta:
        verbose_name        = _("Response")
        verbose_name_plural = _("Response")



#__MODELS__END
