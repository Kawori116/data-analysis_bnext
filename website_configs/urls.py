from django.urls import path
from django.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    # top keywords
    path('', include('app_top_keywords.urls')),
    path('topcorps/', include('app_top_corps.urls')),
    path('customkey/', include('app_custom_keyword.urls')),
    path('pk/', include('app_pk.urls')),
]