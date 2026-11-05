"""DEMONSTRAÇÃO (fora do CI) — mostra o gate REPROVANDO uma página problemática.

Rode com:
    pytest -m demo --browser chromium

O teste vai ficar VERMELHO de propósito: é a prova de que, ao encontrar
violações reais de acessibilidade, a suíte reprova. O CI normal não roda este
teste (está marcado `demo` e é excluído pelo `-m "not demo"`), para o badge
refletir apenas o gate de verdade sobre conteúdo conforme.
"""
import pytest
from axe_playwright_python.sync_playwright import Axe

SEVERE = {"serious", "critical"}


@pytest.mark.demo
def test_broken_page_is_rejected(page, page_url):
    page.goto(page_url("inaccessible.html"))
    results = Axe().run(page)

    severe = [f"{v['id']} ({v['impact']})" for v in results.response["violations"] if v["impact"] in SEVERE]
    assert not severe, f"Acessibilidade REPROVADA — violações sérias/críticas: {severe}"
