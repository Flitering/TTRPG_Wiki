from django import forms
from .models import Character
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'name',
            'race',
            'character_class',
            'level',
            'strength',
            'dexterity',
            'constitution',
            'intelligence',
            'wisdom',
            'charisma',
        ]

    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'race',
            'character_class',
            'level',
            Fieldset(
                'Атрибуты',
                'strength',
                'dexterity',
                'constitution',
                'intelligence',
                'wisdom',
                'charisma',
            ),
            ButtonHolder(
                Submit('submit', 'Сохранить', css_class='btn btn-primary')
            )
        )
