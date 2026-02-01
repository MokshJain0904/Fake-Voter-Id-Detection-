import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from image_analysis import analyze_image
from ocr_module import ocr_analysis

class VoterIDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fake Voter ID Detection System")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        self.image_path = None

        # Title
        title = tk.Label(root, text="Fake Voter ID Detection",
                         font=("Arial", 20, "bold"), fg="darkblue")
        title.pack(pady=10)

        # Frame
        frame = tk.Frame(root)
        frame.pack(pady=10)

        # Image Label
        self.image_label = tk.Label(frame, text="No Image Selected",
                                    width=40, height=15, relief="solid")
        self.image_label.grid(row=0, column=0, padx=20)

        # Buttons Frame
        btn_frame = tk.Frame(frame)
        btn_frame.grid(row=0, column=1, padx=20)

        upload_btn = tk.Button(btn_frame, text="Upload Voter ID",
                               width=20, command=self.upload_image)
        upload_btn.pack(pady=10)

        verify_btn = tk.Button(btn_frame, text="Verify",
                               width=20, command=self.verify_id)
        verify_btn.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(root, text="Result: Not Verified",
                                     font=("Arial", 14))
        self.result_label.pack(pady=20)

    def upload_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
        )
        if file_path:
            self.image_path = file_path
            img = Image.open(file_path)
            img = img.resize((250, 160))
            img = ImageTk.PhotoImage(img)
            self.image_label.configure(image=img, text="")
            self.image_label.image = img

    def verify_id(self):
        if not self.image_path:
            messagebox.showwarning("Warning", "Please upload an image first")
            return

        analysis, _ = analyze_image(self.image_path)
        ocr = ocr_analysis(self.image_path)

        blur = analysis["blur_score"]
        edge = analysis["edge_score"]
        epic = ocr["epic_number"]
        epic_valid = ocr["epic_valid"]

        result_text = (
            f"Blur: {blur}\n"
            f"Edge: {edge}\n"
            f"EPIC: {epic}\n"
            f"EPIC Valid: {epic_valid}"
        )

        self.result_label.config(text=result_text, fg="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = VoterIDApp(root)
    root.mainloop()
