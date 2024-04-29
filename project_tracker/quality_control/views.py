from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from quality_control.models import BugReport, FeatureRequest
from quality_control.forms import BugReportForm, FeatureRequestForm
#FBV

def index(request):
    return render(request, 'quality_control/index.html')

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bug_list': bugs})

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})

def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list': features})

def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature})

def create_bug(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_create.html', {'form': form})

def create_feature(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_create.html', {'form': form})

def update_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_detail', bug_id=bug.id)
    else:
        form =  BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_update.html', {'form': form, 'bug': bug})

def update_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail', feature_id=feature.id)
    else:
        form =  FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_update.html', {'form': form, 'feature': feature})

def delete_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()
    return redirect('quality_control:bug_list')

def delete_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    feature.delete()
    return redirect('quality_control:feature_list')

# CBV

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')

class BugReportListView(ListView):
    model = BugReport
    context_object_name = 'bug_list'
    template_name = 'quality_control/bug_list.html'

class FeatureRequestListView(ListView):
    model = FeatureRequest
    context_object_name = 'feature_list'
    template_name = 'quality_control/feature_list.html'

class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    context_object_name = 'bug'
    template_name = 'quality_control/bug_detail.html'
    
class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    context_object_name = 'feature'
    template_name = 'quality_control/feature_detail.html'

class BugReportCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_create.html'
    success_url = reverse_lazy('quality_control:bug_list')

class FeatureRequestCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_create.html'
    success_url = reverse_lazy('quality_control:feature_list')

class BugReportUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_update.html'
    pk_url_kwarg = 'bug_id'

    def get_success_url(self):
        return reverse_lazy('quality_control:bug_detail', kwargs={'bug_id': self.object.id})
    
class FeatureRequestUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequest
    template_name = 'quality_control/feature_update.html'
    pk_url_kwarg = 'feature_id'

    def get_success_url(self):
        return reverse_lazy('quality_control:feature_detail', kwargs={'feature_id': self.object.id})

class BugReportDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    context_object_name = 'bug'
    success_url = reverse_lazy('quality_control:bug_list')
    template_name = 'quality_control/bug_confirm_delete.html'

class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    context_object_name = 'feature'
    success_url = reverse_lazy('quality_control:feature_list')
    template_name = 'quality_control/feature_confirm_delete.html'