import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw

def load_images():
    global image1, image2
    image1 = load_image()
    image2 = load_image()

def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        try:
            return Image.open(file_path)
        except IOError:
            print("Erreur : Impossible de charger l'image.")
            return None
    else:
        return None

def create_diff_image():
    width, height = image1.size
    diff_image = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(diff_image)
    return diff_image, draw

def scan_images():
    if not image1 or not image2:
        print("Veuillez charger les deux images avant de scanner.")
        return

    diff_image, draw = create_diff_image()

    if image1.size != image2.size:
        print("Erreur : Les images doivent être de même taille pour être comparées.")
        return

    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))
            draw.point((x, y), fill="blue" if pixel1 == pixel2 else "red")

    diff_image.show()
    diff_image.save("image_differences.png")
    print("La nouvelle image avec les différences a été générée et enregistrée.")

image1 = None
image2 = None

def create_root():
    root = tk.Tk()
    root.title("Détection de différences entre images")
    return root

def create_buttons(root):
    load_button = tk.Button(root, text="Charger les images", command=load_images)
    load_button.pack(pady=10)

    scan_button = tk.Button(root, text="Scan", command=scan_images)
    scan_button.pack(pady=20)

def main():
    root = create_root()
    create_buttons(root)
    root.mainloop()

if __name__ == "__main__":
    main()
