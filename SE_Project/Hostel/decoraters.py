from django.http import HttpResponse
from django.shortcuts import redirect,render

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
					return render(request, 'Hostel/authorization.html')
				
			else:
				return render(request, 'Hostel/authorization.html')
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
			return render(request, 'Hostel/application_review.html')
	return wrapper_function


def student_pages(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name
			if group == 'warden':
				return redirect('warden-students')

			elif group == 'caretaker':
				return redirect('caretaker-students')

		else:
			return render(request, 'Hostel/authorization.html')
	return wrapper_function