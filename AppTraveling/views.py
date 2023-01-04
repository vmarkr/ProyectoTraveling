from django.shortcuts import render
from django.http import HttpResponse
from AppTraveling.forms import *
from AppTraveling.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate

# Inicio

def inicio(request):
    
    return render(request,"AppTraveling/InicioALRE/inicio.html")

##Sobre mi 

def about(request):
    
    return render(request, 'AppTraveling/InicioALRE/about.html')

##Login and  Logout

def login_request(request):
    if request.method =="POST":
        form = AuthenticationForm(request,data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username = usuario,password = contra)
            
            if user:
                login(request,user)
                
                return render(request,"AppTraveling/InicioALRE/inicio.html",{"mensaje":f"Bienvenido {usuario} a esta aventura."})
        else:
            return render(request,"AppTraveling/InicioALRE/inicio.html",{"mensaje":"Ocurrio un error en su ingreso de datos"})
    else:
        form = AuthenticationForm()
        
    return render(request, "AppTraveling/InicioALRE/login.html", {"form":form})

#Registro

def register(request):
    if request.method =="POST":
        
        form = RegistroFormulario(request.POST)
        
        if form.is_valid():
            
            user = form.cleaned_data['username']
            form.save()
            return render (request,"AppTraveling/InicioALRE/inicio.html",{"mensaje":"Usuario Creado :)"})
    else:
        form = RegistroFormulario()
        
    return render(request,"AppTraveling/InicioALRE/registro.html",{'form':form})

##Cambiar datos de registro
@login_required
def editarUsuario(request):
    
    usuario = request.user
        
    miFormulario = UserEditForm(request.POST)
        
    if request.method == "POST" and miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion["email"]
            usuario.set_password(informacion["password1"]) #cambia contraseña
            usuario.save()
            
            return render(request,"AppTraveling/InicioALRE/inicio.html")
        
    else:
        miFormulario = UserEditForm(initial={"email":usuario.email})
        
    return render(request,"AppTraveling/InicioALRE/editaPerfil.html" ,{'miFormulario':miFormulario,"usuario":usuario})

###############################                                         CRUD                                             #######################################  

#CRUD OF VIAJERO

#C--Crear
@login_required
def ADDviajeros (request):

    if request.method == 'POST':

        miFormulario=viajeroForm(request.POST)
        
        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            nuevoViajero = viajero(nombre=informacion['nombre'], 
                            apellido=informacion['apellido'],
                            correo=informacion['correo'],
                            destino = informacion['destino'],
                            edad=informacion['edad'],
                            adulto = informacion['adulto'])

            nuevoViajero.save()

        return render(request, 'AppTraveling/InicioALRE/inicio.html')
    
    else:

        miFormulario=viajeroForm()

    return render(request, 'AppTraveling/Viajeros/addViajeros.html',{'miFormulario':miFormulario})

#R--Leer

def viajeros (request):
    
    ALLviajeros = viajero.objects.all()
    
    context = {"viajeros":ALLviajeros}
    
    return render(request, 'AppTraveling/Viajeros/Viajeros.html', context)

#U--Actualizar
@login_required
def editarViajero(request,ViajC): 
    
    Persona = viajero.objects.get(nombre=ViajC)
    
    if request.method == "POST":
        
        miFormulario = viajeroForm (request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data 
            
            Persona.correo = informacion["correo"]
            Persona.edad = informacion["edad"]
            Persona.adulto = informacion["adulto"]
            
            Persona.save()
            
            return render(request,"AppTraveling/InicioALRE/inicio.html")
    
    else:
        miFormulario = viajeroForm(initial={"nombre":Persona.nombre,
                                            "apellido":Persona.apellido , 
                                            "correo":Persona.correo,
                                            "destino":Persona.destino, 
                                            "edad":Persona.edad,
                                            "adulto":Persona.adulto})

    return render(request,"AppTraveling/Viajeros/editarViajero.html",{'miFormulario':miFormulario, 'resultado':ViajC})

#D--Borrar
@login_required
def borrarViajero(request,ViajC):
    
    Persona = viajero.objects.get(nombre=ViajC)
    
    Persona.delete()
    
    people = viajero.objects.all()
    
    return render(request,"AppTraveling/Viajeros/Viajeros.html",{'resultados':people})


###########################################################################################################################################

#CRUD OF DESTINO

#C--Crear
@login_required
def ADDdestino (request):

    if request.method == 'POST':

        miFormulario=destinoForm(request.POST)
        
        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            nuevoDestino = viajero (nombre=informacion['nombre'],comentario=informacion['comentario'])
            
            nuevoDestino.save()

        return render(request, 'AppTraveling/InicioALRE/inicio.html')
    
    else:

        miFormulario=destinoForm()

    return render(request, 'AppTraveling/Destino/añadirDestinos.html', {'miFormulario':miFormulario})

#R--Leer
@login_required
def destinos (request):
    
    ALLdestinos = destino.objects.all()
    
    context = {"destinos":ALLdestinos}
    
    return render (request, 'AppTraveling/Destino/Destinos.html', context)

#U--Actualizar
@login_required
def editarDestino(request,Desti): 
    
    Destinos = destino.objects.get(nombre=Desti)
    
    if request.method == "POST":
        
        miFormulario = destinoForm(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data 
            
            Destinos.comentario = informacion['comentario']
            
            Destinos.save()
            
            return render(request,"AppTraveling/InicioALRE/inicio.html")
    
    else:
        miFormulario = destinoForm(initial={"nombre":Destinos.nombre,
                                            "comentario":Destinos.comentario})

    return render(request,"AppTraveling/Destino/editarDestino.html",{'miFormulario':miFormulario, 'resultado':Desti})

#D--Borrar
@login_required
def borrarDestino(request,Desti):
    
    Lugar = destino.objects.get(destino=Desti)
    
    Lugar.delete()
    
    Destinos = destino.objects.all()
    
    return render(request,"AppTraveling/Destino/Destinos.html",{'resultados':Destinos})

######################################################################################################

##CRUD OF ALOJAMIENTO

#C--Crear
@login_required
def ADDalojamiento (request):

    if request.method == 'POST':

        miFormulario=alojamientoForm(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            nuevoAlojamiento = alojamiento(nombre=informacion['nombre'], 
                            ubicacion = informacion['ubicacion'],
                            cantidad_habitaciones = informacion['cantidad_habitaciones'],
                            cantidad_personas = informacion['cantidad_personas'],
                            mascotas = informacion['mascotas'])

            nuevoAlojamiento.save()

        return render(request, 'AppTraveling/InicioALRE/inicio.html')
    
    else:

        miFormulario=alojamientoForm()

    return render(request, 'AppTraveling/Alojamientos/ADDalojamiento.html', {'miFormulario':miFormulario})

#R--Leer
@login_required
def Alojamientos (request):
    
    ALLalojamiento = alojamiento.objects.all()
    
    context = {"alojamiento":ALLalojamiento}
    
    return render (request, 'AppTraveling/Alojamientos/Alojamiento.html', context)

#U--Actualizar
@login_required
def editarAlojamiento(request,ALOJAM): 
    
    AlojamientoS = alojamiento.objects.get(nombre=ALOJAM)
    
    if request.method == "POST":
        
        miFormulario = alojamientoForm (request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data 
            
            AlojamientoS.nombre = informacion['nombre']
            AlojamientoS.ubicacion = informacion['ubicacion']
            AlojamientoS.cantidad_habitaciones = informacion['cantidad_habitaciones']
            AlojamientoS.cantidad_personas = informacion['cantidad_personas']
            AlojamientoS.mascotas = informacion['mascotas']
                        
            AlojamientoS.save()
            
            return render(request,"AppTraveling/InicioALRE/inicio.html")
    
    else:
        miFormulario = alojamientoForm(initial={"nombre":AlojamientoS.nombre,
                                            "ubicacion":AlojamientoS.ubicacion , 
                                            "cantidad_habitaciones":AlojamientoS.cantidad_habitaciones,
                                            "cantidad_personas":AlojamientoS.cantidad_personas, 
                                            "mascotas":AlojamientoS.mascotas})

    return render(request,"AppTraveling/Alojamientos/editarAlojamiento.html",{'miFormulario':miFormulario, 'resultado':ALOJAM})

#D--Borrar
@login_required
def borrarAlojamiento(request,ALOJAM):
    
    LugarQuedarse = alojamiento.objects.get(nombre=ALOJAM)
    
    LugarQuedarse.delete()
    
    Aloja = alojamiento.objects.all()
    
    return render(request,"AppTraveling/Alojamientos/Alojamiento.html",{'resultados':Aloja})

######################################################################################################

##CRUD OF VUELOS

#C--Crear
@login_required
def ADDvuelos (request):

    if request.method == 'POST':

        miFormulario=vuelosForm(request.POST)
        
        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            nuevoVuelo = vuelos(numero=informacion['numero'], 
                            destino=informacion['destino'],
                            origen=informacion['origen'],
                            salida = informacion['salida'],
                            llegada=informacion['llegada'],
                            cantidad_pasajes = informacion['cantidad_pasajes'],
                            empresa = informacion['empresa'])

            nuevoVuelo.save()

        return render(request, 'AppTraveling/InicioALRE/inicio.html')
    
    else:

        miFormulario=vuelosForm()

    return render(request, 'AppTraveling/Vuelos/ADDvuelos.html',{'miFormulario':miFormulario})

#R--Leer
@login_required
def Vuelo (request):
    
    ALLvuelos = vuelos.objects.all()
    
    context = {"vuelos":ALLvuelos}
    return render(request, 'AppTraveling/Vuelos/Vuelos.html', context)

#U--Actualizar
@login_required
def editarVuelos(request,VueloN):
    
    Vuelo = vuelos.objects.get(numero=VueloN)
    
    if request.method == "POST":
        
        miFormulario = vuelosForm(request.POST)
        
        
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data 
            
            Vuelo.destino = informacion["destino"]
            Vuelo.origen = informacion["origen"]
            Vuelo.salida = informacion["salida"]
            Vuelo.llegada = informacion["llegada"]
            Vuelo.cantidad_pasajes = informacion["cantidad_pasajes"]
            Vuelo.empresa = informacion["empresa"]
            
            Vuelo.save()
            
            return render(request,"AppTraveling/InicioALRE/inicio.html")
    
    else:
        miFormulario = vuelosForm(initial={"numero":Vuelo.numero,
                                            "destino":Vuelo.destino , 
                                            "origen":Vuelo.origen,
                                            "salida":Vuelo.salida, 
                                            "llegada":Vuelo.llegada,
                                            "cantidad_pasajes":Vuelo.cantidad_pasajes,
                                            "empresa":Vuelo.empresa})

    return render(request,"AppTraveling/Vuelos/editarVuelos.html",{'miFormulario':miFormulario, 'resultado':VueloN})

#D--Borrar
@login_required
def borrarVuelo(request, VueloN):
    
    Transporte = vuelos.objects.get(numero=VueloN)
    Transporte.delete()
    
    aviones = vuelos.objects.all()
    
    return render(request,"AppTraveling/Vuelos/Vuelos.html",{'resultados':aviones})

######################################################################################################
