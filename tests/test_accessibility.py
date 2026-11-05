"""Gate de acessibilidade (WCAG).

A página é REPROVADA (teste vermelho) se tiver qualquer violação de impacto
sério ou crítico. Verde = acessível. É assim que o gate protege a aplicação:
se alguém introduzir um problema de acessibilidade, a suíte falha.
"""
import allure
from axe_playwright_python.sync_playwright import Axe

SEVERE = {"serious", "critical"}


def test_page_has_no_serious_violations(page, page_url):
    page.goto(page_url("accessible.html"))
    results = Axe().run(page)

    violations = results.response["violations"]
    allure.attach(
        "\n".join(f"{v['impact']}: {v['id']}" for v in violations) or "nenhuma violação",
        name="auditoria-axe",
        attachment_type=allure.attachment_type.TEXT,
    )

    severe = [f"{v['id']} ({v['impact']})" for v in violations if v["impact"] in SEVERE]
    assert not severe, f"Acessibilidade REPROVADA — violações sérias/críticas: {severe}"
