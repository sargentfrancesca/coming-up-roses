from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
from client_site import views


urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^about/", views.AboutView.as_view(), name="about"),
    url(r"^treatments/", views.TreatmentView.as_view(), name="treatments"),
    url(r"^prices/", views.PriceView.as_view(), name="prices"),
    url(r"^contact/", views.ContactView.as_view(), name="contact"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# url(r"^about/", TemplateView.as_view(template_name="about.html"), name="about"),