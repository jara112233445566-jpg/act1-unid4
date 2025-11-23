import hashlib
from pathlib import Path


def compute_sha256(file_path: str) -> str:
    """Devuelve el hash SHA-256 de un archivo."""
    file = Path(file_path)
    if not file.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {file}")

    sha = hashlib.sha256()
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha.update(chunk)
    return sha.hexdigest()


def write_sha256(file_path: str, output_path: str) -> None:
    """Genera un archivo .sha256 con el hash del archivo."""
    hash_value = compute_sha256(file_path)
    with open(output_path, "w") as f:
        f.write(hash_value)


def verify_sha256(file_path: str, sha256_file: str) -> bool:
    """Verifica que el hash del archivo coincida con el almacenado."""
    expected = Path(sha256_file).read_text().strip()
    actual = compute_sha256(file_path)
    return actual == expected
