import tkinter as tk

def express_feeling(feeling):
    if feeling == "Happy":
        draw_happy_face()
    elif feeling == "Sad":
        draw_sad_face()
    elif feeling == "Excited":
        draw_excited_face()
    elif feeling == "Angry":
        draw_angry_face()
    elif feeling == "Surprised":
        draw_surprised_face()

def draw_happy_face():
    canvas.delete("all")
    canvas.create_oval(50, 50, 250, 250, fill="yellow")  # Head
    canvas.create_oval(90, 100, 110, 120, fill="black")  # Left eye
    canvas.create_oval(190, 100, 210, 120, fill="black")  # Right eye
    canvas.create_arc(90, 150, 210, 190, start=180, extent=180, width=2, style="arc")  # Smile

def draw_sad_face():
    canvas.delete("all")
    canvas.create_oval(50, 50, 250, 250, fill="yellow")  # Head
    canvas.create_oval(90, 130, 110, 150, fill="black")  # Left eye
    canvas.create_oval(190, 130, 210, 150, fill="black")  # Right eye
    canvas.create_arc(90, 180, 210, 220, start=0, extent=180, width=2, style="arc")  # Frown

def draw_excited_face():
    canvas.delete("all")
    canvas.create_oval(50, 50, 250, 250, fill="yellow")  # Head
    canvas.create_oval(90, 100, 110, 120, fill="black")  # Left eye
    canvas.create_oval(190, 100, 210, 120, fill="black")  # Right eye
    canvas.create_line(95, 180, 205, 180, width=2)  # Mouth line

def draw_angry_face():
    canvas.delete("all")
    canvas.create_oval(50, 50, 250, 250, fill="yellow")  # Head
    canvas.create_oval(90, 130, 110, 150, fill="black")  # Left eye
    canvas.create_oval(190, 130, 210, 150, fill="black")  # Right eye
    canvas.create_line(95, 200, 205, 200, width=2)  # Angry mouth line

def draw_surprised_face():
    canvas.delete("all")
    canvas.create_oval(50, 50, 250, 250, fill="yellow")  # Head
    canvas.create_oval(90, 100, 110, 120, fill="black")  # Left eye
    canvas.create_oval(190, 100, 210, 120, fill="black")  # Right eye
    canvas.create_line(95, 180, 205, 180, width=2)  # Mouth line
    canvas.create_line(150, 130, 150, 140, width=2)  # Surprised eyebrow

def create_feeling_button(feeling):
    button = tk.Button(root,width=20, text=feeling, command=lambda: express_feeling(feeling))
    button.pack(pady=5, padx=10)

# Create the main window
root = tk.Tk()
root.title("Express Feelings")
root.configure(background='blue',highlightthickness=7,highlightcolor="PowderBlue")
system_Name =tk.Label(root,padx=0, bd= 20,width=37, relief=tk.RIDGE, text="Muchina's Fellings expressions", fg= "PowderBlue", bg="blue", font=("times new roman",30))
system_Name.pack(pady=0, padx=0)

# Create feeling buttons
feelings = ["Happy", "Sad", "Excited", "Angry", "Surprised"]
for feeling in feelings:
    create_feeling_button(feeling)

# Create a canvas for drawing
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Run the application
root.mainloop()
