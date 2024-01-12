# resume_generator_gui.py
from fpdf import FPDF
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ResumeGenerator:
    def __init__(self, name, email, phone, summary, experience, education, accomplishments):
        self.name = name
        self.email = email
        self.phone = phone
        self.summary = summary
        self.experience = experience
        self.education = education
        self.accomplishments = accomplishments

    def generate_pdf(self, output_filename='resume.pdf'):
        pdf = FPDF()
        pdf.add_page()

        # Set font
        pdf.set_font("Times", size=10)

        # Add name to the top left
        pdf.cell(0, 10, txt=f"{self.name}", ln=True)

        # Add phone to the top right in blue
        pdf.set_xy(150, pdf.get_y() - 10)  # Move up slightly
        pdf.cell(0, 10, txt=f"Phone: {self.phone}", ln=True)

        # Add email to the top right, below the phone, in blue
        pdf.set_xy(150, pdf.get_y() - 13)  # Move up slightly
        pdf.cell(0, 10, txt=f"Email: {self.email}", ln=True)

        # Add content to the PDF
        pdf.ln(10)

        pdf.cell(200, 10, txt="Summary:", ln=True)
        pdf.multi_cell(0, 5, txt=self.summary)
        pdf.ln(10)

        pdf.cell(200, 10, txt="Experience:", ln=True)
        for exp in self.experience:
            pdf.multi_cell(0, 5, txt=exp)
            pdf.ln(5)  # Add some space between experience entries
        pdf.ln(10)

        pdf.cell(200, 10, txt="Education:", ln=True)
        for edu in self.education:
            pdf.multi_cell(0, 5, txt=edu)
            pdf.ln(5)  # Add some space between education entries
        pdf.ln(10)

        pdf.cell(200, 10, txt="Accomplishments:", ln=True)
        for acc in self.accomplishments:
            pdf.multi_cell(0, 5, txt=acc)
            pdf.ln(5)  # Add some space between accomplishment entries
        pdf.ln(10)
        
        # Save the PDF to the specified file
        pdf.output(output_filename)

def generate_resume():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    summary = summary_entry.get("1.0", tk.END).strip()
    experience = experience_entry.get("1.0", tk.END).strip().split('\n')
    education = education_entry.get("1.0", tk.END).strip().split('\n')
    accomplishments = accomplishments_entry.get("1.0", tk.END).strip().split('\n')

    if not name or not email or not phone or not summary or not experience or not education or not accomplishments:
        messagebox.showwarning("Missing Information", "Please fill out all fields.")
        return

    resume_generator = ResumeGenerator(name, email, phone, summary, experience, education, accomplishments)
    resume_generator.generate_pdf()
    messagebox.showinfo("Resume Generated", "Resume generated successfully. Check 'resume.pdf'.")

# Create the main window
root = tk.Tk()
root.title("Resume Generator")

# Create and place widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Name
ttk.Label(frame, text="Name:").grid(row=0, column=0, sticky=tk.W)
name_entry = ttk.Entry(frame)
name_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

# Phone
ttk.Label(frame, text="Phone:").grid(row=1, column=0, sticky=tk.W)
phone_entry = ttk.Entry(frame)
phone_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

# Email
ttk.Label(frame, text="Email:").grid(row=2, column=0, sticky=tk.W)
email_entry = ttk.Entry(frame)
email_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

# Summary
ttk.Label(frame, text="Summary:").grid(row=3, column=0, sticky=tk.W)
summary_entry = tk.Text(frame, height=5, width=40)
summary_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

# Experience
ttk.Label(frame, text="Experience:").grid(row=4, column=0, sticky=tk.W)
experience_entry = tk.Text(frame, height=5, width=40)
experience_entry.grid(row=4, column=1, sticky=(tk.W, tk.E))

# Education
ttk.Label(frame, text="Education:").grid(row=5, column=0, sticky=tk.W)
education_entry = tk.Text(frame, height=5, width=40)
education_entry.grid(row=5, column=1, sticky=(tk.W, tk.E))

# Accomplishments
ttk.Label(frame, text="Accomplishments:").grid(row=6, column=0, sticky=tk.W)
accomplishments_entry = tk.Text(frame, height=5, width=40)
accomplishments_entry.grid(row=6, column=1, sticky=(tk.W, tk.E))

# Generate Resume Button
generate_button = ttk.Button(frame, text="Generate Resume", command=generate_resume)
generate_button.grid(row=7, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
