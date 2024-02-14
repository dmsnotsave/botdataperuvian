import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import base64
import io

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hola! Por favor envíame la información que desees enviar a la API POST.")

async def handle_dni(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Obtener el texto enviado por el usuario después del comando /dni
    text = ' '.join(context.args)
    
    # Encabezados que deseas enviar a la API
    headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host':'xfmxu4pxed5dy7j6v4zske2cou0owymm.lambda-url.us-east-2.on.aws',
        'Origin':'http://mpv.munidesanmarcos.gob.pe',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'Referer':'http://mpv.munidesanmarcos.gob.pe/'
        # Agrega aquí cualquier otro encabezado que necesites enviar
    }
    
    headers_ = {
        'Cookie':'XSRF-TOKEN=eyJpdiI6InZ5aVFFalZsQnFlZXo5MjRjNEluK2c9PSIsInZhbHVlIjoiLy90UjZ3dkpYMHRVUmNqK3U2RUlwOGRNOHhpVWVLeGFvNGZTS2cxUUZKemZRSVp3QmVmWDcwUzJkRnhMWFBDanA2YUh3emsvTEZwbEc3U1VyMkF0R0syV3hiZkpXMUhEQ3F1S3BzS2h6QjZ1QWlsTVdzbWFOZG1RRmFvUklYNFAiLCJtYWMiOiJkNzE3ZTQ2ZDcxMWM0NzZmYzE1OWMwMjU5NWFiYzRjMDg4ZTFkZTJjNjRkMDU0YzhmMWVlMGRjYjdlYjRhZDIwIn0%3D; laravel_session=eyJpdiI6Im9QL1l5OW1uYUN6aE1UUmxVVUkydVE9PSIsInZhbHVlIjoiYk1zY01LSkh5c3h4Zms0ekUxVlVYUENudzJYNVExVjhXYTRjdmJuT2hzdnZxMkZ3K3RlU0VFQmtUbkxHN2xPMEpMU1NCeHhWeWpRdSt6eGp3cWdQVE1RRGp1ZWJJZ0dSaklIa1Ruczc4RzNiZ0hIQVpRWXQwYVQ0cnlmRi9jTEQiLCJtYWMiOiI0OGQyNjUxZTk1YzdmY2MxZTBiYTIzYmM1YTM1M2FjNDhiOWQ4MzA2NzdiMDY5OGYxYjQyODdkMWE3NzEyMGE3In0%3D',
        'Host':'virtual.munisurquillo.gob.pe',
        'Referer':'https://virtual.munisurquillo.gob.pe/crear-cuenta',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
        # Agrega aquí cualquier otro encabezado que necesites enviar
    }
    try:
        api_urla = f'https://virtual.munisurquillo.gob.pe/api-persona?TIPO=DNI&DOCUMENTO={text}'

        response = requests.get(api_urla, data=f'TIPO=DNI&DOCUMENTO={text}', headers=headers_, verify=False)
        foto = response.json()
        foto = foto['DATA']
        foto = foto['FOTO']
        if response.status_code == 200:
            imagen_bytes = base64.b64decode(foto[22:])
            imagen_io = io.BytesIO(imagen_bytes)
            imagen_io.seek(0)
            # Enviar la imagen como foto
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=imagen_io)
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Hubo un error al enviar los datos a la API.")
    except:
        pass
    # Realizar la solicitud POST a la API con los datos recibidos y los encabezados
    api_url = 'https://xfmxu4pxed5dy7j6v4zske2cou0owymm.lambda-url.us-east-2.on.aws/'
    payload = {'codigo': text}  # Puedes ajustar esto según la estructura esperada por la API
    response = requests.post(api_url, data=payload, headers=headers)


    
    # Verificar el estado de la respuesta de la API

    if response.status_code == 200:
        dat = response.json()
        
        try:
            dat = dat['data']
            try:
                dni = dat['numero']
            except:
                dni = '****'
            try:
                veri = dat['codigo_verificacion']
            except:
                veri = '****'
            try:
                apep = dat['apellido_paterno']
            except:
                apep = '****'
            try:
                apem = dat['apellido_materno']
            except:
                apem = '****'
            try:
                nom = dat['nombres']
            except:
                nom = '****'
            try:
                sex = dat['sexo']
            except:
                sex = '****'
            try:
                fna = dat['fecha_nacimiento']
            except:
                fna = '****'
            try:
                esc = dat['estado_civil']
            except:
                esc = '****'
            try:
                dirc =dat['direccion_completa']
            except:
                dirc = '****'
            try:
                reni =dat['ubigeo_reniec']
            except:
                reni = '****'
            try:
                suna =dat['ubigeo_sunat']
            except:
                suna = '****'
        except:
            pass
        
        try:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f'''
→ RENIEC
                                       
DNI : {dni} - {veri}
APELLIDOS : {apep} {apem}
NOMBRES : {nom}
GENERO : {sex}

[📅] NACIMIENTO

FECHA NACIMIENTO : {fna}
ESTADO CIVIL : {esc}

[📍] DIRECCION

DIRECCION : {dirc}

[📍] UBICACION

UBIGEO RENIEC : {reni}
UBIGEO SUNAT : {suna}
''')
        except:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='No Valido')
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Hubo un error al enviar los datos a la API.")
    
if __name__ == '__main__':
    application = ApplicationBuilder().token('6770683590:AAEbREgVI76Fl4IOSAtbjAztPlG3T_qT78Y').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    dni_handler = CommandHandler('dni', handle_dni)
    application.add_handler(dni_handler)
    
    application.run_polling()
