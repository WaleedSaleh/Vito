from django import forms
from .models import Bus

class BusForm(forms.ModelForm):

    make = forms.ChoiceField(choices=Bus.MAKE_TYPE)
    model = forms.ChoiceField(choices=Bus.MODEL_TYPE)
    year = forms.IntegerField(label="Year")
    gear = forms.ChoiceField(choices=Bus.GEAR_TYPE)
    chassis = forms.ChoiceField(choices=Bus.CHASSIS_TYPE)
    mileage = forms.IntegerField(label='Mileage')
    horse_power = forms.IntegerField(label='Horse Power')
    features = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Ex: AC, Power, Center, etc..'}),label="Features")
    capacity = forms.ChoiceField(choices=Bus.CAPACITY_TYPE)
    fuel = forms.ChoiceField(choices=Bus.FUEL_TYPE)
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add location'}))
    price = forms.FloatField()
    color = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ex:Red'}))
    chassis_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ex:WDF...'}), label='Chassis Number')
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ex:079'}),label='Phone Number')
    store_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Store'}),label='Store Name')
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Ex: needs painting'}),label="Bus Description")

    class Meta:
        model = Bus
        fields = '__all__'
