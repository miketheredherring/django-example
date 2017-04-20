from django.conf.urls import include, url

from genomics import views

urlpatterns = [
    # `Gene` URLs
    url(r'^genes/', include([
        url(r'^$', views.GeneListView.as_view(), name='list'),
        url(r'^(?P<ens_gene>ENSG[0-9]{11})/$', views.GeneDetailView.as_view(), name='detail'),
    ], namespace='gene')),
]
