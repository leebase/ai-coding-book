"""
Main entry point for ai-coding-book.

Created on 2026-03-15 by Anonymous.
"""

import argparse


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        prog="ai-coding-book",
        description="ai-coding-book - AI-agent project",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0",
    )
    parser.add_argument(
        "name",
        nargs="?",
        default="World",
        help="Name to greet (default: World)",
    )

    args = parser.parse_args()
    print(f"Hello from ai-coding-book, {args.name}!")


if __name__ == "__main__":
    main()
