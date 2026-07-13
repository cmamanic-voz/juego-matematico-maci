import flet as ft
import random
import time
import asyncio

class JuegoMatematico:
    def __init__(self):
        self.jugadores = []  # Lista de dicts: {"nombre": str, "puntos": int}
        self.num_jugadores = 2
        self.jugador_actual_idx = 0
        self.pregunta_actual_num = 1
        self.total_preguntas = 10
        
        # Datos de la pregunta activa
        self.respuesta_correcta = 0
        self.tiempo_inicio_pregunta = 0
        self.timer_task = None
        self.tiempo_restante = 15

    def generar_ejercicio(self):
        """Genera un ejercicio de nivel secundaria/pre al azar con su respuesta"""
        tipo = random.choice(["ecuacion", "combinada", "potencia"])
        
        if tipo == "ecuacion":
            # Formato: ax + b = c -> Hallar x
            x = random.randint(1, 10)
            a = random.randint(2, 5)
            b = random.randint(1, 15)
            c = a * x + b
            texto = f"Resuelve para X:\n{a}X + {b} = {c}"
            return texto, x
            
        elif tipo == "combinada":
            # Formato: a * (b - c) + d
            a = random.randint(2, 5)
            b = random.randint(5, 12)
            c = random.randint(1, 4)
            d = random.randint(2, 10)
            texto = f"Calcula el resultado:\n{a} × ({b} - {c}) + {d}"
            res = a * (b - c) + d
            return texto, res
            
        else:
            # Formato: a^2 + b o raíces simples
            a = random.choice([2, 3, 4, 5])
            b = random.randint(5, 20)
            texto = f"Calcula la potencia:\n{a}² + {b}"
            res = (a ** 2) + b
            return texto, res

def main(page: ft.Page):
    page.title = "Math Showdown Universitario"
    page.window_width = 450
    page.window_height = 700
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    juego = JuegoMatematico()

    # Componentes visuales reutilizables
    titulo = ft.Text("🏆 MATH SHOWDOWN 🏆", size=28, weight=ft.FontWeight.BOLD, color=ft.colors.CYAN)
    instrucciones = ft.Text("Selecciona la cantidad de competidores:", size=16)
    
    dropdown_jugadores = ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option("2 Jugadores"),
            ft.dropdown.Option("3 Jugadores"),
            ft.dropdown.Option("4 Jugadores"),
        ],
        value="2 Jugadores"
    )

    lista_inputs = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    txt_ejercicio = ft.Text("", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
    txt_turno = ft.Text("", size=18, color=ft.colors.AMBER, weight=ft.FontWeight.BOLD)
    txt_progreso = ft.Text("", size=14, color=ft.colors.GREY_400)
    txt_timer = ft.Text("", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.RED_ACCENT)
    
    input_respuesta = ft.TextField(
        label="Tu respuesta aquí", 
        width=180, 
        text_align=ft.TextAlign.CENTER,
        keyboard_type=ft.KeyboardType.NUMBER
    )
    
    progreso_barra = ft.ProgressBar(width=300, visible=False, color=ft.colors.CYAN)
    txt_cargando = ft.Text("Cargando resultados finales...", visible=False, size=16, italic=True)

    async def iniciar_timer():
        juego.tiempo_restante = 15
        while juego.tiempo_restante > 0:
            txt_timer.value = f"⏱️ Tiempo: {juego.tiempo_restante}s"
            page.update()
            await asyncio.sleep(1)
            juego.tiempo_restante -= 1
        
        # Si llega a 0 sin responder
        input_respuesta.disabled = True
        page.update()
        await asyncio.sleep(1)
        await procesar_respuesta(timeout=True)

    def mostrar_pantalla_nombres(e):
        juego.num_jugadores = int(dropdown_jugadores.value.split()[0])
        lista_inputs.controls.clear()
        for i in range(juego.num_jugadores):
            lista_inputs.controls.append(
                ft.TextField(label=f"Nombre del Jugador {i+1}", width=250, value=f"Jugador {i+1}")
            )
        
        btn_comenzar = ft.ElevatedButton("¡Empezar Batalla!", on_click=comenzar_juego, bgcolor=ft.colors.GREEN_700, color=ft.colors.WHITE)
        
        page.controls.clear()
        page.add(
            titulo,
            ft.Text("Registren sus nombres:", size=18),
            ft.Divider(),
            lista_inputs,
            ft.VerticalDivider(height=20),
            btn_comenzar
        )
        page.update()

    def comenzar_juego(e):
        juego.jugadores = []
        for tf in lista_inputs.controls:
            juego.jugadores.append({"nombre": tf.value.strip(), "puntos": 0})
        
        juego.jugador_actual_idx = 0
        juego.pregunta_actual_num = 1
        cargar_pregunta()

    def cargar_pregunta():
        if juego.timer_task:
            juego.timer_task.cancel()
            
        jugador = juego.jugadores[juego.jugador_actual_idx]
        texto, res = juego.generar_ejercicio()
        juego.respuesta_correcta = res
        
        txt_turno.value = f"🎯 Turno de: {jugador['nombre']}"
        txt_progreso.value = f"Ejercicio {juego.pregunta_actual_num} de {juego.total_preguntas}"
        txt_ejercicio.value = text=texto
        input_respuesta.value = ""
        input_respuesta.disabled = False
        
        page.controls.clear()
        page.add(
            txt_turno,
            txt_progreso,
            ft.Card(
                content=ft.Container(
                    content=txt_ejercicio,
                    padding=20,
                    alignment=ft.alignment.center
                ),
                margin=20
            ),
            txt_timer,
            ft.Row([input_respuesta], alignment=ft.MainAxisAlignment.CENTER),
            ft.VerticalDivider(height=15),
            ft.ElevatedButton("Enviar Respuesta", on_click=lambda _: asyncio.run(procesar_respuesta()), bgcolor=ft.colors.BLUE_700, color=ft.colors.WHITE)
        )
        page.update()
        juego.tiempo_inicio_pregunta = time.time()
        juego.timer_task = asyncio.ensure_future(iniciar_timer())

    async def procesar_respuesta(timeout=False):
        if juego.timer_task:
            juego.timer_task.cancel()
            
        jugador = juego.jugadores[juego.jugador_actual_idx]
        
        if not timeout:
            tiempo_empleado = time.time() - juego.tiempo_inicio_pregunta
            try:
                ans = int(input_respuesta.value)
                if ans == juego.respuesta_correcta:
                    # Sistema de puntos Pro por velocidad
                    if tiempo_empleado <= 5:
                        jugador["puntos"] += 3
                    else:
                        jugador["puntos"] += 1
                else:
                    jugador["puntos"] -= 1
            except ValueError:
                jugador["puntos"] -= 1  # Mal o vacío cuenta como error

        # Avanzar en la estructura continua
        if juego.pregunta_actual_num < juego.total_preguntas:
            juego.pregunta_actual_num += 1
            cargar_pregunta()
        else:
            # Terminó sus 10 preguntas, ¿hay siguiente jugador?
            if juego.jugador_actual_idx < len(juego.jugadores) - 1:
                juego.jugador_actual_idx += 1
                juego.pregunta_actual_num = 1
                # Pantalla de transición limpia
                page.controls.clear()
                page.add(
                    ft.Text("¡Tiempo Completado!", size=24, color=ft.colors.GREEN_400, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Siguiente turno para: {juego.jugadores[juego.jugador_actual_idx]['nombre']}", size=18),
                    ft.VerticalDivider(height=30),
                    ft.ElevatedButton("Listo, ¡A jugar!", on_click=lambda _: cargar_pregunta())
                )
                page.update()
            else:
                # ¡TODOS TERMINARON! Pantalla de suspenso solicitada
                await mostrar_pantalla_carga()

    async def mostrar_pantalla_carga():
        progreso_barra.visible = True
        txt_cargando.visible = True
        page.controls.clear()
        page.add(
            titulo,
            ft.VerticalDivider(height=50),
            txt_cargando,
            progreso_barra
        )
        page.update()
        
        # Efecto dramático de carga (3 segundos)
        await asyncio.sleep(3)
        mostrar_resultados_finales()

    def mostrar_resultados_finales():
        # Ordenar jugadores de mayor a menor puntaje (Orden de mérito)
        ranking = sorted(juego.jugadores, key=lambda k: k['puntos'], reverse=True)
        
        tabla_posiciones = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15)
        
        iconos = ["🥇", "🥈", "🥉", "👤"]
        for idx, jug in enumerate(ranking):
            ico = iconos[idx] if idx < len(iconos) else "👤"
            tabla_posiciones.controls.append(
                ft.Container(
                    content=ft.Row([
                        ft.Text(f"{ico} {idx+1}°. {jug['nombre']}", size=18, weight=ft.FontWeight.BOLD),
                        ft.Text(f"{jug['puntos']} Pts", size=18, color=ft.colors.CYAN_200, weight=ft.FontWeight.BOLD)
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    width=320,
                    bgcolor=ft.colors.SURFACE_VARIANT if idx == 0 else ft.colors.BLACK26,
                    padding=15,
                    border_radius=10
                )
            )

        page.controls.clear()
        page.add(
            ft.Text("📊 ORDEN DE MÉRITO FINAL 📊", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.AMBER),
            ft.VerticalDivider(height=20),
            tabla_posiciones,
            ft.VerticalDivider(height=30),
            ft.ElevatedButton("Reiniciar Todo", on_click=lambda _: reiniciar_todo(), bgcolor=ft.colors.RED_700, color=ft.colors.WHITE)
        )
        page.update()

    def reiniciar_todo():
        nonlocal juego
        juego = JuegoMatematico()
        page.controls.clear()
        page.add(titulo, instrucciones, dropdown_jugadores, ft.ElevatedButton("Configurar Equipos", on_click=mostrar_pantalla_nombres))
        page.update()

    # Pantalla Inicial
    page.add(
        titulo,
        ft.VerticalDivider(height=20),
        instrucciones,
        dropdown_jugadores,
        ft.VerticalDivider(height=10),
        ft.ElevatedButton("Configurar Equipos", on_click=mostrar_pantalla_nombres, bgcolor=ft.colors.BLUE_700, color=ft.colors.WHITE)
    )
    page.update()

ft.app(target=main)
