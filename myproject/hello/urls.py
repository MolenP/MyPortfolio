from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.user_profile_form)
]




#path("", TemplateView.as_view(template_name="main/index2.html", extra_context={"name":"Ерлан"}), name="index"),
#path("about/", TemplateView.as_view(template_name="main/about2.html"), name="about"),

#path("", views.task_list, name="task_list")

#path("contact-us/", views.contact_us),
#path("contacts/", views.contacts),
#path("json/", views.JSON_view),
#path("set_cookies", views.set_cookies),
#path("get_cookies", views.get_cookies)


#path("", views.articleList),
#path("Articles/<int:id>/", views.article),
#path("News", views.news)


#path("<int:id>/", views.id),
#re_path(r"^(?P<name>\w+)/(?P<age>\d+)/", views.home)