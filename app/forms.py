from django import forms


class TranslateFom(forms.Form):
    LANGUAGES = (
        ('English', 'English'),
        ('French', 'French'),
        ('Portuguese', 'Portuguese'),
        ('Russian', 'Russian'),
    )
    LANGUAGES2 = (
        ('Portuguese', 'Portuguese'),
        ('English', 'English'),
        ('French', 'French'),
        ('Russian', 'Russian'),
    )
    from_language = forms.ChoiceField(
        choices=LANGUAGES
    )
    to_language = forms.ChoiceField(
        choices=LANGUAGES2
    )
    query_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter your text here'
        }),
        max_length=500
    )