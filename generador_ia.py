import datetime

def generar_contenido():
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")
    temas = [
        "Automatización de procesos con GitHub Actions y Python",
        "Análisis de volatilidad en CriptoMind AI",
        "Trazabilidad bovina: Innovación en el Cesar",
        "Cómo desplegar dashboards profesionales en Vercel"
    ]
    
    import random
    tema_elegido = random.choice(temas)
    
    contenido = f"# Ideas de Contenido - {fecha}\n\n"
    contenido += f"**Tema Sugerido:** {tema_elegido}\n\n"
    contenido += "1. Crear el script en Termux.\n2. Subir a GitHub.\n3. Notificar en el bot de WhatsApp."
    
    with open("IDEAS_DIARIAS.md", "w", encoding="utf-8") as f:
        f.write(contenido)

if __name__ == "__main__":
    generar_contenido()
