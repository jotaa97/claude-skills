# claude-skills

Skills para Claude. Instálalas con la CLI de skills o copiándolas a tu Claude.

## 🧲 buscar-clientes

Convierte a Claude en tu **ayudante de prospección**: le dices qué vendes y a quién, **busca
empresas reales** que encajan (priorizando las que tienen una señal reciente de oportunidad), te
dice **a quién escribir** y su contacto, y te deja los **mensajes de LinkedIn ya escritos**. Tú solo
revisas y envías. Pensado para comerciales **sin conocimientos técnicos**: sin código, sin APIs.

- **Nunca inventa empresas:** usa la búsqueda web; si no puede buscar, te avisa y te pide una lista.
- **No repite:** guarda tu lista de "ya contactadas" (mejor en un Proyecto de Claude) y cada día te da nuevas.
- **Saca contacto** (email/teléfono de empresa) y propone al decisor + una búsqueda de LinkedIn.
- **RGPD-friendly:** emails de empresa, oferta relevante y opción de baja.

### Instalar

```bash
npx skills add <TU-USUARIO>/claude-skills@buscar-clientes
```

O manualmente: copia la carpeta `buscar-clientes/` a `~/.claude/skills/` (Claude Code), o súbela en
**Ajustes → Skills** de la app de Claude. **Activa la búsqueda web.**

### Usar

Di en Claude: **"búscame clientes nuevos"** (o "necesito leads", "prospección"…). La skill arranca,
te pregunta lo justo y te entrega la lista del día lista para enviar.

---

Hecho por José Javier Pedrero · Automatización e IA para pymes. Licencia MIT.
