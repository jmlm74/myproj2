import itertools
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django_tables2 import RequestConfig, tables
from django.utils.html import format_html
from django.urls import reverse_lazy
from django.contrib import messages

# from sortable_listview import SortableListView
from django_filters import FilterSet, CharFilter, ChoiceFilter, ModelChoiceFilter
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalReadView, BSModalUpdateView, BSModalDeleteView

from .models import Utilisateur
from .forms import CreateUtilisateurForm,UpdateUtilisateurForm
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
        list(messages.get_messages(request))
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


class UtilisateurUpdateView(BSModalUpdateView):
    template_name = 'app_utilisateurs/dialogboxes/create_utilisateur.html'
    form_class = UpdateUtilisateurForm
    success_message = 'Modification utilisateur OK !'
    success_url = reverse_lazy('app_utilisateurs:list')
    model = Utilisateur

    def get_context_data(self, **kwargs):
        context = super(UtilisateurUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Modification utilisateur"
        context['button_title'] = "Update"
        return context


class UtilisateurCreateView(BSModalCreateView):
    template_name = 'app_utilisateurs/dialogboxes/create_utilisateur.html'
    form_class = CreateUtilisateurForm
    success_message = 'Creation utilisateur OK !'
    success_url = reverse_lazy('app_utilisateurs:list')

    def get_context_data(self, **kwargs):
        context = super(UtilisateurCreateView, self).get_context_data(**kwargs)
        context['title'] = "Création utilisateur"
        context['button_title'] = "Create"
        return context

        
    def post(self, request, *args, **kwargs):
        list(messages.get_messages(request))
        myform = CreateUtilisateurForm(request.POST)
        if self.request.is_ajax():
            return redirect(self.success_url)
        if myform.is_valid():
            print("Ici créer l'utilisateur!")  
            util_civil = myform.cleaned_data['util_civil']
            util_first_name = myform.cleaned_data['util_first_name']
            util_last_name = myform.cleaned_data['util_last_name']
            util_email = myform.cleaned_data['util_email']
            util_phone1 = myform.cleaned_data['util_phone1']
            util_is_active = myform.cleaned_data['util_is_active']
            Utilisateur.objects.create(util_civil=util_civil,
                                       util_first_name=util_first_name,
                                       util_last_name=util_last_name,
                                       util_email=util_email,
                                       util_phone1=util_phone1,
                                       util_is_active=util_is_active)
        else:
            list(messages.get_messages(request))
            messages.add_message(request, messages.ERROR, "Erreur création : @ mail doit être unique ")
        return redirect(self.success_url)
    
class UtilisateurDeleteView(BSModalDeleteView):
    template_name = 'app_utilisateurs/dialogboxes/delete_utilisateur.html'
    model = Utilisateur
    success_message = "Supression utilisateur OK !"
    success_url = reverse_lazy('app_utilisateurs:list')

    def get_context_data(self, **kwargs):
        context = super(UtilisateurDeleteView, self).get_context_data(**kwargs)
        context['utilisateur'] = Utilisateur.objects.get(pk=self.kwargs['pk'])
        context['title'] = f"Suppression Utilisateur N° {self.kwargs['pk']}"
        return context