import os

from marp_service import MarpService


def main():
    # --- Manually configure the output here ---
    # Specify the output type from MarpService.OutputType (PDF, HTML, PNG, PPTX)
    output_type = MarpService.OutputType.PDF
    # Specify the output filename
    output_filename = "slides.pdf"
    # -----------------------------------------

    # Setup paths
    slides_path = os.path.join(os.path.dirname(__file__), "slides.md")
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(project_root, "output")

    marp_service = MarpService(slides_path, output_dir)

    # Map OutputType enum to the correct service method
    generation_methods = {
        MarpService.OutputType.PDF: marp_service.generate_pdf,
        MarpService.OutputType.HTML: marp_service.generate_html,
        MarpService.OutputType.PNG: marp_service.generate_png,
        MarpService.OutputType.PPTX: marp_service.generate_pptx,
    }

    method_to_call = generation_methods.get(output_type)

    if method_to_call:
        # A simple check to ensure filename extension matches the type
        if not output_filename.lower().endswith(f".{output_type.value}"):
            print(
                f"Warning: Filename '{output_filename}' does not match the selected output type '{output_type.value}'."
            )

        method_to_call(output_filename)
    else:
        # This should not happen if output_type is from the enum
        print(f"Error: Internal error - unsupported output type '{output_type}'.")


if __name__ == "__main__":
    main()
