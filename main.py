import flet as ft
import random
import time
import asyncio

# =========================================================================
# CLASE: BANCO DE DATOS DEL SISTEMA
# =========================================================================
class BancoDatosJuegos:
    def __init__(self):
        # BANCO DE DATOS FIXED: JUEGO 2 (OPERACIÓN RELÁMPAGO)
        self.juego2_niveles = [
            {
                "numeros": "[8, 4, 2, 6]",
                "objetivo": 10,
                "opciones": ["(8 ÷ 4) + 2 + 6", "(8 - 4) × 2 + 6", "(8 × 4) ÷ 2 - 6", "(8 + 4) - 2 - 6"],
                "correcta": "(8 ÷ 4) + 2 + 6"
            },
            {
                "numeros": "[5, 3, 4, 2]",
                "objetivo": 32,
                "opciones": ["(5 × 3) + 4 - 2", "(5 + 3) × (4 ÷ 2)", "(5 + 3) × 4", "(5 - 3) × 4 × 2"],
                "correcta": "(5 + 3) × 4" 
            },
            {
                "numeros": "[9, 3, 5, 2]",
                "objetivo": 20,
                "opciones": ["(9 × 3) - 5 - 2", "(9 ÷ 3) × 5 + 5", "(9 + 3) × 2 - 4", "(9 ÷ 3) × 5 + 5"],
                "correcta": "(9 ÷ 3) × 5 + 5"
            },
            {
                "numeros": "[12, 4, 6, 2]",
                "objetivo": 48,
                "opciones": ["(12 - 4) × 6", "(12 ÷ 4) × 6 × 2", "(12 + 4) × (6 - 2)", "(12 × 4) ÷ 2"],
                "correcta": "(12 - 4) × 6"
            },
            {
                "numeros": "[7, 5, 4, 2]",
                "objetivo": 39,
                "opciones": ["(7 × 5) + 4,0", "(7 × 5) + 4 + 2", "(7 × 5) + 4 - 2", "(7 + 5) × 4 - 2"],
                "correcta": "(7 × 5) + 4 - 2"
            }
        ]

        # BANCO DE DATOS FIXED: JUEGO 3 (ADIVINA EL PATRÓN)
        self.juego3_niveles = [
            {"sucesion": "4,  9,  14,  19,  ¿__?", "respuesta": 24},
            {"sucesion": "3,  6,  12,  24,  ¿__?", "respuesta": 48},
            {"sucesion": "1,  4,  9,  16,  ¿__?", "respuesta": 25},
            {"sucesion": "1,  1,  2,  3,  5,  8,  ¿__?", "respuesta": 13},
            {"sucesion": "2,  4,  5,  10,  11,  ¿__?", "respuesta": 22}
        ]

    def generar_pregunta_juego1(self):
        a = random.randint(2, 9)
        b = random.randint(5, 25)
        return f"Calcula:\n{a}² + {b}", (a**2) + b


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

    # DICCIONARIO DE ESTADO GLOBAL
    estado = {
        "juego_activo": 0, 
        "tiempo_reloj": 0,
        "token_reloj": 0, 
        
        "juego1_jugadores": [],
        "juego1_idx": 0,
        "juego1_pregunta_num": 1,
        "juego1_correcta": 0,
        "juego1_inicio_t": 0,
        
        "juego2_nivel": 0,
        "juego2_puntos": 0,
        
        "juego3_nivel": 0,
        "juego3_puntos": 0
    }

    # TEXTOS DE RELOJ REUTILIZABLES
    txt_j1_reloj = ft.Text("", size=22, weight=ft.FontWeight.BOLD, color="red")
    txt_j2_reloj = ft.Text("", size=22, weight=ft.FontWeight.BOLD, color="red")
    txt_j3_reloj = ft.Text("", size=22, weight=ft.FontWeight.BOLD, color="red")

    # =========================================================================
    # MOTOR ASÍNCRONO PERFECTO
    # =========================================================================
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
            ft.Text("Suite del Proyecto Final - Edición Adrenalina", size=13, italic=True, color="grey400"),
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
                    ft.ElevatedButton("Desafío Veloz (10s por Nivel)", on_click=lambda _: mostrar_instrucciones_juego2(), bgcolor="green700", color="white")
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
            # BOTÓN SALIR ADICIONADO
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
    # LÓGICA: JUEGO 2 (OPERACIÓN RELÁMPAGO)
    # =========================================================================
    def mostrar_instrucciones_juego2():
        page.controls.clear()
        page.add(
            ft.Container(height=20),
            ft.Text("⚡ INSTRUCCIONES: OPERACIÓN RELÁMPAGO", size=18, weight=ft.FontWeight.BOLD, color="green"),
            ft.Container(height=20),
            ft.Container(
                content=ft.Column([
                    ft.Text("• Verás un grupo de 4 números y un gran OBJETIVO en color ámbar.", size=14),
                    ft.Text("• Abajo aparecerán 4 botones con diferentes combinaciones matemáticas.", size=14),
                    ft.Text("• Debes identificar la opción que use correctamente los signos y paréntesis para llegar exactamente al número objetivo.", size=14),
                    ft.Text("• ¡ADRENALINA! Tienes solo 10 segundos por nivel.", size=14, weight=ft.FontWeight.BOLD, color="red300"),
                    ft.Text("• Acierto: +20 Pts | Error: -5 Pts | Si el tiempo llega a cero: -10 Pts y saltas de nivel.", size=14, color="grey400"),
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
        cargar_nivel_juego2()

    def cargar_nivel_juego2():
        parar_reloj_global()
        niv_data = bd.juego2_niveles[estado["juego2_nivel"]]
        
        row_botones = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)
        for opcion in niv_data["opciones"]:
            row_botones.controls.append(
                ft.ElevatedButton(opcion, on_click=lambda e, opt=opcion: presionar_opcion_juego2(opt), width=280, bgcolor="grey900", color="white")
            )

        page.controls.clear()
        page.add(
            ft.Text("⚡ OPERACIÓN RELÁMPAGO", size=20, weight=ft.FontWeight.BOLD, color="green"),
            ft.Text(f"Nivel {estado['juego2_nivel'] + 1} de 5", size=14, color="grey"),
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
            # BOTÓN SALIR ADICIONADO
            ft.TextButton("🏳️ Salir del Juego", on_click=lambda _: mostrar_menu_principal(), style=ft.ButtonStyle(color="red400"))
        )
        page.update()
        arrancar_reloj_global(10, juego_num=2)

    def presionar_opcion_juego2(opt):
        parar_reloj_global()
        evaluar_juego2(opcion_seleccionada=opt, timeout=False)

    def evaluar_juego2(opcion_seleccionada, timeout=False):
        niv_data = bd.juego2_niveles[estado["juego2_nivel"]]
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
                    ft.Text("• Verás una sucesión o secuencia de números en la pantalla.", size=14),
                    ft.Text("• Analiza lógicamente el comportamiento (¿se suma?, ¿se multiplica?, ¿son potencias?, ¿Fibonacci?).", size=14),
                    ft.Text("• Descubre la regla y escribe rápidamente el número entero que falta en el recuadro.", size=14),
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
        cargar_nivel_juego3()

    def cargar_nivel_juego3():
        parar_reloj_global()
        niv_data = bd.juego3_niveles[estado["juego3_nivel"]]
        in_j3_res.value = ""

        page.controls.clear()
        page.add(
            ft.Text("🔮 ADIVINA EL PATRÓN", size=20, weight=ft.FontWeight.BOLD, color="purple"),
            ft.Text(f"Nivel {estado['juego3_nivel'] + 1} de 5", size=14, color="grey"),
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
            # BOTÓN SALIR ADICIONADO
            ft.TextButton("🏳️ Salir del Juego", on_click=lambda _: mostrar_menu_principal(), style=ft.ButtonStyle(color="red400"))
        )
        page.update()
        arrancar_reloj_global(10, juego_num=3) 

    def presionar_verificar_juego3():
        parar_reloj_global()
        evaluar_juego3(timeout=False)

    def evaluar_juego3(timeout=False):
        niv_data = bd.juego3_niveles[estado["juego3_nivel"]]
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
