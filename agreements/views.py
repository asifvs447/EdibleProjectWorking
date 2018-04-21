

from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, CreateView

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa


class EdibleHome(ListView):
    def index(request):
        return render(request, 'remember/index.html')

    #
    # def signup(request):
    #     return render(request,'enrolled_form.html')

    def agree1(request):
        if request.method=='POST':
            holiday=request.POST.get('Holiday'),
            valentine= request.POST.get('Valentine'),
            christmas= request.POST.get('Christmas')
            context={
            'myname':request.POST.get('myname'),
            'start_date':request.POST.get('startdate'),
            'end_date':request.POST.get('enddate'),
            }
            if holiday:
                context['holiday']=holiday
            if christmas:
                context['christmas']=christmas
            if valentine:
                context['valentine']= valentine
        if 'form_submited' in request.POST:
            return render_to_pdf('agree.html', {'context': context})
        return render(request, 'agree.html')


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
     return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None



# class GeneratePDF(ListView):
#  def get(self, request, *args, **kwargs):
#      template = get_template('plain.html')
#      context = {
#          "invoice_id": 123,
#          "customer_name": "John Cooper",
#          "amount": 1399.99,
#          "today": "Today",
#      }
#      html = template.render(context)
#      pdf = render_to_pdf('plain.html', context)
#      if pdf:
#          response = HttpResponse(pdf, content_type='application/pdf')
#          filename = "Invoice_%s.pdf" %("12341231")
#          content = "inline; filename='%s'" %(filename)
#          download = request.GET.get("download")
#          if download:
#              content = "attachment; filename='%s'" %(filename)
#          response['Content-Disposition'] = content
#          return response
#      return HttpResponse("Not found")




