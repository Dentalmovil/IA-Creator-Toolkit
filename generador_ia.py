import datetime
import random
import requests

def enviar_whatsapp(mensaje):
    # Recuerda obtener tu API KEY en https://www.callmebot.com/
    numero = "3114275056"
    api_key = "TU_API_KEY_AQUI" 
    url = f"https://api.callmebot.com/whatsapp.php?phone={numero}&text={mensaje}&apikey={api_key}"
    
    try:
        # Solo intentará enviar si cambias la API_KEY
        if api_key != "TU_API_KEY_AQUI":
            response = requests.get(url)
            print("Estado del envío WhatsApp:", response.status_code)
    except Exception as e:
        print(f"Error enviando WhatsApp: {e}")

def generar_contenido():
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Lista actualizada con tus proyectos vigentes
    temas = [
        "Nuevas funciones para Aura WhatsApp Bot",
        "Optimización de bases de datos en Sistemas Data R4",
        "Integración de GitHub Actions con Sistemas Data R4",
        "Cómo gestionar Aura WhatsApp Bot desde Termux",
        "Análisis de datos agrícolas en Sistemas Data R4",
        "Seguridad y cifrado para bots en Aura WhatsApp Bot"
    ]
    
    tema_elegido = random.choice(temas)
    
    # Formato para el mensaje de WhatsApp
    mensaje_wa = f"🚀 *IA Creator Idea* ({fecha}):\n\nProyecto: *{tema_elegido}*\n\n¡Manos a la obra, colega! 💻"
    
    # Ejecutar acciones
    enviar_whatsapp(mensaje_wa)
    
    # Guardar reporte en el repositorio
    contenido_md = f"# Reporte de Innovación - {fecha}\n\n**Proyecto seleccionado:** {tema_elegido}\n\n*Generado automáticamente para Dentalmovilr4.*"
    
    with open("IDEAS_DIARIAS.md", "w", encoding="utf-8") as f:
        f.write(contenido_md)

if __name__ == "__main__":
    generar_contenido()



