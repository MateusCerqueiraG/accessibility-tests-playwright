"""A página bem construída não pode ter violações sérias ou críticas de WCAG."""
import allure
from axe_playwright_python.sync_playwright import Axe

SEVERE = {"serious", "critical"}


def test_accessible_page_has_no_severe_violations(page, page_url):
    page.goto(page_url("accessible.html"))
    results = Axe().run(page)

    violations = results.response["violations"]
    allure.attach(
        "\n".join(f"{v['impact']}: {v['id']}" for v in violations) or "nenhuma",
        name="violacoes-axe",
        attachment_type=allure.attachment_type.TEXT,
    )

    severe = [v["id"] for v in violations if v["impact"] in SEVERE]
    assert severe == [], f"Violações sérias/críticas de acessibilidade: {severe}"
