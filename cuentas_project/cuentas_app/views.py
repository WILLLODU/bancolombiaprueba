from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm, CuentaForm, ClaveDinamicaForm
from .models import Cliente, Cuenta, ClaveDinamica

def cliente_create(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        cuenta_form = CuentaForm(request.POST)
        clave_form = ClaveDinamicaForm(request.POST)
        if cliente_form.is_valid() and cuenta_form.is_valid() and clave_form.is_valid():
            cliente = cliente_form.save()
            cuenta = cuenta_form.save(commit=False)
            cuenta.cedula_cliente = cliente
            cuenta.save()
            clave = clave_form.save(commit=False)
            clave.cedula_cliente = cliente
            clave.save()
            return redirect('cliente_list')
    else:
        cliente_form = ClienteForm()
        cuenta_form = CuentaForm()
        clave_form = ClaveDinamicaForm()
    return render(request, 'cliente_create.html', {'cliente_form': cliente_form, 'cuenta_form': cuenta_form, 'clave_form': clave_form})

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})

def cliente_update(request, cedula):
    cliente = get_object_or_404(Cliente, cedula=cedula)
    cuenta = get_object_or_404(Cuenta, cedula_cliente=cliente)
    clave = get_object_or_404(ClaveDinamica, cedula_cliente=cliente)
    
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST, instance=cliente)
        cuenta_form = CuentaForm(request.POST, instance=cuenta)
        clave_form = ClaveDinamicaForm(request.POST, instance=clave)
        if cliente_form.is_valid() and cuenta_form.is_valid() and clave_form.is_valid():
            cliente_form.save()
            cuenta_form.save()
            clave_form.save()
            return redirect('cliente_list')
    else:
        cliente_form = ClienteForm(instance=cliente)
        cuenta_form = CuentaForm(instance=cuenta)
        clave_form = ClaveDinamicaForm(instance=clave)

    return render(request, 'cliente_update.html', {
        'cliente_form': cliente_form,
        'cuenta_form': cuenta_form,
        'clave_form': clave_form,
        'cliente': cliente
    })

def cliente_detail(request, cedula):
    cliente = get_object_or_404(Cliente, cedula=cedula)
    cuentas = Cuenta.objects.filter(cedula_cliente=cliente)
    clave = ClaveDinamica.objects.filter(cedula_cliente=cliente).first()
    return render(request, 'cliente_detail.html', {'cliente': cliente, 'cuentas': cuentas, 'clave': clave})


def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, cedula=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'cliente_delete.html', {'cliente': cliente})
