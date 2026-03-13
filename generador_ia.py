import datetime
import random

def generar_contenido():
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Temas alineados con tus proyectos actuales
    temas = [
        "Automatización de trading con Aura Trade AI",
        "Gestión de repositorios desde Termux y Acode",
        "Análisis de suelos y cultivos con Bio-repo-cultivos",
        "Desarrollo de portafolios digitales para Creadores",
        "Uso de Brain.js para predicción de criptomonedas"
    ]
    
    tema_elegido = random.choice(temas)
    
    contenido = f"""# Ideas de Contenido - {fecha}

**Estado:** Generado por IA (Dentalmovilr4)

## Idea del Día:
> {tema_elegido}

### Pasos sugeridos:
1. Revisar la última actualización en GitHub.
2. Grabar proceso en Termux.
3. Publicar avance en el dashboard de Vercel.
"""
    
    with open("IDEAS_DIARIAS.md", "w", encoding="utf-8") as f:
        f.write(contenido)
    print(f"Archivo generado exitosamente: {tema_elegido}")

if __name__ == "__main__":
    generar_contenido()

