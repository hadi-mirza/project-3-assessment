from django.shortcuts import render, redirect
from .models import Widget
from django.views.generic import DeleteView
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.db.models import Sum

# Create your views here.

class WidgetForm(ModelForm):
    class Meta: 
        model = Widget
        fields = ('__all__')
        success_url = reverse_lazy('home')

def home(request):
    widgets = Widget.objects.all()
    total_quantity = Widget.objects.aggregate(Sum('quantity'))
    total_quantity = total_quantity['quantity__sum']
    if request.method == 'POST':
        form = WidgetForm(request.POST)
        new_widget = form.save(commit=False)
        new_widget.save()
        return render(request, 'main_app/widget_list.html', {'form': WidgetForm, 'widgets': widgets}) 
    else:  
        return render(request, 'main_app/widget_list.html', {'form': WidgetForm, 'widgets': widgets, 'total_quantity': total_quantity})
    
def delete(request,widget_id):
    widgets = Widget.objects.get(id=widget_id)
    widgets.delete()
    return redirect('home')