from .cairo_python_bindings


def call_cairo_to_sierra_compiler(
    input_path: Path, output_path: Optional[Path] = None
) -> Optional[str]:
    return cairo_python_bindings.call_cairo_to_sierra_compiler(  # pyright: ignore
        str(input_path), str(output_path) if output_path else None
    )