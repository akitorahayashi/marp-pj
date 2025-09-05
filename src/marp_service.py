import os
import subprocess
from enum import Enum


class MarpService:
    class OutputType(Enum):
        PDF = "pdf"
        HTML = "html"
        PNG = "png"
        PPTX = "pptx"

    def __init__(self, slides_path, output_dir):
        self.slides_path = slides_path
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_pdf(self, output_filename="slides.pdf"):
        return self._generate(self.OutputType.PDF, output_filename)

    def generate_html(self, output_filename="slides.html"):
        return self._generate(self.OutputType.HTML, output_filename)

    def generate_png(self, output_filename="slides.png"):
        return self._generate(self.OutputType.PNG, output_filename)

    def generate_pptx(self, output_filename="slides.pptx"):
        return self._generate(self.OutputType.PPTX, output_filename)

    def _generate(self, output_type, output_filename):
        output_path = os.path.join(self.output_dir, output_filename)
        try:
            result = subprocess.run(
                ["marp", self.slides_path, "-o", output_path],
                check=True,
                capture_output=True,
                text=True,
            )
            print(f"{output_type.value.upper()} generation successful: {output_path}")
            print(result.stdout)
            return output_path
        except subprocess.CalledProcessError as e:
            print(f"{output_type.value.upper()} generation failed")
            print(e.stderr)
            raise e
