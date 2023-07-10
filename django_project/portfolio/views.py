from django.shortcuts import render
from . import models
import requests
from .forms import search_info_form
from datetime import date
from django.contrib import messages
import json   

# -------------------
# Description
# This Noble Price project displays the results of desired Noble price winners based on the year and area they worked on.
# -------------------
# API-endpoint
# URL = "http://api.nobelprize.org/2.0/nobelPrize/"
# -------------------



# Function to return the category 
def abbrivate_category(obj):
                              if obj == "che": return "Chemistry"
                              elif obj == "eco": return "Economic Sciences"
                              elif obj == "lit": return"Litterature"
                              elif obj == "pea": return "Economic Sciences"
                              elif obj == "phy": return "Physics"
                              elif obj == "med": return "Physiology or Medicin"                   


# Landing page
def home(request):
    return render(request, 'home.html')



def api_np(request):

    if request.method == 'POST':
        np_dict = {}
        category = request.POST['search_info_fld'] # Read the category
        search_year = request.POST['year_search'] # Read the year

        # To verify the year is valid
        if int(search_year) >= 1901 and int(search_year) < date.today().year:      

            # Concatenating category and year to API-endpoint
            final_URL = str("http://api.nobelprize.org/2.0/nobelPrize/")+'/'+str(category)+'/'+str(search_year)
            
            # HTTP request
            get_res = requests.get(url=final_URL)

            # Transform to json format
            data = get_res.json()
            
            # Getting the required data from json response
            info_name = data[0]                                                            
            tem_infor = info_name['laureates']

            # To print the data from the json response
            n = len(tem_infor)
            for i in range(n):
                par_info = tem_infor[i]
                try:
                    name_info = par_info['fullName']
                    mot_info = par_info['motivation']
                    prize=info_name['prizeAmount']
                    np_dict[name_info['en']]=mot_info['en']
                except:
                    name_info = "No name Found "
            abb_cat = abbrivate_category(category)

            # Saving the category and year to the database
            sav_info = models.search_info(
                                        year_search = search_year,
                                        text_search = abb_cat
                                        )
            sav_info.save()
            
            context = {'name':np_dict, 'prz':prize, 'cat':abb_cat, 'yr':search_year}
            return render(request, "portfolio/results.html", context)
            
        # Error message when the year is not valid
        else: 

            error_message= messages.warning(request, "Enter a Valid year in format 'YYYY' between 1901-previous year !!")
            form = search_info_form()
            context = {'form':form, 'error_message':error_message}
            return render(request, "portfolio/info_NP.html", context)
    
    # Landing page
    else:
        form = search_info_form()
    context = {'form':form}
    return render(request, "portfolio/info_NP.html", context)