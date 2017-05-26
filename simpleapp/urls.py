from django.conf.urls import url
from simpleapp.views import test,test2
from django.views.generic import TemplateView

urlpatterns= [
   # url(r"",test,name="test") ,

    url(r"^login/$",TemplateView.as_view(template_name="simpleapp/login.html")),
url(r"^$",test2,name="test"),
]