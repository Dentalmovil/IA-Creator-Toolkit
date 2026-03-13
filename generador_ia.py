import datetime
import random
import requests

def enviar_whatsapp(mensaje):
    # Usaremos una pasarela gratuita para este ejemplo
    # Debes obtener tu API KEY en https://www.callmebot.com/ (es gratis y rápido)
    numero = "3114275056"
    api_key = "TU_API_KEY_AQUI" # Reemplaza con la que te den
    url = f"https://api.callmebot.com/whatsapp.php?phone={numero}&text={mensaje}&apikey={api_key}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("WhatsApp enviado con éxito")
    except Exception as e:
        print(f"Error enviando WhatsApp: {e}")

def generar_contenido():
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")
    temas = [
        "Automatización de trading con Aura Trade AI",
        "Gestión de repositorios desde Termux y Acode",
        "Análisis de suelos con Bio-repo-cultivos",
        "Uso de Brain.js para criptos"
    ]
    tema_elegido = random.choice(temas)
    
    mensaje_wa = f"🚀 *IA Creator Idea* ({fecha}):\n\nTu tema de hoy es: *{tema_elegido}*\n\n¡A darle átomos en GitHub!"
    
    # Enviar el mensaje
    enviar_whatsapp(mensaje_wa)
    
    # Guardar en Markdown
    with open("IDEAS_DIARIAS.md", "w", encoding="utf-8") as f:
        f.write(f"# Idea: {tema_elegido}")

if __name__ == "__main__":
    generar_contenido()


