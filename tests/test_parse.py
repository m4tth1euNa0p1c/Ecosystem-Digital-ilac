import pytest
from src.fetch_parse import parse_and_display

def test_parse_and_display_plain_list(capsys):
    data = [
        {
            "name": "TestItem",
            "description": "Description here",
            "specifications": {"key1": "val1", "key2": 2},
            "tags": ["tagA", "tagB"]
        }
    ]
    parse_and_display(data)
    captured = capsys.readouterr().out

    assert "=== Objet #1 ===" in captured
    assert "Nom         : TestItem" in captured
    assert "Description : Description here" in captured
    assert "Spécifications :" in captured
    assert "- key1 : val1" in captured
    assert "- key2 : 2" in captured
    assert "Tags        : tagA, tagB" in captured

def test_parse_and_display_missing_fields(capsys):
    # If some keys are missing, get() returns None or empty list/dict
    data = [
        {"name": "OnlyName"}
    ]
    parse_and_display(data)
    captured = capsys.readouterr().out

    assert "Nom         : OnlyName" in captured
    assert "Description : None" in captured
    # Even if specifications is absent, it should not crash
    assert "Spécifications :" in captured
    # Tags should default to empty list
    assert "Tags        :" in captured
