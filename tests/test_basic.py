from core.metrics import exact_match


def test_exact_match():
    assert exact_match("Paris", "Paris") == 1
    assert exact_match("Paris", "London") == 0
