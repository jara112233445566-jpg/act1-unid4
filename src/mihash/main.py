import argparse
from .core import compute_sha256, write_sha256, verify_sha256

VERSION = "1.0.0"

def main():
    parser = argparse.ArgumentParser(description="Herramienta SHA-256 (mihash)")
    parser.add_argument("--version", action="store_true", help="Mostrar versión")
    subparsers = parser.add_subparsers(dest="command")

    # mihash compute archivo
    p_compute = subparsers.add_parser("compute")
    p_compute.add_argument("archivo")

    # mihash write archivo archivo.sha256
    p_write = subparsers.add_parser("write")
    p_write.add_argument("archivo")
    p_write.add_argument("salida")

    # mihash verify archivo archivo.sha256
    p_verify = subparsers.add_parser("verify")
    p_verify.add_argument("archivo")
    p_verify.add_argument("sha256")

    args = parser.parse_args()

    if args.version:
        print(VERSION)
        return

    if args.command == "compute":
        print(compute_sha256(args.archivo))
    elif args.command == "write":
        write_sha256(args.archivo, args.salida)
        print("hash escrito en", args.salida)
    elif args.command == "verify":
        ok = verify_sha256(args.archivo, args.sha256)
        print("OK" if ok else "ERROR")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
