from django.contrib import admin
from .models import CustomUser, AadharInfo, Income, CasteData, Domicile, Marksheet
from django.urls import path
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


# Register your models here.
admin.site.register(CustomUser)

# https://github.com/veryacademy/YT_Django_Admin_csv_Button_Upload (Refrence for csv upload)
# handeling csv upload
class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

# aadhar Data upload -------------------------------------------------------------------

class AadharInfoAdmin(admin.ModelAdmin):

    # the display list in the backend or admin panel
    list_display = ('aadhar_no', 'holder_name', 'dob', 'gender', 'phone', 'email')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":

            # getting the csv file
            csv_file = request.FILES["csv_upload"]
            
            # check if csv or not
            if not csv_file.name.endswith('.csv'):

                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            # decoding the file
            file_data = csv_file.read().decode("utf-8")

            # removing teh heading
            csv_data = file_data.split("\n")[1:]

            # saving the data
            for x in csv_data:
                fields = x.split(",")
                if len(fields) != 6:
                    continue
                try:
                    created = AadharInfo.objects.update_or_create(
                            aadhar_no=fields[0],
                            holder_name=str(fields[1]).replace('"', ""),
                            dob=fields[2],
                            gender=fields[3],
                            phone=fields[4],
                            email=fields[5],
                        )
                except:
                    messages.warning(request, 'Something went wrong')
                    return HttpResponseRedirect(request.path_info)
                
            # redirecting to Admin page
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


admin.site.register(AadharInfo, AadharInfoAdmin)

# income Data upload --------------------------------------------------------------

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('aadhar_no', 'name', 'income', 'year')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")

            csv_data = file_data.split("\n")[1:]


            for x in csv_data:
                fields = x.split(",")
                if len(fields) != 4:
                    continue
                try:
                    created = Income.objects.update_or_create(
                            aadhar_no=AadharInfo.objects.get(aadhar_no=fields[0]),
                            name=str(fields[1]).replace('"', ""),
                            income=fields[2],
                            year=fields[3]
                        )
                except:
                    messages.warning(request, 'Something went wrong')
                    return HttpResponseRedirect(request.path_info)
                
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(Income, IncomeAdmin)


# Caste Data upload ----------------------------------------------------------------

class CasteDataAdmin(admin.ModelAdmin):
    list_display = ('aadhar_no', 'name', 'caste')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")

            csv_data = file_data.split("\n")[1:]


            for x in csv_data:
                fields = x.split(",")
                if len(fields) != 3:
                    continue
                
                try:
                    created = CasteData.objects.update_or_create(
                            aadhar_no=AadharInfo.objects.get(aadhar_no=fields[0]),
                            name=str(fields[1]).replace('"', ""),
                            caste=fields[2],
                        )
                except:
                    messages.warning(request, 'Something went wrong')
                    return HttpResponseRedirect(request.path_info)


            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(CasteData, CasteDataAdmin)



# Domicile Upload Process --------------------------------------------------------
class DomicileAdmin(admin.ModelAdmin):
    list_display = ('aadhar_no', 'name', 'city', 'state')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")

            csv_data = file_data.split("\n")[1:]


            for x in csv_data:
                fields = x.split(",")
                if len(fields) != 4:
                    continue
                try:
                    created = Domicile.objects.update_or_create(
                            aadhar_no=AadharInfo.objects.get(aadhar_no=fields[0]),
                            name=str(fields[1]).replace('"', ""),
                            city=fields[2].replace('"', ""),
                            state=fields[3].replace('"', ""),
                        )
                except:
                    messages.warning(request, 'data is Wrong')
                    return HttpResponseRedirect(request.path_info)
                    
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(Domicile, DomicileAdmin)


# markesheet data -----------------------------------------------------------------

class MarksheetAdmin(admin.ModelAdmin):
    list_display = ('aadhar_no', 'name', 'year', 'institute', 'marks', 'standard')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")

            csv_data = file_data.split("\n")[1:]


            for x in csv_data:
                fields = x.split(",")
                if len(fields) != 6:
                    continue
                try:
                    created = Marksheet.objects.update_or_create(
                            aadhar_no=AadharInfo.objects.get(aadhar_no=fields[0]),
                            name=str(fields[1]).replace('"', ""),
                            institute=fields[2].replace('"', ""),
                            year=fields[3].replace('"', ""),
                            marks=fields[4].replace('"', ""),
                            standard=fields[5].replace('"', ""),
                        )
                except:
                    messages.warning(request, 'data is Wrong')
                    return HttpResponseRedirect(request.path_info)
                    
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(Marksheet, MarksheetAdmin)
