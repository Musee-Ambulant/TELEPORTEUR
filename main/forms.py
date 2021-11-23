from django import forms


class CreateNewEcole(forms.Form):
    name = forms.CharField(label="Nom École", max_length=200)


class CreateNewGroupe(forms.Form):
    name = forms.CharField(label="Nom Groupe", max_length=200)


class CreateNewAmi(forms.Form):
    name = forms.CharField(label="Nom Ami", max_length=200)


class DeleteEcole(forms.Form):
    name = forms.CharField(label="suprimer", max_length=200)
