from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Utilisateur
from django import forms

class CreateUtilisateurForm(BSModalModelForm):
    class Meta:
        model = Utilisateur
        fields = '__all__'

    def clean(self,*args, **kwargs):
        super(CreateUtilisateurForm, self).clean(*args, **kwargs)
        email = self.cleaned_data.get('util_email')
        count = Utilisateur.objects.filter(util_email=email).count()
        if count > 0:
            print('Erreur')
            raise forms.ValidationError("ERREUR")
        return self.cleaned_data


class UpdateUtilisateurForm(BSModalModelForm):
    class Meta:
        model = Utilisateur
        fields = '__all__'