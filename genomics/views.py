from django.views.generic import DetailView, ListView

from genomics.models import Gene


# Create your views here.
class GeneListView(ListView):
    '''Simple listing of all `Genes` as a table.
    '''
    model = Gene
    template_name = 'genomics/gene-list.html'


class GeneDetailView(DetailView):
    '''Detailed informaton about a single `Gene`.
    '''
    model = Gene
    template_name = 'genomics/gene-detail.html'
    slug_field = 'ens_gene'
    slug_url_kwarg = 'ens_gene'
