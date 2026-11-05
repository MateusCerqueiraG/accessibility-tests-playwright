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

Testes automatizados de **acessibilidade** com **Playwright** (dirigindo Chromium e Firefox) + **axe-core** (o motor de auditoria de WCAG usado pela indústria). Audita páginas, aponta violações por severidade e **reprova** quando há problema sério.

> 🎯 **Alvo sob teste:** duas páginas de demonstração no próprio repo — uma **acessível** (que deve passar) e uma **cheia de problemas** (que a auditoria deve detectar). As mesmas técnicas valem para qualquer página web real.

## ✅ O que a suíte verifica

| Teste | O que faz |
|:--|:--|
| ✅ **Página acessível** | audita `accessible.html` e exige **zero violações sérias/críticas** de WCAG |
| 🔎 **Detecção de problemas** | audita `inaccessible.html` e confirma que o axe **pega** as violações reais |

Violações detectadas na página-problema incluem: `image-alt` (imagem sem texto alternativo), `html-has-lang` (idioma não declarado), `document-title` (sem `<title>`), `link-name` (link sem texto), `color-contrast` (contraste baixo).

<div align="center">

**3 testes × 2 navegadores = 6 execuções &nbsp;·&nbsp; Chromium + Firefox &nbsp;·&nbsp; 100% verde**

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
├── accessible.html       # página bem construída (deve passar)
└── inaccessible.html     # página com problemas (a auditoria deve detectar)
tests/
├── test_accessible_page.py   # exige zero violações sérias/críticas
└── test_detects_issues.py    # confirma que o axe pega os problemas conhecidos
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
