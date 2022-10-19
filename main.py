from utils import preprocessing as pp
from utils import keyword_finder as kf
from utils import strategies as st
from google_play_scraper import app
#%%
longa = """¡Empieza ya a ganar dinero como conductor! Sé un driver en DiDi Conductor y te garantizamos mínimo $6000 pesos realizando 80 viajes en los primeros 7 días. ¡Descarga ya DiDi Driver!


Convierta su tiempo libre en ganancias como conductor y comienza a manejar para generar ganancias adicionales con viajes seguros y rápidos. ¡Descarga DiDi Conductor ahora!

¡En DiDi tu seguridad no es un mito!

Una de las más de 20 funciones de seguridad es la verificación facial para pasajeros. Si un pasajero solicita un conductor o taxi driver por primera vez o está en una zona de riesgo, la app puede pedirle una validación facial antes de confirmar el viaje. Más seguridad para que seas un driver DiDi. Para las conductoras, nuestro programa de apoyo ofrece la opción de transportar sólo otras mujeres.

Obtenga ganancias adicionales en su tiempo libre
Con DiDi, la aplicación de taxi driver y conductores privados, los conductores pueden elegir las mejores horas para conducir viajes seguros y tener ganancias mensuales garantizados.

Cuenta con una plataforma sencilla
Puedes generar ganancias adicionales con más facilidad manejando como un driver. DiDi Conductor es una plataforma de movilidad que facilita el trabajo de los conductores y taxi driver. Reciba llamadas de viajes cercanos y vea sus ganancias en tiempo real en la propia app.

Se un conductor privado o taxi driver
¡Empieza a generar más ganancias cómo uno de nuestros conductores! Si posees un automóvil privado o un driver taxi particular, puedes manejar de manera flexible y aumentar tus ganancias como un dr en el servicio de transporte privado DiDi Conductor y DiDi Taxi!

️ Viajes seguros ️
DiDi Driver tiene un equipo de seguridad 24/7. Siempre que acepte un viaje, recibirá alertas de zona de peligro, además de tener una línea directa de emergencia para brindar asistencia inmediata en caso de que la necesites.

DiDi Mujeres Conductoras
Si eres mujer y quieres ser una conductora asociada, ¡conoce nuestro programa integral de apoyo para mujeres conductoras! Puedes optar por recibir solicitudes de viaje y hacer el transporte solo de otras mujeres, para manejar de forma más segura. Así te queda tranquila para ser una conductora en DiDi Driver, conduciendo más viajes privados y generando ganancias extra.

Requisitos para registro como un driver
Para registrarte como conductor o taxi driver en la app, necesitas los siguientes documentos:
Identificación oficial (INE/IFE)
Licencia de conducir
Tarjeta de circulación
Póliza de seguro del auto
Registro Federal de Contribuyentes (RFC)
Carta de no antecedentes penales (CNAP)

Esta información de registro del driver puede cambiar según las leyes locales.

Servicios DiDi
DiDi Express: ideal para quien tiene un automóvil privado.
DiDi Taxi: si tienes un taxi, puedes recibir viajes a través de la app para transportar pasajeros que deseen viajar en taxi privado. Es como una aplicación de taxi dentro de la app DiDi.
DiDi Entrega: en lugar de transporte de pasajeros, transportará paquetes o productos.

Consulta https://mexico.didiglobal.com/centro-de-ayuda/ o contacta a través de: help.driver@mx.didiglobal.com o llamando al 800 725 8888."""
#%%
keywordfinder = kf.KeywordFinder(
                long_description=longa,
                strategy=st.Portuguese()
)
keywordfinder.stopwords
keywordfinder.get_head_tail()
keywordfinder.get_short_tail()
keywordfinder.get_long_tail()
#%%
keywordfinderenglish = kf.KeywordFinder(
                long_description=longa,
                strategy=st.English()
)
keywordfinderenglish.get_head_tail()
keywordfinderenglish.get_short_tail()
keywordfinderenglish.get_long_tail()
#%%
keywordfinderspanish = kf.KeywordFinder(
                long_description=longa,
                strategy=st.Spanish()
)
keywordfinderspanish.get_head_tail()
keywordfinderspanish.get_short_tail()
keywordfinderspanish.get_long_tail()
#%%