from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
# from anabond.forms import ControlPlanForm
# from anabond.models import ControlPlan, ControlPlanProperty, ControlPlanPropertyItem
from datetime import datetime
from .models import Teachers,NewsAndEvents,NewsAndEventImages, Toppers, Sports, CoCarricular, ExtraCurricular, Facilitie, SmartClass, LifeAtSchool, OrientationProgram, Gallery

class CoursesView(TemplateView):
	template_name = "base/courses.html"

	def get(self,request):
		return render(request, self.template_name,{})

class TeachersView(TemplateView):
	template_name = "base/teachers.html"

	def get(self,request):
		teachers = Teachers.objects.filter(is_approved=True)
		return render(request, self.template_name,{"teachers":teachers})

class ClassRoutinesView(TemplateView):
	template_name = "base/class_routines.html"

	def get(self,request):
		return render(request, self.template_name,{})

class AboutUsView(TemplateView):
	template_name = "base/about_us.html"

	def get(self,request):
		return render(request, self.template_name,{})

class ContactUsView(TemplateView):
	template_name = "base/contact_us.html"

	def get(self,request):
		return render(request, self.template_name,{})


class NewsAndEventsView(TemplateView):
	template_name = "base/news_and_events.html"

	def get(self,request):
		news_and_events = NewsAndEvents.objects.filter()
		return render(request, self.template_name,{"news_and_events":news_and_events})
class NewsAndEventsDetailView(TemplateView):
	template_name = "base/news_and_event_detail.html"

	def get(self,request,form_id):
		news_and_event = NewsAndEvents.objects.get(pk=form_id)
		return render(request, self.template_name,{"news_and_event":news_and_event})

class GalleryView(TemplateView):
	template_name = "base/gallery.html"

	def get(self,request):
		return render(request, self.template_name,{})

class VideosView(TemplateView):
	template_name = "base/videos.html"

	def get(self,request):
		return render(request, self.template_name,{})
class TopperView(TemplateView):
	template_name = 'base/topper.html'
	def get(self,request):
		toppers_10 = Toppers.objects.filter(std='10')
		toppers_12 = Toppers.objects.filter(std='12')
		return render(request, self.template_name,{"toppers_10":toppers_10,"toppers_12":toppers_12})

class SportsView(TemplateView):
	template_name = "base/sports.html"

	def get(self,request):
		sports = Sports.objects.filter()
		return render(request, self.template_name,{"sports":sports})
class SportsDetailView(TemplateView):
	template_name = "base/sports_detail.html"

	def get(self,request,form_id):
		sport = Sports.objects.get(pk=form_id)
		return render(request, self.template_name,{"sport":sport})

class CoCarricularView(TemplateView):
	template_name = "base/cocarricular.html"

	def get(self,request):
		cocarriculars = CoCarricular.objects.filter()
		return render(request, self.template_name,{"cocarriculars":cocarriculars})
class CoCarricularDetailView(TemplateView):
	template_name = "base/cocarricular_detail.html"

	def get(self,request,form_id):
		cocarricular = CoCarricular.objects.get(pk=form_id)
		return render(request, self.template_name,{"cocarricular":cocarricular})



class ExtraCurricularView(TemplateView):
	template_name = "base/extracurricular.html"

	def get(self,request):
		extracurriculars = ExtraCurricular.objects.filter()
		return render(request, self.template_name,{"extracurriculars":extracurriculars})
class ExtraCurricularDetailView(TemplateView):
	template_name = "base/extracurricular_detail.html"

	def get(self,request,form_id):
		extracurricular = ExtraCurricular.objects.get(pk=form_id)
		return render(request, self.template_name,{"extracurricular":extracurricular})


class FacilitieView(TemplateView):
	template_name = "base/facilitie.html"

	def get(self,request):
		facilities = Facilitie.objects.filter()
		return render(request, self.template_name,{"facilities":facilities})
class FacilitieDetailView(TemplateView):
	template_name = "base/facilitie_detail.html"

	def get(self,request,form_id):
		facilitie = Facilitie.objects.get(pk=form_id)
		return render(request, self.template_name,{"facilitie":facilitie}) 
class SmartClassView(TemplateView):
	template_name = "base/smartclass.html"

	def get(self,request):
		smartclasss = SmartClass.objects.filter()
		return render(request, self.template_name,{"smartclasss":smartclasss})
class SmartClassDetailView(TemplateView):
	template_name = "base/smartclass_detail.html"

	def get(self,request,form_id):
		smartclass = SmartClass.objects.get(pk=form_id)
		return render(request, self.template_name,{"smartclass":smartclass})
class LifeAtSchoolView(TemplateView):
	template_name = "base/life_at_school.html"

	def get(self,request):
		life_at_schools = LifeAtSchool.objects.filter()
		return render(request, self.template_name,{"life_at_schools":life_at_schools})
class LifeAtSchoolDetailView(TemplateView):
	template_name = "base/life_at_school_detail.html"

	def get(self,request,form_id):
		life_at_school = LifeAtSchool.objects.get(pk=form_id)
		return render(request, self.template_name,{"life_at_school":life_at_school})

class OrientationProgramView(TemplateView):
	template_name = "base/orientation_program.html"

	def get(self,request):
		orientation_programs = OrientationProgram.objects.filter()
		return render(request, self.template_name,{"orientation_programs":orientation_programs})
class OrientationProgramDetailView(TemplateView):
	template_name = "base/orientation_program_detail.html"

	def get(self,request,form_id):
		orientation_program = OrientationProgram.objects.get(pk=form_id)
		return render(request, self.template_name,{"orientation_program":orientation_program})


class GalleryView(TemplateView):
	template_name = "base/gallery.html"

	def get(self,request):
		gallerys = Gallery.objects.filter()
		return render(request, self.template_name,{"gallerys":gallerys})
class GalleryDetailView(TemplateView):
	template_name = "base/gallery_detail.html"

	def get(self,request,form_id):
		gallery = Gallery.objects.get(pk=form_id)
		return render(request, self.template_name,{"gallery":gallery})