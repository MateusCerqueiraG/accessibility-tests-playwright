<div align="center">

# ♿ a11y-playwright

**Testes de Acessibilidade (WCAG)** &nbsp;·&nbsp; Playwright &nbsp;·&nbsp; axe-core &nbsp;·&nbsp; cross-browser

[![Accessibility Tests](https://github.com/MateusCerqueiraG/a11y-playwright/actions/workflows/a11y.yml/badge.svg)](https://github.com/MateusCerqueiraG/a11y-playwright/actions/workflows/a11y.yml)
&nbsp;
[![Relatório Allure](https://img.shields.io/badge/📊_Relatório-Allure_ao_vivo-5fd0e6?style=flat&labelColor=103a4e)](https://mateuscerqueirag.github.io/a11y-playwright/)

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?logo=playwright&logoColor=white)
![axe-core](https://img.shields.io/badge/axe--core-a11y-663399)
![WCAG](https://img.shields.io/badge/WCAG-2.1_AA-5A2D82)

</div>

---

Testes automatizados de **acessibilidade** com **Playwright** (dirigindo Chromium e Firefox) + **axe-core** (o motor de auditoria de WCAG usado pela indústria). É um **gate**: audita a página e **reprova (fica vermelho) se encontrar qualquer violação séria ou crítica**. Verde = acessível.

> 🎯 **Alvo sob teste:** páginas de demonstração no próprio repo. As mesmas técnicas valem para qualquer página web real.

## ✅ Como funciona o gate

| Situação | Resultado |
|:--|:--|
| Página **sem** violações sérias/críticas | ✅ **verde** (acessível) |
| Página **com** violações | ❌ **vermelho** (reprovado, lista as violações) |

Se alguém introduzir um problema de acessibilidade (imagem sem `alt`, link sem texto, contraste baixo…), a suíte **falha** — é esse o valor do gate.

### 🔴 Ver o gate reprovando (demo)
O repo traz uma página propositalmente problemática (`inaccessible.html`). Para ver o gate **ficar vermelho** de verdade:
```bash
pytest -m demo --browser chromium
# FAILED: image-alt (critical), link-name (serious), html-has-lang (serious)...
```
Essa demo fica **fora do CI** (marcador `demo`, excluído por `-m "not demo"`), para o badge refletir só o gate sobre conteúdo conforme.

<div align="center">

**Gate real × 2 navegadores (Chromium + Firefox) &nbsp;·&nbsp; verde = acessível**

</div>

## 🧰 Stack & práticas

- 🎭 **Playwright** — dirige Chromium e Firefox (mesma suíte, 2 engines via `--browser`)
- ♿ **axe-core** — auditoria WCAG padrão de mercado, integrada via `axe-playwright-python`
- 🎚️ **Gate por severidade** — só reprova em violações **sérias/críticas** (o filtro real de a11y)
- 📎 **Evidência** — a lista de violações é anexada ao relatório Allure
- ⚙️ **CI** — GitHub Actions roda cross-browser e publica o Allure

## 📁 Estrutura

```
pages/
├── accessible.html       # página conforme (o gate aprova)
└── inaccessible.html     # página com problemas (usada na demo do gate reprovando)
tests/
├── test_accessibility.py # o gate: reprova se houver violação séria/crítica
└── test_demo_gate.py     # demo (fora do CI): mostra o gate ficando vermelho
.github/workflows/a11y.yml
```

## ▶️ Como rodar localmente

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium firefox

pytest --browser chromium --browser firefox
```

## 📊 Relatório Allure

### 👉 **[mateuscerqueirag.github.io/a11y-playwright](https://mateuscerqueirag.github.io/a11y-playwright/)**

---

<div align="center">
<sub>Projeto de portfólio · foco em acessibilidade (WCAG) com Playwright + axe-core</sub>
</div>
