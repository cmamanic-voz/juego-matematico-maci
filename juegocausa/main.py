import flet as ft
import random
import time
import asyncio

# =========================================================================
# CLASE: BANCO DE DATOS DEL SISTEMA (DINÁMICO Y AMPLIADO)
# =========================================================================
class BancoDatosJuegos:
    def __init__(self):
        # BANCO DE DATOS JUEGO 2: 15 NIVELES CORREGIDOS Y VERIFICADOS
        self.juego2_normales = [
            {"numeros": "[8, 4, 2, 6]", "objetivo": 10, "opciones": ["(8 ÷ 4) + 2 + 6", "(8 - 4) × 2 + 6", "(8 × 4) ÷ 2 - 6", "(8 + 4) - 2 - 6"], "correcta": "(8 ÷ 4) + 2 + 6", "tiempo": 15},
            {"numeros": "[5, 3, 4, 2]", "objetivo": 32, "opciones": ["(5 × 3) + 4 - 2", "(5 + 3) × (4 ÷ 2)", "(5 + 3) × 4", "(5 - 3) × 4 × 2"], "correcta": "(5 + 3) × 4", "tiempo": 15},
            {"numeros": "[9, 3, 5, 2]", "objetivo": 13, "opciones": ["(9 × 3) - 5", "(9 ÷ 3) + 5 × 2", "(9 + 3) × 2", "(9 - 3) × 2"], "correcta": "(9 ÷ 3) + 5 × 2", "tiempo": 15},
            {"numeros": "[6, 2, 8, 8]", "objetivo": 16, "opciones": ["(6 × 2) + 8", "(6 ÷ 2) × 8 - 8", "(6 - 2) + 8", "(6 + 2) × 2"], "correcta": "(6 ÷ 2) × 8 - 8", "tiempo": 15},
            {"numeros": "[10, 5, 4, 3]", "objetivo": 9, "opciones": ["(10 ÷ 5) + 4 + 3", "(10 - 5) × 4", "(10 ÷ 5) × 3 + 3", "(10 + 5) - 4 - 2"], "correcta": "(10 ÷ 5) + 4 + 3", "tiempo": 15},
            {"numeros": "[4, 4, 4, 4]", "objetivo": 0, "opciones": ["(4 + 4) - (4 + 4)", "(4 × 4) ÷ 4", "(4 - 4) × 4", "4 + 4 - 4"], "correcta": "(4 + 4) - (4 + 4)", "tiempo": 15},
            {"numeros": "[7, 3, 2, 1]", "objetivo": 24, "opciones": ["(7 × 3) + 2", "(7 + 3) × 2 + 3", "(7 × 3) + 2 + 1", "(7 - 3) × 5"], "correcta": "(7 × 3) + 2 + 1", "tiempo": 15},
            {"numeros": "[12, 4, 2, 5]", "objetivo": 10, "opciones": ["(12 ÷ 4) + 2 + 5", "(12 - 4) + 2", "(12 × 4) ÷ 8", "(12 + 4) ÷ 2"], "correcta": "(12 ÷ 4) + 2 + 5", "tiempo": 15}
        ]
        
        self.juego2_dificiles = [
            {"numeros": "[12, 4, 6, 2]", "objetivo": 48, "opciones": ["(12 - 4) × 6", "(12 - 4) × (6 ÷ 2) × 2", "(12 + 4) × (6 - 2)", "(12 × 4) ÷ 2"], "correcta": "(12 - 4) × (6 ÷ 2) × 2", "tiempo": 20},
            {"numeros": "[7, 5, 4, 2]", "objetivo": 35, "opciones": ["(7 × 5) + 4 - 4", "(7 × 5) × (4 - 2) ÷ 2", "(7 + 5) × 3", "(7 × 5) ÷ (4 - 2)"], "correcta": "(7 × 5) × (4 - 2) ÷ 2", "tiempo": 20},
            {"numeros": "[9, 9, 3, 5]", "objetivo": 32, "opciones": ["(9 × 9) ÷ 3", "(9 + 9) + 3 × 5", "(9 ÷ 3) × 9 + 5", "(9 - 3) × 5 + 2"], "correcta": "(9 ÷ 3) × 9 + 5", "tiempo": 20},
            {"numeros": "[15, 3, 8, 1]", "objetivo": 40, "opciones": ["(15 ÷ 3) × 8 × 1", "(15 - 3) × 3", "(15 + 5) × 2", "(15 × 2) + 10"], "correcta": "(15 ÷ 3) × 8 × 1", "tiempo": 20},
            {"numeros": "[6, 6, 6, 3]", "objetivo": 39, "opciones": ["(6 × 6) + 6 - 3", "(6 + 6) × 3 + 3", "(6 × 6) ÷ 3", "(6 - 3) × 12"], "correcta": "(6 × 6) + 6 - 3", "tiempo": 20},
            {"numeros": "[20, 5, 10, 2]", "objetivo": 9, "opciones": ["(20 ÷ 5) + 10 ÷ 2", "(20 - 10) ÷ 2", "(20 ÷ 5) × 2", "(20 + 10) ÷ 3"], "correcta": "(20 ÷ 5) + 10 ÷ 2", "tiempo": 20},
            {"numeros": "[8, 8, 4, 4]", "objetivo": 60, "opciones": ["(8 × 8) - 4", "(8 + 8) × 4 - 4", "(8 × 8) - 40", "(8 - 2) × 10"], "correcta": "(8 + 8) × 4 - 4", "tiempo": 20}
        ]

        # BANCO DE DATOS JUEGO 3: 15 NIVELES COMPROBADOS
        self.juego3_normales = [
            {"sucesion": "4,  9,  14,  19,  ¿__?", "respuesta": 24, "dif": "Normal"},
            {"sucesion": "3,  6,  12,  24,  ¿__?", "respuesta": 48, "dif": "Normal"},
            {"sucesion": "1,  4,  9,  16,  ¿__?", "respuesta": 25, "dif": "Normal"},
            {"sucesion": "5,  8,  11,  14,  ¿__?", "respuesta": 17, "dif": "Normal"},
            {"sucesion": "40,  35,  30,  25,  ¿__?", "respuesta": 20, "dif": "Normal"},
            {"sucesion": "2,  6,  10,  14,  ¿__?", "respuesta": 18, "dif": "Normal"},
            {"sucesion": "1,  3,  9,  27,  ¿__?", "respuesta": 81, "dif": "Normal"},
            {"sucesion": "50,  44,  38,  32,  ¿__?", "respuesta": 26, "dif": "Normal"}
        ]
        
        self.juego3_dificiles = [
            {"sucesion": "1,  1,  2,  3,  5,  8,  ¿__?", "respuesta": 13, "dif": "Complicadito 🔥"},
            {"sucesion": "2,  4,  5,  10,  11,  ¿__?", "respuesta": 22, "dif": "Complicadito 🔥"},
            {"sucesion": "1,  2,  4,  7,  11,  ¿__?", "respuesta": 16, "dif": "Complicadito 🔥"},
            {"sucesion": "3,  4,  6,  9,  13,  ¿__?", "respuesta": 18, "dif": "Complicadito 🔥"},
            {"sucesion": "2,  6,  12,  20,  30,  ¿__?", "respuesta": 42, "dif": "Complicadito 🔥"},
            {"sucesion": "27,  25,  21,  15,  ¿__?", "respuesta": 7, "dif": "Complicadito 🔥"},
            {"sucesion": "2,  3,  5,  7,  11,  ¿__?", "respuesta": 13, "dif": "Complicadito 🔥"}
        ]

    def generar_pregunta_juego1(self):
        a = random.randint(2, 9)
        b = random.randint(5, 25)
        return f"Calcula:\n{a}² + {b}", (a**2) + b

    def generar_partida_juego2(self):
        partida_normales = random.sample(self.juego2_normales, 3)
        partida_dificiles = random.sample(self.juego2_dificiles, 2)
        return partida_normales + partida_dificiles

    def generar_partida_juego3(self):
        partida_normales = random.sample(self.juego3_normales, 3)
        partida_dificiles = random.sample(self.juego3_dificiles, 2)
        return partida_normales + partida_dificiles


# =========================================================================
# FUNCIÓN PRINCIPAL DE LA INTERFAZ DE FLET
# =========================================================================
def main(page: ft.Page):
    page.title = "Plataforma de Olimpíadas Matemáticas UNI"
    page.window_width = 460
    page.window_height = 800
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    bd = BancoDatosJuegos()

    estado = {
        "juego_activo": 0, 
        "tiempo_reloj": 0,
        "token_reloj": 0, 
        
        "juego1_jugadores": [],
        "juego1_idx": 0,
        "juego1_pregunta_num": 1,
        "juego1_correcta": 0,
        "juego1_inicio_t": 0,
        
        "juego2_partida_actual": [],
        "juego2_nivel": 0,
        "juego2_puntos": 0,
        
        "juego3_partida_actual": [],
        "juego3_nivel": 0,
        "juego3_puntos": 0
    }

    # RELOJ UNIVERSAL EN CAJA SÓLIDA
    txt_reloj_label = ft.Text("", size=22, weight=ft.FontWeight.BOLD, color="red200")
    txt_reloj_universal = ft.Container(
        content=txt_reloj_label,
        bgcolor="#EE121212",
        padding=ft.Padding(15, 5, 15, 5),
        border_radius=10,
        border=ft.Border.all(1, "red900")
    )

    def parar_reloj_global():
        estado["tiempo_reloj"] = -1
        estado["token_reloj"] += 1 

    def arrancar_reloj_global(segundos, juego_num):
        parar_reloj_global() 
        estado["tiempo_reloj"] = segundos
        estado["juego_activo"] = juego_num
        txt_reloj_label.value = f"⏱️ ¡Apúrate! {segundos}s"
        page.update()
        page.run_task(ciclo_reloj_universal) 

    async def ciclo_reloj_universal():
        token_local = estado["token_reloj"] 
        while estado["tiempo_reloj"] > 0 and token_local == estado["token_reloj"]:
            await asyncio.sleep(1)
            if estado["tiempo_reloj"] > 0 and token_local == estado["token_reloj"]:
                estado["tiempo_reloj"] -= 1
                txt_reloj_label.value = f"⏱️ ¡Apúrate! {estado['tiempo_reloj']}s"
                page.update()
        if estado["tiempo_reloj"] == 0 and token_local == estado["token_reloj"]:
            if estado["juego_activo"] == 1:
                evaluar_respuesta_juego1(timeout=True)
            elif estado["juego_activo"] == 2:
                evaluar_juego2(opcion_seleccionada=None, timeout=True)
            elif estado["juego_activo"] == 3:
                evaluar_juego3(timeout=True)

    # --- FUNCIÓN AUXILIAR DE RENDERIZADO RESPONSIVA ---
    def renderizar_con_fondo(contenido_especifico, nombre_fondo="fondo_principal.png"):
        page.controls.clear()
        
        cuerpo_app = ft.Container(
            content=ft.Column(
                contenido_especifico, 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO
            ),
            width=430,
            height=750,
            padding=20,
            border_radius=15,
            image=ft.DecorationImage(
                src=f"/{nombre_fondo}",
                fit="cover"
            ),
        )
        
        layout_centrado = ft.Row(
            controls=[
                ft.Column(
                    controls=[cuerpo_app],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        page.add(layout_centrado)
        page.update()

    # =========================================================================
    # VISTA: MENÚ PRINCIPAL
    # =========================================================================
    def mostrar_menu_principal():
        parar_reloj_global()
        estado["juego_activo"] = 0
        
        contenido_menu = [
            ft.Container(height=10),
            ft.Container(
                content=ft.Text("🏛️ OLIMPÍADA MATEMÁTICA", size=24, weight=ft.FontWeight.BOLD, color="amber"),
                bgcolor="#CC121212",
                padding=15,
                border_radius=25,
                border=ft.Border.all(1.5, "amber")
            ),
            ft.Container(height=5),
            ft.Container(
                content=ft.Text("✨ ¡Disfruta de las matemáticas! ✨", size=13, italic=True, color="cyan200"),
                bgcolor="#AA000000",
                padding=ft.Padding(12, 4, 12, 4),
                border_radius=8
            ),
            ft.Container(height=15),

            # JUEGO 1 CARD
            ft.Container(
                content=ft.Column([
                    ft.Text("⚔️ 1. EL DUELO DE CRACKS", size=15, weight=ft.FontWeight.BOLD, color="blue200"),
                    ft.Image(src="/duelo.png", width=140, height=80, fit="contain", error_content=ft.Text("🖼️ [duelo.png]", color="grey")),
                    ft.ElevatedButton("Modo Grupal (15s)", on_click=lambda _: configurar_juego1(), bgcolor="blue800", color="white")
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor="#EE121212", padding=15, border_radius=15, border=ft.Border.all(1, "blue900"), width=340
            ),
            ft.Container(height=10),

            # JUEGO 2 CARD
            ft.Container(
                content=ft.Column([
                    ft.Text("⚡ 2. OPERACIÓN RELÁMPAGO", size=15, weight=ft.FontWeight.BOLD, color="green200"),
                    ft.Image(src="/relampago.png", width=140, height=80, fit="contain", error_content=ft.Text("🖼️ [relampago.png]", color="grey")),
                    ft.ElevatedButton("Desafío Dinámico", on_click=lambda _: mostrar_instrucciones_juego2(), bgcolor="green800", color="white")
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor="#EE121212", padding=15, border_radius=15, border=ft.Border.all(1, "green900"), width=340
            ),
            ft.Container(height=10),

            # JUEGO 3 CARD
            ft.Container(
                content=ft.Column([
                    ft.Text("🔮 3. ADIVINA EL PATRÓN", size=15, weight=ft.FontWeight.BOLD, color="purple200"),
                    ft.Image(src="/patron.png", width=140, height=80, fit="contain", error_content=ft.Text("🖼️ [patron.png]", color="grey")),
                    ft.ElevatedButton("Sucesiones Flash", on_click=lambda _: mostrar_instrucciones_juego3(), bgcolor="purple800", color="white")
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor="#EE121212", padding=15, border_radius=15, border=ft.Border.all(1, "purple900"), width=340
            ),
            ft.Container(height=15)
        ]
        
        renderizar_con_fondo(contenido_menu, "fondo_principal.png")

    # =========================================================================
    # LÓGICA: JUEGO 1 (EL DUELO DE CRACKS)
    # =========================================================================
    dd_cant = ft.Dropdown(width=180, value="2 Jugadores", options=[ft.dropdown.Option("2 Jugadores"), ft.dropdown.Option("3 Jugadores"), ft.dropdown.Option("4 Jugadores")])
    col_nombres = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    txt_j1_pregunta = ft.Text("", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, color="white")
    txt_j1_turno = ft.Text("", size=18, color="amber", weight=ft.FontWeight.BOLD)
    in_j1_res = ft.TextField(label="Tu respuesta", width=140, text_align=ft.TextAlign.CENTER, keyboard_type=ft.KeyboardType.NUMBER)

    def configurar_juego1():
        contenido_config = [
            ft.Container(height=15),
            ft.Container(
                content=ft.Text("⚔️ CONFIGURACIÓN DEL DUELO", size=18, weight=ft.FontWeight.BOLD, color="blue200"),
                bgcolor="#CC121212", padding=10, border_radius=12
            ),
            ft.Container(height=20),
            ft.Container(content=ft.Text("¿Cuántos cracks van al pizarrón?", color="white"), bgcolor="#AA000000", padding=5, border_radius=5),
            dd_cant,
            ft.Container(height=20),
            ft.ElevatedButton("Siguiente", on_click=pedir_nombres_juego1, bgcolor="blue800", color="white"),
            ft.TextButton("Volver al Menú", on_click=lambda _: mostrar_menu_principal(), style=ft.ButtonStyle(color="white"))
        ]
        renderizar_con_fondo(contenido_config, "fondo_juego1.png")

    def pedir_nombres_juego1(e):
        cant = int(dd_cant.value.split()[0])
        col_nombres.controls.clear()
        for i in range(cant):
            col_nombres.controls.append(ft.TextField(label=f"Nombre Crack {i+1}", width=240, value=f"Crack {i+1}"))
        
        contenido_nombres = [
            ft.Container(content=ft.Text("Ingresen sus Nombres", size=18, weight=ft.FontWeight.BOLD, color="white"), bgcolor="#CC000000", padding=8, border_radius=8),
            ft.Container(height=10),
            ft.Container(content=col_nombres, bgcolor="#EE121212", padding=15, border_radius=12),
            ft.Container(height=20),
            ft.ElevatedButton("Continuar", on_click=mostrar_instrucciones_juego1, bgcolor="green700", color="white")
        ]
        renderizar_con_fondo(contenido_nombres, "fondo_juego1.png")

    def mostrar_instrucciones_juego1(e):
        contenido_instrucciones = [
            ft.Container(height=20),
            ft.Container(content=ft.Text("⚔️ INSTRUCCIONES: DUELO", size=18, weight=ft.FontWeight.BOLD, color="blue200"), bgcolor="#CC000000", padding=10, border_radius=10),
            ft.Container(height=20),
            ft.Container(
                content=ft.Column([
                    ft.Text("• Los jugadores se turnarán para resolver ecuaciones mentalmente.", size=14, color="white"),
                    ft.Text("• Escribe solo el número entero de la respuesta correcta.", size=14, color="white"),
                    ft.Text("• Tienen exactamente 15 segundos por pregunta.", size=14, weight=ft.FontWeight.BOLD, color="red200"),
                    ft.Text("• Puntuación: +3 pts en menos de 5s, +1 pt después, y -1 pt si fallas o se agota el tiempo.", size=14, color="amber200"),
                ], spacing=10),
                bgcolor="#F2121212", padding=20, border_radius=15, border=ft.Border.all(1, "blue900")
            ),
            ft.Container(height=30),
            ft.ElevatedButton("¡Empezar Duelo!", on_click=arrancar_juego1, bgcolor="blue800", color="white", width=220),
            ft.TextButton("Cancelar", on_click=lambda _: mostrar_menu_principal(), style=ft.ButtonStyle(color="white"))
        ]
        renderizar_con_fondo(contenido_instrucciones, "fondo_juego1.png")

    def arrancar_juego1(e):
        estado["juego1_jugadores"] = []
        for tf in col_nombres.controls:
            estado["juego1_jugadores"].append({"nombre": tf.value.strip(), "puntos": 0})
        estado["juego1_idx"] = 0
        estado["juego1_pregunta_num"] = 1
        cargar_pregunta_juego1()

    def cargar_pregunta_juego1():
        parar_reloj_global()
        jugador = estado["juego1_jugadores"][estado["juego1_idx"]]
        txt, correcta = bd.generar_pregunta_juego1()
        estado["juego1_correcta"] = correcta
        
        txt_j1_turno.value = f"🎯 Turno de: {jugador['nombre']}"
        txt_j1_pregunta.value = f"Pregunta {estado['juego1_pregunta_num']} de 10:\n\n{txt}"
        in_j1_res.value = ""

        contenido_pregunta = [
            ft.Container(content=txt_j1_turno, bgcolor="#CC121212", padding=8, border_radius=8),
            ft.Container(content=txt_j1_pregunta, bgcolor="#EE121212", padding=25, border_radius=15, border=ft.Border.all(1, "grey800"), margin=15),
            txt_reloj_universal,
            ft.Container(height=10),
            ft.Row([in_j1_res], alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(height=15),
            ft.ElevatedButton("Enviar rápido", on_click=lambda _: procesar_click_juego1(), bgcolor="blue800", color="white"),
            ft.Container(height=15),
            ft.TextButton("🏳️ Salir del Juego", on_click=lambda _: mostrar_menu_principal(), style=ft.ButtonStyle(color="red400"))
        ]
        renderizar_con_fondo(contenido_pregunta, "fondo_juego1.png")
        estado["juego1_inicio_t"] = time.time()
        arrancar_reloj_global(15, juego_num=1)

    def procesar_click_juego1():
        parar_reloj_global()
        evaluar_respuesta_juego1(timeout=False)

    def evaluar_respuesta_juego1(timeout=False):
        jugador = estado["juego1_jugadores"][estado["juego1_idx"]]
        if not timeout:
            t_empleado = time.time() - estado["juego1_inicio_t"]
            try:
                ans = int(in_j1_res.value)
                if ans == estado["juego1_correcta"]:
                    if t_empleado <= 5: jugador["puntos"] += 3
                    else: jugador["puntos"] += 1
                else: jugador["puntos"] -= 1
            except ValueError:
                jugador["puntos"] -= 1
        else:
            jugador["puntos"] -= 1

        if estado["juego1_pregunta_num"] < 10:
            estado["juego1_pregunta_num"] += 1
            cargar_pregunta_juego1()
        else:
            if estado["juego1_idx"] < len(estado["juego1_jugadores"]) - 1:
                estado["juego1_idx"] += 1
                estado["juego1_pregunta_num"] = 1
                
                contenido_cambio = [
                    ft.Container(height=40),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("¡Ronda Completada!", size=22, color="green200", weight=ft.FontWeight.BOLD),
                            ft.Text("Entreguen el dispositivo al siguiente crack:", size=14, color="white"),
                            ft.Container(height=10),
                            ft.Text(f"👉 {estado['juego1_jugadores'][estado['juego1_idx']]['nombre']} 👈", size=20, color="amber", weight=ft.FontWeight.BOLD),
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        bgcolor="#EE121212", padding=25, border_radius=15
                    ),
                    ft.Container(height=30),
                    ft.ElevatedButton("¡Ya lo tengo, empezar!", on_click=lambda _: cargar_pregunta_juego1(), bgcolor="blue800", color="white")
                ]
                renderizar_con_fondo(contenido_cambio, "fondo_juego1.png")
            else:
                mostrar_podio_juego1()

    def mostrar_podio_juego1():
        ranking = sorted(estado["juego1_jugadores"], key=lambda x: x["puntos"], reverse=True)
        col_res = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)
        medallas = ["🥇", "🥈", "🥉", "👤"]
        for idx, j in enumerate(ranking):
            med = medallas[idx] if idx < len(medallas) else "👤"
            col_res.controls.append(
                ft.Container(content=ft.Row([ft.Text(f"{med} {j['nombre']}", size=16, weight=ft.FontWeight.BOLD, color="white"), ft.Text(f"{j['puntos']} Pts", size=16, color="cyan", weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN), width=300, bgcolor="#CC000000", padding=12, border_radius=8, border=ft.Border.all(1, "grey800"))
            )
        
        contenido_podio = [
            ft.Container(content=ft.Text("📊 CLASIFICACIÓN FINAL", size=20, weight=ft.FontWeight.BOLD, color="amber"), bgcolor="#CC121212", padding=12, border_radius=12),
            ft.Container(height=20),
            ft.Container(content=col_res, bgcolor="#EE121212", padding=15, border_radius=15),
            ft.Container(height=30),
            ft.ElevatedButton("Volver al Menú Principal", on_click=lambda _: mostrar_menu_principal(), bgcolor="red800", color="white")
        ]
        renderizar_con_fondo(contenido_podio, "fondo_juego1.png")


    # =========================================================================
    # LÓGICA: JUEGO 2 (OPERACIÓN RELÁMPAGO)
    # =========================================================================
    def mostrar_instrucciones_juego2():
        contenido_instrucciones = [
            ft.Container(height=20),
            ft.Container(content=ft.Text("⚡ INSTRUCCIONES: RELÁMPAGO", size=18, weight=ft.FontWeight.BOLD, color="green200"), bgcolor="#CC000000", padding=10, border_radius=10),
            ft.Container(height=20),
            ft.Container(
                content=ft.Column([
                    ft.Text("• Se te darán 4 números y una cifra objetivo en grande.", size=14, color="white"),
                    ft.Text("• Elige la combinación exacta para el resultado.", size=14, color="white"),
                    ft.Text("• El desafío consta de 5 niveles que suben de dificultad.", size=14, color="white"),
                    ft.Text("• Niveles 1-3: 15s | Niveles 4-5: 20s.", size=14, weight=ft.FontWeight.BOLD, color="amber200"),
                    ft.Text("• Acierto +20 | Error -5 | Quedarse sin tiempo -10.", size=14, color="cyan200")
                ], spacing=10),
                bgcolor="#F2121212", padding=20, border_radius=15, border=ft.Border.all(1, "green900")
            ),
            ft.Container(height=30),
            ft.ElevatedButton("¡Empezar Desafío!", on_click=lambda _: iniciar_juego2(), bgcolor="green700", color="white", width=220),
            ft.TextButton("Volver al Menú", on_click=lambda _: mostrar_menu_principal(), style=ft.ButtonStyle(color="white"))
        ]
        renderizar_con_fondo(contenido_instrucciones, "fondo_juego2.png")

    def iniciar_juego2():
        estado["juego2_nivel"] = 0
        estado["juego2_puntos"] = 0
        estado["juego2_partida_actual"] = bd.generar_partida_juego2()
        cargar_nivel_juego2()

    def cargar_nivel_juego2():
        parar_reloj_global()
        niv_data = estado["juego2_partida_actual"][estado["juego2_nivel"]]
        
        row_botones = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)
        for opcion in niv_data["opciones"]:
            row_botones.controls.append(
                ft.ElevatedButton(opcion, on_click=lambda e, opt=opcion: presionar_opcion_juego2(opt), width=280, bgcolor="#222222", color="white")
            )

        dif_tag = "Normal" if niv_data["tiempo"] == 15 else "Complicadito 🔥"

        contenido_nivel = [
            ft.Container(content=ft.Text("⚡ OPERACIÓN RELÁMPAGO", size=18, weight=ft.FontWeight.BOLD, color="green200"), bgcolor="#CC121212", padding=8, border_radius=8),
            ft.Container(content=ft.Text(f"Nivel {estado['juego2_nivel'] + 1} de 5 | Modo: {dif_tag}", size=13, color="white"), bgcolor="#AA000000", padding=5, border_radius=5),
            ft.Container(height=10),
            txt_reloj_universal,
            ft.Container(height=5),
            ft.Container(content=ft.Text("Combina números para llegar al objetivo:", color="white"), bgcolor="#AA000000", padding=5),
            ft.Container(content=ft.Text(f"Disponibles: {niv_data['numeros']}", size=15, weight=ft.FontWeight.BOLD, color="white"), bgcolor="#CC000000", padding=8, border_radius=8),
            ft.Container(
                content=ft.Text(str(niv_data["objetivo"]), size=44, weight=ft.FontWeight.BOLD, color="amber"),
                alignment=ft.alignment.Alignment(0, 0), height=80, bgcolor="#EE000000", border_radius=15, width=180, margin=10  # SOLUCIONADO: ft.alignment.Alignment nativo
            ),
            row_botones,
            ft.Container(height=15),
            ft.Container(content=ft.Text(f"Puntaje acumulado: {estado['juego2_puntos']} Pts", size=14, color="white"), bgcolor="#CC000000", padding=8, border_radius=8),
            ft.Container(height=10),
            ft.TextButton("🏳️ Salir", on_click=lambda _: mostrar_menu_principal(), style=ft.ButtonStyle(color="red400"))
        ]
        renderizar_con_fondo(contenido_nivel, "fondo_juego2.png")
        arrancar_reloj_global(niv_data["tiempo"], juego_num=2)

    def presionar_opcion_juego2(opt):
        parar_reloj_global()
        evaluar_juego2(opt, timeout=False)

    def evaluar_juego2(opcion_seleccionada, timeout=False):
        niv_data = estado["juego2_partida_actual"][estado["juego2_nivel"]]
        if not timeout:
            if opcion_seleccionada == niv_data["correcta"]: estado["juego2_puntos"] += 20
            else: estado["juego2_puntos"] -= 5
        else:
            estado["juego2_puntos"] -= 10 

        if estado["juego2_nivel"] < 4:
            estado["juego2_nivel"] += 1
            cargar_nivel_juego2()
        else:
            finalizar_juego_individual("⚡ Operación Relámpago", estado["juego2_puntos"], "fondo_juego2.png")


    # =========================================================================
    # LÓGICA: JUEGO 3 (ADIVINA EL PATRÓN)
    # =========================================================================
    def mostrar_instrucciones_juego3():
        contenido_instrucciones = [
            ft.Container(height=20),
            ft.Container(content=ft.Text("🔮 INSTRUCCIONES: PATRÓN", size=18, weight=ft.FontWeight.BOLD, color="purple200"), bgcolor="#CC000000", padding=10, border_radius=10),
            ft.Container(height=20),
            ft.Container(
                content=ft.Column([
                    ft.Text("• Estudia la sucesión numérica en pantalla.", size=14, color="white"),
                    ft.Text("• Deduce la regla lógica y calcula el número faltante ¿__?.", size=14, color="white"),
                    ft.Text("• Escribe tu respuesta y presiona verificar.", size=14, color="white"),
                    ft.Text("• Cuentas con solo 10 segundos por nivel.", size=14, weight=ft.FontWeight.BOLD, color="red300"),
                    ft.Text("• Acierto +20 | Fallo -5 | Tiempo -10.", size=14, color="cyan200")
                ], spacing=10),
                bgcolor="#F2121212", padding=20, border_radius=15, border=ft.Border.all(1, "purple900")
            ),
            ft.Container(height=30),
            ft.ElevatedButton("¡Empezar Desafío!", on_click=lambda _: iniciar_juego3(), bgcolor="purple800", color="white", width=220),
            ft.TextButton("Volver al Menú", on_click=lambda _: mostrar_menu_principal(), style=ft.ButtonStyle(color="white"))
        ]
        renderizar_con_fondo(contenido_instrucciones, "fondo_juego3.png")

    in_j3_res = ft.TextField(label="Número faltante", width=160, text_align=ft.TextAlign.CENTER, keyboard_type=ft.KeyboardType.NUMBER)

    def iniciar_juego3():
        estado["juego3_nivel"] = 0
        estado["juego3_puntos"] = 0
        estado["juego3_partida_actual"] = bd.generar_partida_juego3()
        cargar_nivel_juego3()

    def cargar_nivel_juego3():
        parar_reloj_global()
        niv_data = estado["juego3_partida_actual"][estado["juego3_nivel"]]
        in_j3_res.value = ""

        contenido_nivel = [
            ft.Container(content=ft.Text("🔮 ADIVINA EL PATRÓN", size=18, weight=ft.FontWeight.BOLD, color="purple200"), bgcolor="#CC121212", padding=8, border_radius=8),
            ft.Container(content=ft.Text(f"Nivel {estado['juego3_nivel'] + 1} de 5 | Dificultad: {niv_data['dif']}", size=13, color="white"), bgcolor="#AA000000", padding=5, border_radius=5),
            ft.Container(height=10),
            txt_reloj_universal,
            ft.Container(height=10),
            ft.Container(content=ft.Text("Descubre la regla de la sucesión:", color="white"), bgcolor="#AA000000", padding=5),
            ft.Container(
                content=ft.Text(niv_data["sucesion"], size=24, weight=ft.FontWeight.BOLD, color="cyan", text_align=ft.TextAlign.CENTER),
                padding=15, bgcolor="#EE121212", border_radius=12, width=360, alignment=ft.alignment.Alignment(0, 0), border=ft.Border.all(1, "grey800") # SOLUCIONADO: ft.alignment.Alignment nativo
            ),
            ft.Container(height=20),
            ft.Row([in_j3_res], alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(height=20),
            ft.ElevatedButton("Verificar Sucesión", on_click=lambda _: presionar_verificar_juego3(), bgcolor="purple800", color="white", width=200),
            ft.Container(height=15),
            ft.Container(content=ft.Text(f"Puntaje acumulado: {estado['juego3_puntos']} Pts", size=14, color="white"), bgcolor="#CC000000", padding=8, border_radius=8),
            ft.Container(height=10),
            ft.TextButton("🏳️ Salir", on_click=lambda _: mostrar_menu_principal(), style=ft.ButtonStyle(color="red400"))
        ]
        renderizar_con_fondo(contenido_nivel, "fondo_juego3.png")
        arrancar_reloj_global(10, juego_num=3) 

    def presionar_verificar_juego3():
        parar_reloj_global()
        evaluar_juego3(timeout=False)

    def evaluar_juego3(timeout=False):
        niv_data = estado["juego3_partida_actual"][estado["juego3_nivel"]]
        if not timeout:
            try:
                ans = int(in_j3_res.value)
                if ans == niv_data["respuesta"]: estado["juego3_puntos"] += 20
                else: estado["juego3_puntos"] -= 5
            except ValueError:
                estado["juego3_puntos"] -= 5
        else:
            estado["juego3_puntos"] -= 10 

        if estado["juego3_nivel"] < 4:
            estado["juego3_nivel"] += 1
            cargar_nivel_juego3()
        else:
            finalizar_juego_individual("🔮 Adivina el Patrón", estado["juego3_puntos"], "fondo_juego3.png")


    # =========================================================================
    # VIEW: PANTALLA GENERAL DE RESULTADOS INDIVIDUALES
    # =========================================================================
    def finalizar_juego_individual(nombre_juego, puntaje, nombre_fondo):
        parar_reloj_global()
        
        contenido_final = [
            ft.Container(height=30),
            ft.Container(content=ft.Text("🎉 ¡DESAFÍO COMPLETADO!", size=24, weight=ft.FontWeight.BOLD, color="amber"), bgcolor="#CC121212", padding=15, border_radius=20),
            ft.Container(height=20),
            ft.Container(
                content=ft.Column([
                    ft.Text(nombre_juego, size=18, weight=ft.FontWeight.BOLD, color="white"),
                    ft.Container(height=10),
                    ft.Text("Puntuación final:", size=15, color="white"),
                    ft.Text(f"{puntaje} PUNTOS", size=32, color="cyan", weight=ft.FontWeight.BOLD),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor="#EE121212", padding=30, border_radius=15, width=340
            ),
            ft.Container(height=40),
            ft.ElevatedButton("Volver al Menú Principal", on_click=lambda _: mostrar_menu_principal(), bgcolor="red800", color="white", width=240)
        ]
        renderizar_con_fondo(contenido_final, nombre_fondo)

    mostrar_menu_principal()

ft.app(target=main, assets_dir="assets")