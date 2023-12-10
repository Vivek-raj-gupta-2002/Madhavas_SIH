from django.contrib import admin
from .models import CustomUser
from django.urls import path
from django.shortcuts import render
from django import forms
from .models import AadharInfo
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


# Register your models here.
admin.site.register(CustomUser)

# https://github.com/veryacademy/YT_Django_Admin_csv_Button_Upload (Refrence for csv upload)
# handeling csv upload
class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class AadharInfoAdmin(admin.ModelAdmin):
    list_display = ('aadhar_no', 'holder_name', 'dob', 'gender', 'phone', 'email')

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
                
                created = AadharInfo.objects.update_or_create(
                        aadhar_no=fields[0],
                        holder_name=fields[1],
                        dob=fields[2],
                        gender=fields[3],
                        phone=fields[4],
                        email=fields[5],
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(AadharInfo, AadharInfoAdmin)


