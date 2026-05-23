import tkinter as tk

def main():
    root = tk.Tk()
    root.title("MollyKao robot")
    root.geometry("1920x1080")
    root.attributes("-fullscreen", True)
    root.configure(bg="gray")
    title_label = tk.Label(
        root,
        text="V0 MollyKao",
        font=("Arial", 45, "bold"),
        fg="white",
        bg="gray",
    )
    title_label.pack(pady=35)
    button_frame = tk.Frame( root, bg="gray" )
    button_frame.pack(expand=True)

    button_opts = {
        "font": ("Arial", 24),
        "width": 20,
        "height": 2,
        "bg": "white",
        "fg": "black",
        "bd": 0,
        "activebackground": "lightgray",
        "activeforeground": "black"
    }
    b1 = tk.Button(button_frame, text="Control", **button_opts)
    b2 = tk.Button(button_frame, text="Bailes", **button_opts)
    b3 = tk.Button(button_frame, text="IA", **button_opts)
    b4 = tk.Button(button_frame, text="Config", **button_opts)

    b1.grid(row=0, column=0, padx=20, pady=20)
    b2.grid(row=0, column=1, padx=20, pady=20)
    b3.grid(row=1, column=0, padx=20, pady=20)
    b4.grid(row=1, column=1, padx=20, pady=20)

    root.bind("<Escape>", lambda e: root.destroy())

    root.mainloop()

if __name__ == "__main__":    main()