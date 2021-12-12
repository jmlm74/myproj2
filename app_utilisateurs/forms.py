from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Utilisateur

class CreateUtilisateurForm(BSModalModelForm):
    class Meta:
        model = Utilisateur
        fields = '__all__'