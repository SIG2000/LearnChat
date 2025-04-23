import pytest
import resolve_path

from chatbot.retrieval import Retrieval

retrieval = Retrieval()


def test_retrieve() -> None:
    retrieved = retrieval.retrieve("igeon")
    assert retrieved is not None
