from django.shortcuts import render

from sortable_listview import SortableListView

from .models import Utilisateur
# Create your views here.
class UTilisateurListView(SortableListView):
    """
    Users list --> SortableListView package
    The pagination has been reviewed.
    the fields (visible or not) are treated in the template
    The querysets are different depending the user profile (get_queryset)
    """
    context = {'title': "Liste Utilisateurs"}
    context_object_name = "utilisateurs"

    allowed_sort_fields = {"id": {'default_direction': '', 'verbose_name': 'Id'},
                           "util_first_name": {'default_direction': '', 'verbose_name': 'Prenom'},
                           "util_last_name": {'default_direction': '', 'verbose_name': 'Nom'},
                           "util_email": {'default_direction': '', 'verbose_name': 'Email'},
                           "util_phone1": {'default_direction': '', 'verbose_name': 'Phone'},
                           "util_is_active": {'default_direction': '', 'verbose_name': 'Actif'},
                           }

    default_sort_field = 'util_last_name'  # mandatory
    paginate_by = 5
    template_name = 'app_utilisateurs/list.html'
    model = Utilisateur
    
    def get_queryset(self):
        order = self.request.GET.get('sort')
        if order is None:
            order = self.default_sort_field
        if self.request.user.is_superuser:
            return Utilisateur.objects.all().order_by(order)
        else:
            return Utilisateur.objects.filter(util_is_active=True)\
                .order_by(order)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort'] = self.request.GET.get('sort')
        context['title'] = 'Liste Utilisateurs'
        return context
