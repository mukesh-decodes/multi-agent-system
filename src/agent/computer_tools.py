
from pathlib import Path
from langchain_core.tools import tool

WORKSPACE = (Path(__file__).parent / "agent_workspace").resolve()


@tool
def list_files(relative_path: str = ".") -> list[str]:
    """List files and folders in the approved workspace.
    Use this to discover available files before reading them."""
    target = (WORKSPACE / relative_path).resolve()
    print("WORKSPACE:", WORKSPACE)
    print("Requested path:", repr(relative_path))
    print("Resolved target:", target)
    print("Exists:", target.exists())
    print("Is directory:", target.is_dir())
    if not target.is_relative_to(WORKSPACE):
        raise ValueError("Path outside approved workspace.")

    if not target.is_dir():
        raise ValueError("Directory not found.")

    return sorted(
        item.name + ("/" if item.is_dir() else "")
        for item in target.iterdir()
    )


@tool
def read_text_file(relative_path: str) -> str:
    """Read a UTF-8 text file from the approved workspace.
    Pass a relative path such as notes.txt."""
    target = (WORKSPACE / relative_path).resolve()

    if not target.is_relative_to(WORKSPACE):
        raise ValueError("Path outside approved workspace.")

    if not target.is_file():
        raise ValueError("File not found.")

    if target.stat().st_size > 200_000:
        raise ValueError("File exceeds the 200 KB limit.")

    return target.read_text(encoding="utf-8")
