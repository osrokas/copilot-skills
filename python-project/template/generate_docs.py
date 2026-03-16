"""
generate_docs.py - Generates a PDF description of the project.

Usage:
    python generate_docs.py "<Project Name>" "<Project Description>"

The generated PDF will be saved to docs/project_description.pdf.
"""

import os
import sys
from fpdf import FPDF


def generate_project_pdf(project_name: str, project_description: str) -> None:
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Helvetica", style="B", size=24)
    pdf.cell(0, 15, project_name, new_x="LMARGIN", new_y="NEXT", align="C")

    pdf.ln(5)

    # Section: About
    pdf.set_font("Helvetica", style="B", size=14)
    pdf.cell(0, 10, "About", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", size=12)
    pdf.multi_cell(0, 8, project_description)

    pdf.ln(5)

    # Section: Project Structure
    pdf.set_font("Helvetica", style="B", size=14)
    pdf.cell(0, 10, "Project Structure", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Courier", size=11)
    structure = (
        f"{project_name}/\n"
        "|-- docs/\n"
        "|   |-- project_description.pdf\n"
        "|-- notebooks/\n"
        "|-- src/\n"
        "|-- .gitignore\n"
        "|-- generate_docs.py\n"
        "|-- requirements.txt\n"
        "|-- README.md\n"
    )
    pdf.multi_cell(0, 7, structure)

    pdf.ln(5)

    # Section: Getting Started
    pdf.set_font("Helvetica", style="B", size=14)
    pdf.cell(0, 10, "Getting Started", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", size=12)
    steps = (
        "1. Clone the repository.\n"
        "2. Create and activate a virtual environment:\n"
        "       python -m venv .venv\n"
        "       source .venv/bin/activate  # macOS/Linux\n"
        "       .venv\\Scripts\\activate     # Windows\n"
        "3. Install dependencies:\n"
        "       pip install -r requirements.txt\n"
        "4. Start developing in the src/ directory.\n"
    )
    pdf.multi_cell(0, 8, steps)

    output_path = "docs/project_description.pdf"
    os.makedirs("docs", exist_ok=True)
    pdf.output(output_path)
    print(f"PDF generated: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_docs.py \"<Project Name>\" \"<Project Description>\"")
        sys.exit(1)

    name = sys.argv[1]
    description = sys.argv[2]
    generate_project_pdf(name, description)
