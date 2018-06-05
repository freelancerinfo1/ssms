from django.shortcuts import render, redirect, get_object_or_404
from django.core.cache import cache, caches
from django.contrib.sites.shortcuts import get_current_site

def siteinfo(request):
	data = {}
	return {"data":"data"}