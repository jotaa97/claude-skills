# claude-skills

Skills para Claude, listas para usar. Cada una viene en **dos formas**:
- **Skill** (`SKILL.md`) → la instalas y Claude la usa solo cuando hace falta.
- **Prompt** (`PROMPT.md`) → si no quieres instalar nada, copias y pegas.

Sin código y sin APIs. Solo necesitas tu Claude con la **búsqueda web activada**.

> 🟢 **¿No sabes de informática?** Abre **[GUIA-usar-skill-en-claude.pdf](GUIA-usar-skill-en-claude.pdf)**:
> te explica en 2 minutos cómo abrir Claude y usar la herramienta (la forma más fácil es copiar y
> pegar el `PROMPT.md`, sin instalar nada).
>
> 📄 **Aún más fácil (para enviar a alguien):** en **[`pdf-para-clientes/`](pdf-para-clientes)** tienes
> un PDF «todo en uno» por herramienta — ya incluye los 3 pasos **y el texto listo para copiar**.
> Le envías ese único archivo y no tiene que tocar nada más.

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

## ✍️ crear-post-linkedin — `crear-post-linkedin/`

Escribe **posts de LinkedIn de alto alcance** usando la fórmula **A + B + C** (gancho + valor +
detonador), **sin engagement-bait**. Elige el tipo (autoridad, tutorial, caso real, building in
public, newsjacking, comercial), aporta valor real y atrae clientes. Nunca inventa cifras.

- **Instalar como skill:** `npx skills add jotaa97/claude-skills@crear-post-linkedin`
- **O copiar el prompt:** abre `crear-post-linkedin/PROMPT.md` y pégalo en Claude.

## 🧭 optimizar-perfil-linkedin — `optimizar-perfil-linkedin/`

Convierte tu perfil en una **página de ventas**: headline, «Acerca de» (estructura PAS), Destacado,
banner y comentario de bienvenida, con un **método con nombre propio**. El contenido atrae, el perfil
convierte.

- **Instalar como skill:** `npx skills add jotaa97/claude-skills@optimizar-perfil-linkedin`
- **O copiar el prompt:** abre `optimizar-perfil-linkedin/PROMPT.md` y pégalo en Claude.

## 📰 newsjacking-ia — `newsjacking-ia/`

Convierte una **novedad real de IA** en un post aplicado a pymes para ganar alcance por actualidad,
sin sensacionalismo. Traduce el titular a «qué significa para tu negocio» y «qué montaría yo con esto».

- **Instalar como skill:** `npx skills add jotaa97/claude-skills@newsjacking-ia`
- **O copiar el prompt:** abre `newsjacking-ia/PROMPT.md` y pégalo en Claude.

## 🎠 crear-carrusel-linkedin — `crear-carrusel-linkedin/`

Crea un **carrusel PDF** para LinkedIn (el formato de mayor alcance, ≈6x el texto solo) slide a
slide: portada-gancho, una idea por slide, resumen y CTA **sin engagement-bait**, más el post que lo
acompaña. Formato 1080×1350 (4:5).

- **Instalar como skill:** `npx skills add jotaa97/claude-skills@crear-carrusel-linkedin`
- **O copiar el prompt:** abre `crear-carrusel-linkedin/PROMPT.md` y pégalo en Claude.

---

## Instalar (resumen)

```bash
npx skills add jotaa97/claude-skills@buscar-clientes
npx skills add jotaa97/claude-skills@crear-presentaciones
npx skills add jotaa97/claude-skills@crear-post-linkedin
npx skills add jotaa97/claude-skills@optimizar-perfil-linkedin
npx skills add jotaa97/claude-skills@newsjacking-ia
npx skills add jotaa97/claude-skills@crear-carrusel-linkedin
```

O manualmente: copia la carpeta de la skill a `~/.claude/skills/` (Claude Code) o súbela en
**Ajustes → Skills** de la app de Claude. Activa siempre la **búsqueda web**.

---

Hecho por José Javier Pedrero · Automatización e IA para pymes. Licencia MIT.
