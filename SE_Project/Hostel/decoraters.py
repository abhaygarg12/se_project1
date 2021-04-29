from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('Hostel-home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

				if group in allowed_roles:
					return view_func(request, *args, **kwargs)
				else:
					return HttpResponse('You are not authorized to view this page')
				
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator


def home_pages(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name
			if group == 'student':
				return redirect('student-home')

			elif group == 'warden':
				return redirect('warden-home')

			elif group == 'caretaker':
				return redirect('caretaker-home')

			else:
				return HttpResponse('You are not authorized to view this page')
		else:
			return HttpResponse('Please register yourself to access this page')
	return wrapper_function