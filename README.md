# claude-skills

Skills para Claude, listas para usar. Cada una viene en **dos formas**:
- **Skill** (`SKILL.md`) → la instalas y Claude la usa solo cuando hace falta.
- **Prompt** (`PROMPT.md`) → si no quieres instalar nada, copias y pegas.

Sin código y sin APIs. Solo necesitas tu Claude con la **búsqueda web activada**.

---

## 🧲 buscar-clientes — `buscar-clientes/`

Tu **ayudante de prospección**: le dices qué vendes y a quién, **busca empresas reales** que
encajan (priorizando las que tienen una señal reciente de oportunidad), te dice **a quién escribir**
y su contacto, y te deja los **mensajes de LinkedIn ya escritos**. Tú revisas y envías. Nunca
inventa empresas; si no puede buscar, te avisa.

- **Instalar como skill:** `npx skills add jotaa97/claude-skills@buscar-clientes`
- **O copiar el prompt:** abre `buscar-clientes/PROMPT.md` y pégalo en Claude.

## 📊 crear-presentaciones — `crear-presentaciones/`

Convierte un tema en una **presentación diapositiva a diapositiva** (título, viñetas, qué decir y
qué visual poner), con un hilo que engancha y lista para PowerPoint, Google Slides o Canva. Una idea
por diapositiva, sin relleno, y sin inventarse datos.

- **Instalar como skill:** `npx skills add jotaa97/claude-skills@crear-presentaciones`
- **O copiar el prompt:** abre `crear-presentaciones/PROMPT.md` y pégalo en Claude.

---

## Instalar (resumen)

```bash
npx skills add jotaa97/claude-skills@buscar-clientes
npx skills add jotaa97/claude-skills@crear-presentaciones
```

O manualmente: copia la carpeta de la skill a `~/.claude/skills/` (Claude Code) o súbela en
**Ajustes → Skills** de la app de Claude. Activa siempre la **búsqueda web**.

---

Hecho por José Javier Pedrero · Automatización e IA para pymes. Licencia MIT.
