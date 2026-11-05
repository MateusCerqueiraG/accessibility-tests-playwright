"""Prova que a auditoria realmente pega problemas reais de acessibilidade."""
from axe_playwright_python.sync_playwright import Axe

# Regras WCAG que a página-problema deve, com certeza, violar.
EXPECTED_VIOLATIONS = {"image-alt", "html-has-lang", "document-title", "link-name"}


def test_audit_catches_known_wcag_issues(page, page_url):
    page.goto(page_url("inaccessible.html"))
    results = Axe().run(page)

    found = {v["id"] for v in results.response["violations"]}
    missing = EXPECTED_VIOLATIONS - found
    assert not missing, f"A auditoria não detectou estas violações esperadas: {missing}"


def test_bad_page_reports_violations(page, page_url):
    page.goto(page_url("inaccessible.html"))
    results = Axe().run(page)
    assert results.violations_count > 0
