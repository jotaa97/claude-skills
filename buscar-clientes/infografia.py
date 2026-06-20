# -*- coding: utf-8 -*-
"""Genera una infografía PDF (estilo tarjeta vertical) que explica qué hace la skill en 5 pasos."""

import os
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
from reportlab.lib.colors import HexColor

W, H = 1000, 1500
MARGIN = 80
BG = HexColor("#E9F0F8")        # azul cielo suave (como la referencia)
BANDA = HexColor("#D9E6F4")
PILL = HexColor("#FFFFFF")
BORDE = HexColor("#D5E2F0")
INK = HexColor("#15263B")       # azul marino oscuro
MUT = HexColor("#5B6B7E")
ACC = HexColor("#D3FD50")       # acid-lime (marca)
ACC_INK = HexColor("#1C2A0A")   # texto sobre el lime

TITULO = "Tu scraper de IA\nque busca clientes\npotenciales"
SUBT = "Qué hace, en 5 pasos"
PASOS = [
    "Le dices qué vendes y a qué tipo de empresa quieres llegar.",
    "Busca en internet empresas reales que encajan contigo.",
    "Detecta las que tienen un motivo para comprarte ahora: acaban de abrir, contratan o salen en prensa.",
    "Te dice a quién escribir y te da su contacto.",
    "Te entrega el mensaje de LinkedIn listo. Tú revisas y envías.",
]
PIE = "José Javier Pedrero · Automatización e IA con Claude"
CTA = 'Comenta «CLIENTES» y te la paso'


def _wrap(c, txt, font, size, maxw):
    return simpleSplit(txt, font, size, maxw)


def construir(ruta):
    c = canvas.Canvas(ruta, pagesize=(W, H))
    # fondo
    c.setFillColor(BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(BANDA)
    c.rect(0, H - 360, W, 360, fill=1, stroke=0)

    # título
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 56)
    y = H - MARGIN - 56
    for ln in TITULO.split("\n"):
        c.drawString(MARGIN, y, ln)
        y -= 64
    # subtítulo
    c.setFillColor(MUT)
    c.setFont("Helvetica-Bold", 30)
    c.drawString(MARGIN, y - 4, SUBT)

    # cajas de pasos
    top = 1120
    alto, gap = 158, 24
    txt_size = 28
    for i, paso in enumerate(PASOS, 1):
        y0 = top - (i - 1) * (alto + gap)
        # pill
        c.setFillColor(PILL)
        c.setStrokeColor(BORDE)
        c.setLineWidth(1.2)
        c.roundRect(MARGIN, y0 - alto, W - 2 * MARGIN, alto, 28, fill=1, stroke=1)
        # número en círculo lime
        cx, cy = MARGIN + 62, y0 - alto / 2
        c.setFillColor(ACC)
        c.circle(cx, cy, 40, fill=1, stroke=0)
        c.setFillColor(ACC_INK)
        c.setFont("Helvetica-Bold", 40)
        c.drawCentredString(cx, cy - 14, str(i))
        # texto del paso (centrado vertical dentro de la caja)
        tx = MARGIN + 130
        maxw = (W - MARGIN) - tx - 24
        lineas = _wrap(c, paso, "Helvetica", txt_size, maxw)
        bloque = len(lineas) * (txt_size * 1.28)
        ty = cy + bloque / 2 - txt_size
        c.setFillColor(INK)
        c.setFont("Helvetica", txt_size)
        for ln in lineas:
            c.drawString(tx, ty, ln)
            ty -= txt_size * 1.28

    # pie
    c.setFillColor(ACC)
    c.roundRect(MARGIN, 96, W - 2 * MARGIN, 56, 28, fill=1, stroke=0)
    c.setFillColor(ACC_INK)
    c.setFont("Helvetica-Bold", 26)
    c.drawCentredString(W / 2, 113, CTA)
    c.setFillColor(MUT)
    c.setFont("Helvetica", 22)
    c.drawCentredString(W / 2, 56, PIE)

    c.showPage()
    c.save()


if __name__ == "__main__":
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "que-hace-la-skill.pdf")
    construir(ruta)
    print("PDF generado:", ruta)
