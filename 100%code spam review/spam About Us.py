from tkinter import Tk, Label, Button, PhotoImage, Frame

# Initialize the main window
root = Tk()
root.title("About Us")
root.geometry("700x500")  # Set window size
root.configure(bg="#f0f0f0")  # Light gray background

# --- Header Section ---
header = Frame(root, bg="#4CAF50", height=80)  # Green background
header.pack(side="top", fill="x")

Label(header, text="About Us", bg="#4CAF50", fg="white", font=("Arial", 24, "bold")).pack(pady=20)

# --- Content Section ---
content_frame = Frame(root, bg="white", padx=20, pady=20)
content_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Title Text
Label(content_frame, text="Welcome to Our Platform", font=("Arial", 18, "bold"), bg="white", fg="#333").pack(anchor="center", pady=10)

# Description Text
description = """we are dedicated to creating a safer and more efficient digital world. Our mission is to combat spam in all its forms—emails, messages, reviews, and beyond. Leveraging cutting-edge machine learning, natural language processing, and behavioral analysis, we provide innovative solutions to protect individuals and businesses from unwanted or harmful content.

Founded on the principles of trust and transparency, our team of experts is passionate about using technology to empower users and enhance communication"""

Label(content_frame, text=description, font=("Arial", 12), bg="white", fg="#555", wraplength=600, justify="left").pack(anchor="center", pady=10)

# Optional Image
try:
    img = PhotoImage(file="teamwork_image.jpg")  # Image in the same folder
    Label(content_frame, image=img, bg="white").pack(pady=10)
except:
    Label(content_frame, text="[Image Placeholder]", bg="white", fg="gray", font=("Arial", 12, "italic")).pack(pady=10)

# Button for More Information
Button(content_frame, text="Learn More", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", 
       padx=10, pady=5, relief="flat").pack(pady=20)

# --- Footer ---
footer = Frame(root, bg="#4CAF50", height=50)
footer.pack(side="bottom", fill="x")
Label(footer, text="© 2024 Our Company | All Rights Reserved", bg="#4CAF50", fg="white", font=("Arial", 10)).pack(pady=15)

# Run the main loop
root.mainloop()
