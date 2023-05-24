from django.forms import ModelForm
from django import forms

from .models import Election, Constituency, Candidates, Voters


class ElectionForm(ModelForm):
    class Meta:
        model = Election
        fields = '__all__'


class AddConstituencyForm(ModelForm):
    class Meta:
        model = Constituency
        fields = "__all__"

    # def __int__(self, *args, **kwargs):
    #     super.__init__(*args, **kwargs)
    #     self.fields['constituency'].queryset = Constituency.objects.none()

    #     if 'election' in self.data:
    #         try:
    #             election_id = int(self.data.get('election'))
    #             self.fields['constituency'].queryset = Constituency.objects.filter(
    #                 election_id=election_id)
    #         except (ValueError, TypeError):
    #             pass
    #     elif self.instance.pk:
    #         self.fields['constituency'].queryset = self.instance.election.constituency_set


class AddCandidateForm(ModelForm):
    class Meta:
        model = Candidates
        fields = ['constituency', 'name',
                  'party_name', 'photo', 'candidate_symbol']


class AddVoterForm(ModelForm):
    class Meta:
        model = Voters
        fields = ['name', 'UID', 'photo']
