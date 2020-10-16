from django.contrib import admin

class FuncionarioAdmin(admin.ModelAdmin):
    fields = ('empresa',)
    def save_model(self, request, instance, form, change):
        print('Entrou no editar ......')
        form.empresa = request.empresa
        form.save()