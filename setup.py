from setuptools import setup, find_packages

setup(
	name             = "django-pdf",
	version          = 0.1,
	url              = "https://github.com/directeur/django-pdf",
	license          = "GPLv2",
	description      = "A Django middleware that automatically converts views from html to pdf output.",
	author           = "Karim A. (Directeur) <directeur@gmail.com>",
	packages         = find_packages("django_pdf"),
	package_dir      = {"": "django_pdf"},
	install_requires = ["setuptools",] + open("requirements.txt").readlines()
)
