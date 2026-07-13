import flet as ft
import random
import os
import ssl

# ======================================================================
# SOLUCIÓN AL ERROR DE CERTIFICADO SSL
# ======================================================================
if not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
    ssl._create_default_https_context = ssl._create_unverified_context
# ======================================================================

def main(page: ft.Page):
    # Configuración de la ventana (Modo teléfono móvil)
    page.title = "Math Game Móvil"
    page.window_width = 380
    page.window_height = 700
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK # Modo oscuro moderno

    # Variables del juego usando el estado interno de Python
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operacion = random.choice(["+", "-", "*"])
    score = 0

    # Calcular la primera respuesta correcta
    if operacion == "+": respuesta_correcta = num1 + num2
    elif operacion == "-": respuesta_correcta = num1 - num2
    else: respuesta_correcta = num1 * num2

    # --- ELEMENTOS VISUALES ---
    txt_score = ft.Text(f"Puntaje: {score}", size=24, weight=ft.FontWeight.BOLD, color="green")
    txt_operacion = ft.Text(f"{num1} {operacion} {num2}", size=45, weight=ft.FontWeight.BOLD)
    
    txt_respuesta = ft.TextField(
        label="Tu respuesta", 
        keyboard_type=ft.KeyboardType.NUMBER, # Teclado numérico directo en celulares
        text_align=ft.TextAlign.CENTER,
        width=200,
        autofocus=True
    )
    
    txt_mensaje = ft.Text("", size=18, weight=ft.FontWeight.W_500)

    # --- LÓGICA DEL JUEGO ---
    def generar_nueva_operacion():
        nonlocal num1, num2, operacion, respuesta_correcta
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        operacion = random.choice(["+", "-", "*"])
        
        if operacion == "+": respuesta_correcta = num1 + num2
        elif operacion == "-": respuesta_correcta = num1 - num2
        else: respuesta_correcta = num1 * num2
        
        txt_operacion.value = f"{num1} {operacion} {num2}"
        txt_respuesta.value = ""
        page.update()

    def verificar_respuesta(e):
        nonlocal score
        
        # Validar si el cuadro está vacío
        if not txt_respuesta.value:
            txt_mensaje.value = "¡Escribe un número!"
            txt_mensaje.color = "orange"
            page.update()
            return

        # Validar si el usuario metió texto en vez de números
        try:
            int_respuesta = int(txt_respuesta.value)
        except ValueError:
            txt_mensaje.value = "Solo se permiten números"
            txt_mensaje.color = "red"
            page.update()
            return

        # Comprobar resultado matemático
        if int_respuesta == respuesta_correcta:
            score += 1
            txt_score.value = f"Puntaje: {score}"
            txt_mensaje.value = "¡Correcto! 🎉"
            txt_mensaje.color = "green"
            generar_nueva_operacion()
        else:
            txt_mensaje.value = f"Incorrecto ❌ Era {respuesta_correcta}"
            txt_mensaje.color = "red"
            txt_respuesta.value = ""
            page.update()

    # Botón principal adaptado al estándar más reciente de Flet
    btn_enviar = ft.ElevatedButton(
        content=ft.Text("Comprobar", color="white", weight=ft.FontWeight.BOLD), 
        on_click=verificar_respuesta,
        style=ft.ButtonStyle(bgcolor="blue")
    )

    # --- INTERFAZ TIPO CARD MÓVIL ---
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Math Challenge 🧠", size=28, weight=ft.FontWeight.BOLD),
                    ft.Divider(height=20, color="grey"),
                    txt_score,
                    ft.Container(height=40),
                    txt_operacion,
                    ft.Container(height=20),
                    txt_respuesta,
                    ft.Container(height=10),
                    btn_enviar,
                    ft.Container(height=30),
                    txt_mensaje
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=30,
            margin=10,
            bgcolor="black26",
            border_radius=20,
            alignment=ft.Alignment(0, 0) # Coordenadas X=0, Y=0 para centrar
        )
    )

# CONFIGURACIÓN DINÁMICA PARA INTERNET (RENDER) Y LOCAL
if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 8550))
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, host="0.0.0.0", port=puerto)