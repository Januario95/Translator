from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import translators as ts

from .forms import TranslateFom
from .helpers import LANGUAGES

import json

# ts.preaccelerate()

@require_POST
def translate_api(request):
    data = json.loads(request.body)
    from_language = LANGUAGES[data.get('from_language')]
    to_language = LANGUAGES[data.get('to_language')]
    query_text = data.get('query_text')

    translation = ts.translate_text(
        query_text=query_text,
        to_language=to_language)

    return JsonResponse({
        'translation': translation
    })

def translate_view(request):
    translation = ''
    if request.method == 'POST':
        form = TranslateFom(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # print(data)
            from_language = LANGUAGES[data.get('from_language')]
            to_language = LANGUAGES[data.get('to_language')]
            query_text = data.get('query_text')
            print(from_language)
            print(to_language)

            translation = ts.translate_text(
                query_text=query_text,
                to_language=to_language)
        else:
            print(form.errors)
    else:
        form = TranslateFom()

    return render(request,
                  'app/translate.html',
                  {'form': form, 'translation': translation})


