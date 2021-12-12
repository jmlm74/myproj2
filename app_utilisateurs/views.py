import itertools
from django.shortcuts import render
from django_tables2 import RequestConfig, tables
from django.utils.html import format_html
from django.urls import reverse_lazy

# from sortable_listview import SortableListView
from django_filters import FilterSet, CharFilter, ChoiceFilter, ModelChoiceFilter
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalReadView, BSModalUpdateView, BSModalDeleteView

from .models import Utilisateur
from .forms import CreateUtilisateurForm
from app_utilities.views import render_col_del_generic, render_is_active_generic


class UtilisateurFilter(FilterSet):
    util_nom = CharFilter(field_name='util_first_name', lookup_expr='icontains')

    class Meta:
        model = Utilisateur
        fields = ['util_nom']


def utilisateur_list_view(request):
    context = {'title': "Gestion utilisateurs"}
    if request.method == "POST":
        return render(request, "app_utilisateurs/list2.html", context=context)
    if request.method == "GET":
        utilisateurs = Utilisateur.objects.all().order_by('util_last_name')
        myfilter = UtilisateurFilter(request.GET, queryset=utilisateurs)
        utilisateurs = myfilter.qs
        utilisateurs_table = UTilisateurListTable(utilisateurs, prefix='1-')
        RequestConfig(request, paginate={"per_page": 15}).configure(utilisateurs_table)
        context['utilisateurs_table'] = utilisateurs_table
        context['myfilter'] = myfilter
        return render(request, "app_utilisateurs/list2.html", context=context)

class UTilisateurListTable(tables.Table):

    counter = tables.columns.Column(empty_values=(), orderable=False, verbose_name="#",
                                    attrs={'td': {'class': 'util_counter_col'}})
    id = tables.columns.Column(attrs={'td': {'class': 'util_id'}})
    util_is_active = tables.columns.Column(attrs={'td': {'class': 'util_is_active'}})
    col_del = tables.columns.Column(empty_values=(),
                                    orderable=False,
                                    verbose_name="",
                                    attrs={'td': {'class': 'line_col_del_col'}})
    util_is_active = tables.columns.Column(attrs={'td': {'class': 'line_enable_col'}})

    class Meta:
        model = Utilisateur
        fields = ('counter', 'id', 'util_first_name', 'util_last_name', 'util_phone1', 'util_is_active', 'col_del')
        attrs = {'class': 'table table-striped table-hover'}

    def render_counter(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count())
        return next(self.row_counter) + 1

    def render_col_del(self, *args, **kwargs):
        var = render_col_del_generic(str(kwargs['record'].pk))
        return format_html(var)

    # noinspection PyMethodMayBeStatic
    def render_util_is_active(self, *args, **kwargs):
        var = render_is_active_generic(kwargs['value'])
        return format_html(var)


class UtilisateurDisplay(BSModalReadView):
    template_name = 'app_utilisateurs/dialogboxes/display.html'
    model = Utilisateur

    def get_context_data(self, **kwargs):
        context = super(UtilisateurDisplay, self).get_context_data(**kwargs)
        context['utilisateur'] = Utilisateur.objects.get(pk=self.kwargs['pk'])
        context['title'] = f"Utilisateur N° {self.kwargs['pk']}"
        return context

class UtilisateurCreateView(BSModalCreateView):
    template_name = 'app_utilisateurs/create_utilisateur.html'
    form_class = CreateUtilisateurForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('list')