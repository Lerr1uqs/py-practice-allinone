from rich.console import Console
console = Console()

try:
    raise Exception()
except Exception:
    console.print_exception(show_locals=True)