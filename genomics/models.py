from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models
from django.core.urlresolvers import reverse


class Disease(models.Model):
    '''A known single or multi-genic disease sourced from OMIM.
    '''
    # Unique URL safe identifier.
    slug = models.SlugField(editable=False)

    # As pulled directly from OMIM, long-form unicode disease name.
    name = models.CharField(max_length=256)

    # Brief synopsis describing the symptoms of the condition.
    summary = models.TextField(blank=True, help_text='A description of the disease.')

    # Modes of inheritance
    INHERITANCE_CHOICES = (
        ('AR', 'AR: Autosomal recessive'),
        ('AD', 'AD: Autosomal dominant'),
        ('XLR', 'XLR: X-linked recessive'),
        ('XLD', 'XLD: X-linked dominant'),
        ('XL', 'XL: X-linked'),
        ('YL', 'YL: Y-linked'),
        ('MI', 'MI: Mitochondrial'),
        ('SM', 'SM: Somatic')
    )
    primary_inheritance = models.CharField(
        choices=INHERITANCE_CHOICES,
        max_length=3
    )

    def get_absolute_url(self):
        '''Returns URL of the `Disease` detail route.
        '''
        return reverse('disease:detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        '''Simple string representation of the `Disease`.
        '''
        return self.name


class Gene(models.Model):
    '''Identified genomic region from Ensembl.

    Has `start` and `end` positions on a `chromosome`.
    '''
    # Ensembl gene identifier.
    ens_gene = models.CharField(
        db_index=True,
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'(?P<ens_gene>ENSG[0-9]{11})',
                message='Please provide a valid Ensembl gene identifier'
            )
        ],
        verbose_name='Ensembl gene identifier'
    )

    # As pulled directly from Ensembl, long-form unicode gene name.
    name = models.CharField(max_length=128, db_index=True, verbose_name='Gene name')

    # Chromosome the `Gene` is located on in the genome.
    CHROMOSOME_CHOICES = tuple(
        (str(i), str(i)) for i in range(1, 23)
    ) + (('X', 'X'), ('Y', 'Y'), ('M', 'M'))
    chromosome = models.CharField(max_length=2)

    # Is this `Gene` active in the system currently?
    active = models.BooleanField(default=False)

    def get_absolute_url(self):
        '''Returns URL of the `Gene` detail route.
        '''
        return reverse('gene:detail', kwargs={'ens_gene': self.ens_gene})

    def __unicode__(self):
        '''Simple stripe representation of the `Gene`.
        '''
        return self.name
