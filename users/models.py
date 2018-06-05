from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import FileField
# Create your models here.

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


class User(AbstractUser):
	SEX = (
		("male", 'Male'),
		('female', 'Female')
	)
	TYPES = (
		("parents", 'Parents'),
		('assistant_teacher', 'Assistant Teacher')
	)
	tos = models.BooleanField(default=False)
	sex=models.CharField(max_length=255,choices=SEX,null=True,blank=True)
	telephone = models.CharField(max_length=255,null=True,blank=True)
	code_postal = models.CharField(max_length=255,null=True,blank=True)
	city = models.CharField(max_length=255,null=True,blank=True)
	address = models.CharField(max_length=255,null=True,blank=True)
	user_type = models.CharField(max_length=255,choices=TYPES,null=True,blank=True)
	image = ContentTypeRestrictedFileField(null=True, blank=True, default='',max_length=200, upload_to='profile',content_types=['image/jpeg', 'image/png'],verbose_name='Banner image')