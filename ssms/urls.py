""" Default urlconf for {{ project_name }} """

from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.static import serve
from .views import CoursesView,TeachersView,ClassRoutinesView,AboutUsView,ContactUsView,NewsAndEventsView,GalleryView,VideosView, NewsAndEventsDetailView, TopperView, SportsView, SportsDetailView, CoCarricularView, CoCarricularDetailView,ExtraCurricularView,ExtraCurricularDetailView,FacilitieView,FacilitieDetailView,SmartClassView, SmartClassDetailView, LifeAtSchoolView, LifeAtSchoolDetailView,OrientationProgramView, OrientationProgramDetailView,GalleryView, GalleryDetailView, AdmissionCriteria, HistoryView, ClassRoutineView,ClassRoutineDetailView,AwardView ,AwardDetailView

admin.autodiscover()

def bad(request):
    """ Simulates a server error """
    1 / 0


urlpatterns = patterns('',
        # Examples:
        # url(r'^$', '{{ project_name }}.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),
        url(r'^accounts/', include('allauth.urls')),
        url(r'^grappelli/', include('grappelli.urls')),
        url(r'^admin/', include(admin.site.urls)),
        url(r'', include('base.urls')),
        url(r'^bad/$', bad),
        url(r'^i18n/', include('django.conf.urls.i18n')),

        url(r'^courses/$', CoursesView.as_view(), name='courses'),
        url(r'^teachers/$', TeachersView.as_view(), name='teachers'),
        url(r'^class-routines/$', ClassRoutinesView.as_view(), name='class_routines'),
        url(r'^about-us/$', AboutUsView.as_view(), name='about_us'),
        url(r'^contact-us/$', ContactUsView.as_view(), name='contact_us'),
        url(r'^news-and-events/$', NewsAndEventsView.as_view(), name='news_and_events'),
        url(r'^news-and-event/(?P<form_id>\d+)/$', NewsAndEventsDetailView.as_view(), name='news_and_event_detail'),
        url(r'^gallery/$', GalleryView.as_view(), name='gallery'),
        url(r'^videos/$', VideosView.as_view(), name='videos'),
        url(r'^topper/$', TopperView.as_view(), name='topper'),
        
        url(r'^sports/$', SportsView.as_view(), name='sports'),
        url(r'^sports/(?P<form_id>\d+)/$', SportsDetailView.as_view(), name='sports_detail'),

        url(r'^cocurricular/$', CoCarricularView.as_view(), name='cocarricular'),
        url(r'^cocarricular/(?P<form_id>\d+)/$', CoCarricularDetailView.as_view(), name='cocarricular_detail'),
        url(r'^extracurricular/$', ExtraCurricularView.as_view(), name='extracurricular'),
        url(r'^extracurricular/(?P<form_id>\d+)/$', ExtraCurricularDetailView.as_view(), name='extracurricular_detail'),
        url(r'^facilitie/$', FacilitieView.as_view(), name='facilitie'),
        url(r'^facilitie/(?P<form_id>\d+)/$', FacilitieDetailView.as_view(), name='facilitie_detail'),
        url(r'^smartclass/$', SmartClassView.as_view(), name='smartclass'),
        url(r'^smartclass/(?P<form_id>\d+)/$', SmartClassDetailView.as_view(), name='smartclass_detail'),
        url(r'^life-at-school/$', LifeAtSchoolView.as_view(), name='life_at_school'),
        url(r'^life-at-school/(?P<form_id>\d+)/$', LifeAtSchoolDetailView.as_view(), name='life_at_school_detail'),
        url(r'^orientation-program/$', OrientationProgramView.as_view(), name='orientation_program'),
        url(r'^orientation-program/(?P<form_id>\d+)/$', OrientationProgramDetailView.as_view(), name='orientation_program_detail'),

        url(r'^gallery/$', GalleryView.as_view(), name='gallery'),
        url(r'^gallery/(?P<form_id>\d+)/$', GalleryDetailView.as_view(), name='gallery_detail'),
        url(r'^admission-criteria/$', AdmissionCriteria.as_view(), name='admission_criteria'),
        url(r'^history/$', HistoryView.as_view(), name='history'),

        url(r'^class-routine/$', ClassRoutineView.as_view(), name='class_routine'),
        url(r'^class-routine/(?P<form_id>\d+)/$', ClassRoutineDetailView.as_view(), name='class_routine_detail'),
        url(r'^awards/$', AwardView.as_view(), name='award'),
        url(r'^awards/(?P<form_id>\d+)/$', AwardDetailView.as_view(), name='award_detail'),
        )



if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})
    ]
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]
