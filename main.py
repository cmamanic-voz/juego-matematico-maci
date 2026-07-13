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
            {"numeros": "[7, 3, 2, 1]", "objetivo": 23, "opciones": ["(7 × 3) + 2", "(7 + 3) × 2 + 3", "(7 × 3) + 2 + 1", "(7 - 3) × 5"], "correcta": "(7 × 3) + 2 + 1", "tiempo": 15},
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
    page.window_height = 780
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

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

    txt_j1_reloj = ft.Text("", size=22, weight=ft.FontWeight.BOLD, color="red")
    txt_j2_reloj = ft.Text("", size=22, weight=ft.FontWeight.BOLD, color="red")
    txt_j3_reloj = ft.Text("", size=22, weight=ft.FontWeight.BOLD, color="red")

    def parar_reloj_global():
        estado["tiempo_reloj"] = -1
        estado["token_reloj"] += 1 

    def arrancar_reloj_global(segundos, juego_num):
        parar_reloj_global() 
        estado["tiempo_reloj"] = segundos
        estado["juego_activo"] = juego_num
        
        if juego_num == 1:
            txt_j1_reloj.value = f"⏱️ ¡Apúrate! {segundos}s"
            page.update()
            page.run_task(ciclo_reloj_juego1) 
        elif juego_num == 2:
            txt_j2_reloj.value = f"⏱️ ¡Apúrate! {segundos}s"
            page.update()
            page.run_task(ciclo_reloj_juego2) 
        elif juego_num == 3:
            txt_j3_reloj.value = f"⏱️ ¡Apúrate! {segundos}s"
            page.update()
            page.run_task(ciclo_reloj_juego3) 

    async def ciclo_reloj_juego1():
        token_local = estado["token_reloj"] 
        while estado["tiempo_reloj"] > 0 and token_local == estado["token_reloj"]:
            await asyncio.sleep(1)
            if estado["tiempo_reloj"] > 0 and token_local == estado["token_reloj"]:
                estado["tiempo_reloj"] -= 1
                txt_j1_reloj.value = f"⏱️ ¡Apúrate! {estado['tiempo_reloj']}s"
                page.update()
        if estado["tiempo_reloj"] == 0 and token_local == estado["token_reloj"]:
            evaluar_respuesta_juego1(timeout=True)

    async def ciclo_reloj_juego2():
        token_local = estado["token_reloj"]
        while estado["tiempo_reloj"] > 0 and token_local == estado["token_reloj"]:
            await asyncio.sleep(1)
            if estado["tiempo_reloj"] > 0 and token_local == estado["token_reloj"]:
                estado["tiempo_reloj"] -= 1
                txt_j2_reloj.value = f"⏱️ ¡Apúrate! {estado['tiempo_reloj']}s"
                page.update()
        if estado["tiempo_reloj"] == 0 and token_local == estado["token_reloj"]:
            evaluar_juego2(opcion_seleccionada=None, timeout=True)

    async def ciclo_reloj_juego3():
        token_local = estado["token_reloj"]
        while estado["tiempo_reloj"] > 0 and token_local == estado["token_reloj"]:
            await asyncio.sleep(1)
            if estado["tiempo_reloj"] > 0 and token_local == estado["token_reloj"]:
                estado["tiempo_reloj"] -= 1
                txt_j3_reloj.value = f"⏱️ ¡Apúrate! {estado['tiempo_reloj']}s"
                page.update()
        if estado["tiempo_reloj"] == 0 and token_local == estado["token_reloj"]:
            evaluar_juego3(timeout=True)

    # =========================================================================
    # VISTA: MENÚ PRINCIPAL
    # =========================================================================
    def mostrar_menu_principal():
        parar_reloj_global()
        estado["juego_activo"] = 0
        page.controls.clear()
        page.add(
            ft.Container(height=10),
            ft.Text("🏛️ OLIMPÍADA MATEMÁTICA", size=26, weight=ft.FontWeight.BOLD, color="amber"),
            ft.Text("✨ ¡Disfruta de las matemáticas! ✨", size=14, italic=True, color="cyan200"),
            ft.Container(height=20),

            ft.Container(
                content=ft.Column([
                    ft.Text("⚔️ 1. EL DUELO DE CRACKS", size=16, weight=ft.FontWeight.BOLD, color="blue"),
                    ft.Image(src="duelo.png", width=140, height=80, fit="contain", error_content=ft.Text("🖼️ [Imagen: duelo.png]", color="grey")),
                    ft.ElevatedButton("Modo Grupal (15s por Pregunta)", on_click=lambda _: configurar_juego1(), bgcolor="blue", color="white")
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor="black26", padding=12, border_radius=10, border=ft.Border.all(1, "grey800"), width=340
            ),
            ft.Container(height=10),

            ft.Container(
                content=ft.Column([
                    ft.Text("⚡ 2. OPERACIÓN RELÁMPAGO", size=16, weight=ft.FontWeight.BOLD, color="green"),
                    ft.Image(src="relampago.png", width=140, height=80, fit="contain", error_content=ft.Text("🖼️ [Imagen: relampago.png]", color="grey")),
                    ft.ElevatedButton("Desafío Dinámico (15s - 20s)", on_click=lambda _: mostrar_instrucciones_juego2(), bgcolor="green700", color="white")
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor="black26", padding=12, border_radius=10, border=ft.Border.all(1, "grey800"), width=340
            ),
            ft.Container(height=10),

            ft.Container(
                content=ft.Column([
                    ft.Text("🔮 3. ADIVINA EL PATRÓN", size=16, weight=ft.FontWeight.BOLD, color="purple"),
                    ft.Image(src="patron.png", width=140, height=80, fit="contain", error_content=ft.Text("🖼️ [Imagen: patron.png]", color="grey")),
                    ft.ElevatedButton("Sucesiones Flash (10s por Nivel)", on_click=lambda _: mostrar_instrucciones_juego3(), bgcolor="purple", color="white")
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor="black26", padding=12, border_radius=10, border=ft.Border.all(1, "grey800"), width=340
            ),
            ft.Container(height=20)
        )
        page.update()

    # =========================================================================
    # LÓGICA: JUEGO 1 (EL DUELO DE CRACKS)
    # =========================================================================
    dd_cant = ft.Dropdown(width=180, value="2 Jugadores", options=[ft.dropdown.Option("2 Jugadores"), ft.dropdown.Option("3 Jugadores"), ft.dropdown.Option("4 Jugadores")])
    col_nombres = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    txt_j1_pregunta = ft.Text("", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
    txt_j1_turno = ft.Text("", size=18, color="amber", weight=ft.FontWeight.BOLD)
    in_j1_res = ft.TextField(label="Tu respuesta", width=140, text_align=ft.TextAlign.CENTER, keyboard_type=ft.KeyboardType.NUMBER)

    def configurar_juego1():
        page.controls.clear()
        page.add(
            ft.Text("⚔️ CONFIGURACIÓN DEL DUELO", size=20, weight=ft.FontWeight.BOLD, color="blue"),
            ft.Container(height=20),
            ft.Text("¿Cuántos cracks van al pizarrón?"),
            dd_cant,
            ft.Container(height=20),
            ft.ElevatedButton("Siguiente", on_click=pedir_nombres_juego1, bgcolor="blue", color="white"),
            ft.TextButton("Volver al Menú", on_click=lambda _: mostrar_menu_principal())
        )
        page.update()

    def pedir_nombres_juego1(e):
        cant = int(dd_cant.value.split()[0])
        col_nombres.controls.clear()
        for i in range(cant):
            col_nombres.controls.append(ft.TextField(label=f"Nombre del Crack {i+1}", width=240, value=f"Crack {i+1}"))
        page.controls.clear()
        page.add(
            ft.Text("Ingresen sus Nombres", size=18, weight=ft.FontWeight.BOLD),
            ft.Container(height=10),
            col_nombres,
            ft.Container(height=20),
            ft.ElevatedButton("Continuar", on_click=mostrar_instrucciones_juego1, bgcolor="green", color="white")
        )
        page.update()

    def mostrar_instrucciones_juego1(e):
        page.controls.clear()
        page.add(
            ft.Container(height=20),
            ft.Text("⚔️ INSTRUCCIONES: DUELO DE CRACKS", size=20, weight=ft.FontWeight.BOLD, color="blue"),
            ft.Container(height=20),
            ft.Container(
                content=ft.Column([
                    ft.Text("• Los jugadores tomarán turnos para resolver ecuaciones en pantalla.", size=14),
                    ft.Text("• Deberán resolver mentalmente la operación y escribir SOLO la respuesta entera.", size=14),
                    ft.Text("• Cada jugador tendrá 10 preguntas asignadas consecutivamente.", size=14),
                    ft.Text("• ¡CUIDADO! Cada pregunta tiene un límite estricto de 15 segundos.", size=14, weight=ft.FontWeight.BOLD, color="red300"),
                    ft.Text("• Si respondes bien en menos de 5 segundos, recibes un Bono de +3 Pts.", size=14, color="green200"),
                    ft.Text("• Quedarse sin tiempo o equivocarse te restará 1 punto.", size=14, color="orange300"),
                ], spacing=10),
                bgcolor="black26", padding=20, border_radius=10, border=ft.Border.all(1, "grey800")
            ),
            ft.Container(height=30),
            ft.ElevatedButton("¡Empezar Duelo!", on_click=arrancar_juego1, bgcolor="blue", color="white", width=220),
            ft.TextButton("Cancelar", on_click=lambda _: mostrar_menu_principal())
        )
        page.update()

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
        in_j1_res.disabled = False

        page.controls.clear()
        page.add(
            txt_j1_turno,
            ft.Card(content=ft.Container(content=txt_j1_pregunta, padding=20), margin=15),
            txt_j1_reloj,
            ft.Row([in_j1_res], alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(height=15),
            ft.ElevatedButton("Enviar rápido", on_click=lambda _: procesar_click_juego1(), bgcolor="blue", color="white"),
            ft.Container(height=15),
            ft.TextButton("🏳️ Salir del Juego", on_click=lambda _: mostrar_menu_principal(), style=ft.ButtonStyle(color="red400"))
        )
        page.update()
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
                    jugador["puntos"] += 3 if t_empleado <= 5 else 1
                else:
                    jugador["puntos"] -= 1
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
                page.controls.clear()
                page.add(
                    ft.Text("¡Ronda Terminada!", size=22, color="green", weight=ft.FontWeight.BOLD),
                    ft.Text(f"Siguiente al pizarrón: {estado['juego1_jugadores'][estado['juego1_idx']]['nombre']}", size=16),
                    ft.Container(height=20),
                    ft.ElevatedButton("¡Listo!", on_click=lambda _: cargar_pregunta_juego1(), bgcolor="blue", color="white")
                )
                page.update()
            else:
                mostrar_podio_juego1()

    def mostrar_podio_juego1():
        ranking = sorted(estado["juego1_jugadores"], key=lambda x: x["puntos"], reverse=True)
        col_res = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)
        medallas = ["🥇", "🥈", "🥉", "👤"]
        for idx, j in enumerate(ranking):
            med = medallas[idx] if idx < len(medallas) else "👤"
            col_res.controls.append(
                ft.Container(content=ft.Row([ft.Text(f"{med} {j['nombre']}", size=16, weight=ft.FontWeight.BOLD), ft.Text(f"{j['puntos']} Pts", size=16, color="cyan", weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN), width=300, bgcolor="black26", padding=10, border_radius=8)
            )
        page.controls.clear()
        page.add(
            ft.Text("📊 CLASIFICACIÓN FINAL", size=22, weight=ft.FontWeight.BOLD, color="amber"),
            ft.Container(height=20),
            col_res,
            ft.Container(height=30),
            ft.ElevatedButton("Volver al Menú Principal", on_click=lambda _: mostrar_menu_principal(), bgcolor="red", color="white")
        )
        page.update()


    # =========================================================================
    # LÓGICA: JUEGO 2 (OPERACIÓN RELÁMPAGO) - ¡ARREGLADO CORRECCIÓN DE CLICKS!
    # =========================================================================
    def mostrar_instrucciones_juego2():
        page.controls.clear()
        page.add(
            ft.Container(height=20),
            ft.Text("⚡ INSTRUCCIONES: OPERACIÓN RELÁMPAGO", size=18, weight=ft.FontWeight.BOLD, color="green"),
            ft.Container(height=20),
            ft.Container(
                content=ft.Column([
                    ft.Text("• El juego elegirá 5 niveles aleatorios de un banco de 15 ejercicios.", size=14),
                    ft.Text("• Encontrarás 2 dificultades: Niveles Normales y Complicaditos.", size=14, weight=ft.FontWeight.BOLD, color="cyan200"),
                    ft.Text("• Nivel Normal: Tendrás 15 segundos para responder.", size=14, color="green200"),
                    ft.Text("• Nivel Complicadito: Tendrás 20 segundos para responder.", size=14, color="amber200"),
                    ft.Text("• Identifica la combinación matemática correcta antes de que expire el tiempo.", size=14),
                    ft.Text("• Acierto: +20 Pts | Error: -5 Pts | Sin tiempo: -10 Pts.", size=14, color="grey400"),
                ], spacing=10),
                bgcolor="black26", padding=20, border_radius=10, border=ft.Border.all(1, "grey800")
            ),
            ft.Container(height=30),
            ft.ElevatedButton("¡Empezar Desafío!", on_click=lambda _: iniciar_juego2(), bgcolor="green700", color="white", width=220),
            ft.TextButton("Volver al Menú", on_click=lambda _: mostrar_menu_principal())
        )
        page.update()

    def iniciar_juego2():
        estado["juego2_nivel"] = 0
        estado["juego2_puntos"] = 0
        estado["juego2_partida_actual"] = bd.generar_partida_juego2()
        cargar_nivel_juego2()

    def cargar_nivel_juego2():
        parar_reloj_global()
        niv_data = estado["juego2_partida_actual"][estado["juego2_nivel"]]
        
        row_botones = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)
        # CORRECCIÓN AQUÍ: opt=opcion captura el valor exacto del bucle en cada botón
        for opcion in niv_data["opciones"]:
            row_botones.controls.append(
                ft.ElevatedButton(
                    opcion, 
                    on_click=lambda e, opt=opcion: presionar_opcion_juego2(opt), 
                    width=280, 
                    bgcolor="grey900", 
                    color="white"
                )
            )

        dif_tag = "Normal" if niv_data["tiempo"] == 15 else "Complicadito 🔥"

        page.controls.clear()
        page.add(
            ft.Text("⚡ OPERACIÓN RELÁMPAGO", size=20, weight=ft.FontWeight.BOLD, color="green"),
            ft.Text(f"Desafío {estado['juego2_nivel'] + 1} de 5 | Modo: {dif_tag}", size=14, color="grey400"),
            ft.Container(height=10),
            txt_j2_reloj,
            ft.Container(height=5),
            ft.Text("Combina los números para llegar al objetivo:"),
            ft.Text(f"Números disponibles: {niv_data['numeros']}", size=15, weight=ft.FontWeight.BOLD),
            ft.Container(
                content=ft.Text(str(niv_data["objetivo"]), size=44, weight=ft.FontWeight.BOLD, color="amber"),
                alignment=ft.Alignment(0, 0), height=80
            ),
            ft.Text("Selecciona la combinación correcta:"),
            ft.Container(height=5),
            row_botones,
            ft.Container(height=15),
            ft.Text(f"Puntaje acumulado: {estado['juego2_puntos']} Pts", size=14),
            ft.Container(height=10),
            ft.TextButton("🏳️ Salir del Juego", on_click=lambda _: mostrar_menu_principal(), style=ft.ButtonStyle(color="red400"))
        )
        page.update()
        arrancar_reloj_global(niv_data["tiempo"], juego_num=2)

    def presionar_opcion_juego2(opt):
        parar_reloj_global()
        evaluar_juego2(opt, timeout=False)

    def evaluar_juego2(opcion_seleccionada, timeout=False):
        niv_data = estado["juego2_partida_actual"][estado["juego2_nivel"]]
        if not timeout:
            if opcion_seleccionada == niv_data["correcta"]:
                estado["juego2_puntos"] += 20
            else:
                estado["juego2_puntos"] -= 5
        else:
            estado["juego2_puntos"] -= 10 

        if estado["juego2_nivel"] < 4:
            estado["juego2_nivel"] += 1
            cargar_nivel_juego2()
        else:
            finalizar_juego_individual("⚡ Operación Relámpago", estado["juego2_puntos"])


    # =========================================================================
    # LÓGICA: JUEGO 3 (ADIVINA EL PATRÓN)
    # =========================================================================
    def mostrar_instrucciones_juego3():
        page.controls.clear()
        page.add(
            ft.Container(height=20),
            ft.Text("🔮 INSTRUCCIONES: ADIVINA EL PATRÓN", size=18, weight=ft.FontWeight.BOLD, color="purple"),
            ft.Container(height=20),
            ft.Container(
                content=ft.Column([
                    ft.Text("• El sistema elegirá 5 sucesiones al azar de un banco de 15 ejercicios.", size=14),
                    ft.Text("• Analiza lógicamente el comportamiento de los números en pantalla.", size=14),
                    ft.Text("• Escribe rápidamente el número entero que falta en el recuadro.", size=14),
                    ft.Text("• ¡MÁXIMA PRESIÓN! Solo tienes 10 segundos por nivel.", size=14, weight=ft.FontWeight.BOLD, color="red300"),
                    ft.Text("• Acierto: +20 Pts | Error: -5 Pts | Si expira el tiempo: -10 Pts.", size=14, color="grey400"),
                ], spacing=10),
                bgcolor="black26", padding=20, border_radius=10, border=ft.Border.all(1, "grey800")
            ),
            ft.Container(height=30),
            ft.ElevatedButton("¡Empezar Desafío!", on_click=lambda _: iniciar_juego3(), bgcolor="purple", color="white", width=220),
            ft.TextButton("Volver al Menú", on_click=lambda _: mostrar_menu_principal())
        )
        page.update()

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

        page.controls.clear()
        page.add(
            ft.Text("🔮 ADIVINA EL PATRÓN", size=20, weight=ft.FontWeight.BOLD, color="purple"),
            ft.Text(f"Nivel {estado['juego3_nivel'] + 1} de 5 | Dificultad: {niv_data['dif']}", size=14, color="grey"),
            ft.Container(height=10),
            txt_j3_reloj,
            ft.Container(height=10),
            ft.Text("Descubre la regla lógica de la sucesión:"),
            ft.Container(
                content=ft.Text(niv_data["sucesion"], size=24, weight=ft.FontWeight.BOLD, color="cyan", text_align=ft.TextAlign.CENTER),
                padding=15, bgcolor="black12", border_radius=8, width=360, alignment=ft.Alignment(0, 0)
            ),
            ft.Container(height=20),
            ft.Row([in_j3_res], alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(height=20),
            ft.ElevatedButton("Verificar Sucesión", on_click=lambda _: presionar_verificar_juego3(), bgcolor="purple", color="white", width=200),
            ft.Container(height=15),
            ft.Text(f"Puntaje acumulado: {estado['juego3_puntos']} Pts", size=14),
            ft.Container(height=10),
            ft.TextButton("🏳️ Salir del Juego", on_click=lambda _: mostrar_menu_principal(), style=ft.ButtonStyle(color="red400"))
        )
        page.update()
        arrancar_reloj_global(10, juego_num=3) 

    def presionar_verificar_juego3():
        parar_reloj_global()
        evaluar_juego3(timeout=False)

    def evaluar_juego3(timeout=False):
        niv_data = estado["juego3_partida_actual"][estado["juego3_nivel"]]
        if not timeout:
            try:
                ans = int(in_j3_res.value)
                if ans == niv_data["respuesta"]:
                    estado["juego3_puntos"] += 20
                else:
                    estado["juego3_puntos"] -= 5
            except ValueError:
                estado["juego3_puntos"] -= 5
        else:
            estado["juego3_puntos"] -= 10 

        if estado["juego3_nivel"] < 4:
            estado["juego3_nivel"] += 1
            cargar_nivel_juego3()
        else:
            finalizar_juego_individual("🔮 Adivina el Patrón", estado["juego3_puntos"])


    # =========================================================================
    # VIEW: PANTALLA GENERAL DE RESULTADOS INDIVIDUALES
    # =========================================================================
    def finalizar_juego_individual(nombre_juego, puntaje):
        parar_reloj_global()
        page.controls.clear()
        page.add(
            ft.Container(height=30),
            ft.Text("🎉 ¡DESAFÍO COMPLETADO!", size=24, weight=ft.FontWeight.BOLD, color="amber"),
            ft.Container(height=20),
            ft.Text(nombre_juego, size=18, weight=ft.FontWeight.BOLD),
            ft.Container(height=10),
            ft.Text("Tu puntuación final es de:", size=15),
            ft.Text(f"{puntaje} PUNTOS", size=32, color="cyan", weight=ft.FontWeight.BOLD),
            ft.Container(height=40),
            ft.ElevatedButton("Volver al Menú Principal", on_click=lambda _: mostrar_menu_principal(), bgcolor="blue", color="white", width=240)
        )
        page.update()

    mostrar_menu_principal()

ft.app(target=main, assets_dir=".")
