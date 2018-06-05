# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.db import connections, models
from django.contrib.auth.models import User
from django.db.models import FileField
import os
from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth.models import AbstractUser

class ContentTypeRestrictedFileField(FileField):
	def __init__(self, *args, **kwargs):
		try:
			self.content_types = kwargs.pop("content_types")
		except:
			pass
		super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

	def clean(self, *args, **kwargs):
		data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)
		file = data.file
		if hasattr(file,"content_type"):
			content_type = file.content_type
			if content_type in self.content_types:
				pass
			else:
				raise forms.ValidationError(_('Please select valid file.'))
		return data

 


class Banner(models.Model):
	image = ContentTypeRestrictedFileField(null=True, blank=True, default='',max_length=200, upload_to='banner',content_types=['image/jpeg', 'image/png'],verbose_name='Banner image')
	slide_text = models.TextField(max_length=300, null=True, blank=True)
	caption = models.CharField(max_length=100, null=True, blank=True)
	is_fadeinleft = models.BooleanField(default=False, blank=True)

class Reviews(models.Model):
	comments = models.TextField(max_length=300, null=True, blank=True)
	is_approved = models.BooleanField(default=False, blank=True)

class Courses(models.Model):
	image = ContentTypeRestrictedFileField(null=True, blank=True, default='',max_length=200, upload_to='courses',content_types=['image/jpeg', 'image/png'],verbose_name='Banner image')
	is_open = models.BooleanField(default=False, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)

class Teachers(models.Model):
	image = ContentTypeRestrictedFileField(null=True, blank=True, default='',max_length=200, upload_to='teachers',content_types=['image/jpeg', 'image/png'],verbose_name='Banner image')
	position = models.CharField(max_length=100, null=True, blank=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	is_approved = models.BooleanField(default=False, blank=True)
	home_page = models.BooleanField(default=False, blank=True)

	def __str__(self):
		return self.name

class NewsAndEvents(models.Model):
	title = models.CharField(max_length=100)
	comments = models.TextField(max_length=600, null=True, blank=True)
	def __str__(self):
		return self.title

class NewsAndEventImages(models.Model):
	image = ContentTypeRestrictedFileField(null=True, blank=True, default='',max_length=200, upload_to='news_and_events',content_types=['image/jpeg', 'image/png'],verbose_name='News And Events')
	news_and_events = models.ForeignKey(NewsAndEvents,null=True,blank=True,related_name='news_and_event_images')

class Toppers(models.Model):
	STD = (
		('10', '10'),
		('12', '+12'),
	)
	std = models.CharField(max_length=50, choices=STD)
	name = models.CharField(max_length=200,null=True,blank=True)
	image = ContentTypeRestrictedFileField(null=True, blank=True, default='',max_length=200, upload_to='toppers',content_types=['image/jpeg', 'image/png'],verbose_name='Toppers image')
	mark = models.IntegerField(null=True,blank=True)

	def __str__(self):
		return self.name


class Sports(models.Model):
	title = models.CharField(max_length=100)
	comments = models.TextField(max_length=600, null=True, blank=True)
	def __str__(self):
		return self.title

class SportsImages(models.Model):
	image = ContentTypeRestrictedFileField(null=True, blank=True, default='',max_length=200, upload_to='sports',content_types=['image/jpeg', 'image/png'],verbose_name='Sports')
	sports = models.ForeignKey(Sports,null=True,blank=True,related_name='sports_images')


class CoCarricular(models.Model):
	title = models.CharField(max_length=100)
	comments = models.TextField(max_length=600, null=True, blank=True)
	def __str__(self):
		return self.title

class CoCarricularImages(models.Model):
	image = ContentTypeRestrictedFileField(null=True, blank=True, default='',max_length=200, upload_to='cocarricular',content_types=['image/jpeg', 'image/png'],verbose_name='CoCarricular')
	cocarricular = models.ForeignKey(CoCarricular,null=True,blank=True,related_name='cocarricular_images')



class ExtraCurricular(models.Model):
	title = models.CharField(max_length=100)
	comments = models.TextField(max_length=600, null=True, blank=True)
	def __str__(self):
		return self.title

class ExtraCurricularImages(models.Model):
	image = ContentTypeRestrictedFileField(null=True, blank=True, default='',max_length=200, upload_to='extracurricular',content_types=['image/jpeg', 'image/png'],verbose_name='ExtraCurricular')
	extracurricular = models.ForeignKey(ExtraCurricular,null=True,blank=True,related_name='extracurricular_images')

class Facilitie(models.Model):
	title = models.CharField(max_length=100)
	comments = models.TextField(max_length=600, null=True, blank=True)
	def __str__(self):
		return self.title

class FacilitieImages(models.Model):
	image = ContentTypeRestrictedFileField(null=True, blank=True, default='',max_length=200, upload_to='facilitie',content_types=['image/jpeg', 'image/png'],verbose_name='facilitie')
	facilitie = models.ForeignKey(Facilitie,null=True,blank=True,related_name='facilitie_images')

class SmartClass(models.Model):
	title = models.CharField(max_length=100)
	comments = models.TextField(max_length=600, null=True, blank=True)
	def __str__(self):
		return self.title

class SmartClassImages(models.Model):
	image = ContentTypeRestrictedFileField(null=True, blank=True, default='',max_length=200, upload_to='smartclass',content_types=['image/jpeg', 'image/png'],verbose_name='smartclass')
	smartclass = models.ForeignKey(SmartClass,null=True,blank=True,related_name='smartclass_images')
class LifeAtSchool(models.Model):
	title = models.CharField(max_length=100)
	comments = models.TextField(max_length=600, null=True, blank=True)
	def __str__(self):
		return self.title

class LifeAtSchoolImages(models.Model):
	image = ContentTypeRestrictedFileField(null=True, blank=True, default='',max_length=200, upload_to='life_at_school',content_types=['image/jpeg', 'image/png'],verbose_name='life_at_school')
	life_at_school = models.ForeignKey(LifeAtSchool,null=True,blank=True,related_name='life_at_school_images')

class OrientationProgram(models.Model):
	title = models.CharField(max_length=100)
	comments = models.TextField(max_length=600, null=True, blank=True)
	def __str__(self):
		return self.title

class OrientationProgramImages(models.Model):
	image = ContentTypeRestrictedFileField(null=True, blank=True, default='',max_length=200, upload_to='orientation_program',content_types=['image/jpeg', 'image/png'],verbose_name='orientation_program')
	orientation_program = models.ForeignKey(OrientationProgram,null=True,blank=True,related_name='orientation_program_images')

class Gallery(models.Model):
	title = models.CharField(max_length=100)
	comments = models.TextField(max_length=600, null=True, blank=True)
	def __str__(self):
		return self.title

class GalleryImages(models.Model):
	image = ContentTypeRestrictedFileField(null=True, blank=True, default='',max_length=200, upload_to='gallery',content_types=['image/jpeg', 'image/png'],verbose_name='gallery')
	gallery = models.ForeignKey(Gallery,null=True,blank=True,related_name='gallery_images')