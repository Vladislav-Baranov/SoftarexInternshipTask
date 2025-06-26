from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, request, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.db.models import F
from .models import Calculations
from .forms import CalculationsForm
from .model_django import calculate
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib.pagesizes import letter
from io import BytesIO


@login_required()
def head(request):
    data = {'title': 'Main page'}
    return render(request, 'main/index.html', data)

@login_required()
def about(request):
    return render(request, 'main/about.html', {'title': 'About'})

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Not Found</h1>')


class MakeCalculations(LoginRequiredMixin, CreateView):
    form_class = CalculationsForm
    template_name = 'main/calculations.html'
    success_url = reverse_lazy('result')
    extra_context = {'title': "Calculation",
                     'button_name': 'calculate'}

    def form_valid(self, form):
        w = form.save(commit=False)
        w.user = self.request.user
        self.request.user.calc_count = F('calc_count') + 1
        self.request.user.save()
        return super().form_valid(form)


@login_required()
def result(request):
    obj = Calculations.objects.latest('id')
    obj.result = calculate(obj.img.url)
    obj.save()
    return render(request, 'main/result.html', {'obj': obj})


def generate_pdf():
    obj = Calculations.objects.latest('id')
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    data = [['image', 'result'], [obj.img.url, obj.result]]
    table = Table(data)
    elements = [table]
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf


def download_pdf(request):
    pdf_content = generate_pdf()
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="result.pdf"'
    return response





