from django import forms
from .models import Tournament


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'sports', 'format', 'team_player']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply title-case and replace underscores with spaces for choices in specific fields
        for field_name in ['sports', 'format', 'team_player']:
            if field_name in self.fields:
                # Update each choice label to replace '_' with ' ' and apply title case
                self.fields[field_name].choices = [
                    (value, label.replace('_', ' ').title()) for value, label in self.fields[field_name].choices
                ]