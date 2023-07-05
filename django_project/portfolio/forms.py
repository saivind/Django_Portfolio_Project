from django import forms
from . import models


choices_NP = (                                                      
                              ("che","Chemistry"),
                              ("eco","Economic Sciences"),
                              ("lit","Litterature"),
                              ("pea","Peace"),
                              ("phy","Physics"),
                              ("med","Physiology or Medicin"),
)
# creating a form to display in html page
class search_info_form(forms.Form):
                              search_info_fld = forms.ChoiceField(choices = choices_NP, label='Category', initial='Choose a Category to search')
                              year_search = forms.IntegerField(label='Year', initial= 'ex: 1983')