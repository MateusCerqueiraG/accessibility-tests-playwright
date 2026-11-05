<div align="center">

# ♿ accessibility-tests-playwright

**Testes de Acessibilidade (WCAG)** &nbsp;·&nbsp; Playwright &nbsp;·&nbsp; axe-core &nbsp;·&nbsp; cross-browser

[![Accessibility Tests](https://github.com/MateusCerqueiraG/accessibility-tests-playwright/actions/workflows/a11y.yml/badge.svg)](https://github.com/MateusCerqueiraG/accessibility-tests-playwright/actions/workflows/a11y.yml)
&nbsp;
[![Relatório Allure](https://img.shields.io/badge/📊_Relatório-Allure_ao_vivo-5fd0e6?style=flat&labelColor=103a4e)](https://mateuscerqueirag.github.io/accessibility-tests-playwright/)

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?logo=playwright&logoColor=white)
![axe-core](https://img.shields.io/badge/axe--core-a11y-663399)
![WCAG](https://img.shields.io/badge/WCAG-2.1_AA-5A2D82)

</div>

---

Testes automatizados de **acessibilidade** com **Playwright** (dirigindo Chromium e Firefox) + **axe-core** (o motor de auditoria de WCAG usado pela indústria). É um **gate**: audita a página e **reprova (fica vermelho) se encontrar qualquer violação séria ou crítica**. Verde = acessível.

> 🎯 **Alvo sob teste:** páginas de demonstração no próprio repo. As mesmas técnicas valem para qualquer página web real.

## ✅ Como funciona o gate

A regra é simples e intuitiva: **achou violação séria/crítica → vermelho**. O CI roda **dois jobs** que mostram isso na prática:

| Job | Página | Resultado |
|:--|:--|:--|
| 🟢 **Gate de acessibilidade** | `accessible.html` (conforme) | ✅ **verde** — sem violações |
| 🔴 **Demo — página problemática** | `inaccessible.html` | ❌ **vermelho** — acha e lista as violações |

O job da demo roda com `continue-on-error` (**falha permitida**): ele fica vermelho de verdade — provando que o gate pega problema — mas **não derruba o badge geral**, que reflete o gate sobre conteúdo conforme. No [relatório Allure](https://mateuscerqueirag.github.io/accessibility-tests-playwright/) dá pra ver os dois: a página boa passando e a ruim reprovando com as violações (`image-alt`, `link-name`, `html-has-lang`, `color-contrast`…).

Rodar a demo localmente:
```bash
pytest -m demo --browser chromium   # FAILED: image-alt (critical), link-name (serious)...
```

<div align="center">

**2 jobs (conforme + problemática) × 2 navegadores &nbsp;·&nbsp; achou problema = vermelho**

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

### 👉 **[mateuscerqueirag.github.io/accessibility-tests-playwright](https://mateuscerqueirag.github.io/accessibility-tests-playwright/)**

---

<div align="center">
<sub>Projeto de portfólio · foco em acessibilidade (WCAG) com Playwright + axe-core</sub>
</div>
