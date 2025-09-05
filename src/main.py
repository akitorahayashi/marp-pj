import os
import sys

from marp_service import MarpService


def main():
    # --- Manually configure the output here ---
    # Specify the output type from MarpService.OutputType (PDF, HTML, PNG, PPTX)
    output_type = MarpService.OutputType.HTML
    # Specify the output filename
    output_filename = "slides.html"
    # Specify a theme (optional, e.g., "src/theme.css")
    theme_path = "src/theme.css"
    # -----------------------------------------

    # Setup paths
    slides_path = os.path.join(os.path.dirname(__file__), "slides.md")
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(project_root, "output")

    # Command-line argument determines the action
    command = "generate"  # Default action
    if len(sys.argv) > 1:
        command = sys.argv[1]

    if command == "preview":
        # For preview, output_dir is not needed
        marp_service = MarpService(slides_path)
        print(
            "👀 Starting preview server at http://localhost:8080 (Press Ctrl+C to stop)"
        )
        marp_service.preview(server=True, watch=True)

    elif command == "generate":
        marp_service = MarpService(slides_path, output_dir)
        generation_methods = {
            MarpService.OutputType.PDF: marp_service.generate_pdf,
            MarpService.OutputType.HTML: marp_service.generate_html,
            MarpService.OutputType.PNG: marp_service.generate_png,
            MarpService.OutputType.PPTX: marp_service.generate_pptx,
        }

        method_to_call = generation_methods.get(output_type)

        if method_to_call:
            if not output_filename.lower().endswith(f".{output_type.value}"):
                print(
                    f"Warning: Filename '{output_filename}' does not match the selected output type '{output_type.value}'."
                )

            print(f"Generating {output_type.value} file...")
            method_to_call(output_filename, theme=theme_path)
        else:
            print(f"Error: Internal error - unsupported output type '{output_type}'.")
    else:
        print(f"Unknown command: {command}")
        print("Usage: python src/main.py [generate|preview]")


if __name__ == "__main__":
    main()
