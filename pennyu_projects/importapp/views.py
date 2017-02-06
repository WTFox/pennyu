from django.shortcuts import render, HttpResponse

from .forms import ImportForm
from .utils import handle_upload


def import_products(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        if form.is_valid():
            valid, invalid = handle_upload(request.FILES['file'])
            return HttpResponse(dict(valid=valid, invalid=invalid))
    else:
        form = ImportForm()
        return render(request, 'importform.html', {
            'form': form,
        })
