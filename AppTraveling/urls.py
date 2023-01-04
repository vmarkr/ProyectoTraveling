from django.urls import path
from AppTraveling.views import  *
from django.contrib.auth.views import LogoutView

urlpatterns = [ 
    ##INICIO
    path('', inicio, name='Inicio'),
    path('about/', about, name='Acerca de mí'),
    
    ##REGISTROS Y LOGIN
    path('login/', login_request, name = 'Login'),
    path('logout/', LogoutView.as_view(template_name='AppTraveling/logout.html'), name='Logout'),
    path('register/', register, name = 'Register'),
    path('editarUsuario/',editarUsuario,name = 'Editar usuario'),
    
    
    ##VIAJEROS CRUD
    path("AgregarViajeros/",ADDviajeros,name = 'Agregar viajeros'),
    path("Viajeros/",viajeros,name="Informacion de los viajeros"),
    path("EditarViajeros/<ViajC>",editarViajero,name="Editar viajeros"),
    path("BorrarViajeros/<ViajC>",borrarViajero,name="Borrar viajeros"),
    path('buscar/',buscar,name="Buscar viajeros"),
    
    ##DESTINO CRUD
    path("AgregarDestino/",ADDdestino,name = 'Agregar destinos'),
    path("Destinos/",destinos,name="Informacion de los destinos"),
    path("EditarDestino/<Desti>",editarDestino,name="Editar destinos"),
    path("BorrarDestino/<Desti>",borrarDestino,name="Borrar destinos"),
    
    ##ALOJAMIENTO CRUD
    path("AgregarAlojamientos/",ADDalojamiento,name = 'Agregar alojamientos'),
    path("Alojamientos/",Alojamientos,name="Informacion de los alojamientos"),
    path("EditarAlojamientos/<ALOJAM>",editarAlojamiento,name="Editar alojamientos"),
    path("BorrarAlojamientos/<ALOJAM>",borrarAlojamiento,name="Borrar alojamientos"),
    
    ##VUELOS CRUD
    path("AgregarVuelos/",ADDvuelos,name = 'Agregar vuelos'),
    path("Vuelos/",Vuelo,name="Informacion de los vuelos"),
    path("EditarVuelos/<VueloN>",editarVuelos,name="Editar vuelos"),
    path("BorrarVuelos/<VueloN>",borrarVuelo,name="Borrar vuelos"),
]