from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Add the title
        self.set_font("helvetica", "B", 40)
        self.cell(0, 50, "CS50 Shirtificate", align="C")
        self.ln(20)

def main():
    # Get user's name
    name = input("Name: ")

    # Create PDF
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Add the shirt image
    pdf.image("shirtificate.png", x=0, y=60, w=210)

    # Add user's name to the shirt
    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)  # White text
    pdf.cell(0, 213, f"{name} took CS50", align="C")

    # Save the PDF
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
