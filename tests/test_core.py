from src.mihash.core import compute_sha256, verify_sha256, write_sha256
from pathlib import Path


def test_sha256(tmp_path):
    f = tmp_path / "test.txt"
    f.write_text("hola")
    h = compute_sha256(f)
    assert len(h) == 64


def test_verify(tmp_path):
    f = tmp_path / "test.txt"
    f.write_text("mundo")
    sha_file = tmp_path / "test.txt.sha256"

    write_sha256(f, sha_file)
    assert verify_sha256(f, sha_file) is True
