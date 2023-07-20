import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import pandas as pd
import os
import csv

# Keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class MalariaDetectionUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Malaria Detection")
        self.model_loaded = False

        self.label_top = tk.Label(root, text="Malaria Detection", justify=CENTER, fg="white", bg="steelblue")
        self.label_top.config(font=("Arial", 40 , "bold"))
        self.label_top.pack(pady=10)

        self.btn_load = tk.Button(root, text="Load Model", command=self.load_model)
        self.btn_load.pack(pady=10)

        self.label_path = tk.Label(root, text="Image Path:",width=0, height=0)
        self.label_path.pack()

        self.btn_browse = tk.Button(root, text="Browse", command=self.browse_image)
        self.btn_browse.pack()

        self.img_label = tk.Label(root)
        self.img_label.pack()

        self.btn_predict = tk.Button(root, text="Predict", command=self.predict)
        self.btn_predict.pack(pady=10)

        self.result_label = tk.Label(root, text="Result:", fg="black", bg="steelblue")
        self.result_label.pack(pady=10)
        

    def load_model(self):
        # Placeholder function to load the model file
        # Replace this with your actual model loading code
        self.model_loaded = True
        self.btn_browse.config(state=tk.NORMAL)
        self.btn_predict.config(state=tk.NORMAL)
        self.MODEL_PATH = 'model_vgg19.h5'
        # Load your trained model
        if os.path.exists(self.MODEL_PATH):
            # File exists, proceed with opening or accessing it
            self.model = load_model(self.MODEL_PATH)
            alert_message = "Successfully loaded"
            messagebox.showwarning("Alert", alert_message)
        else:
            # File does not exist, handle the error accordingly
            alert_message = "File does not exist, handle the error accordingly"
            messagebox.showwarning("Alert", alert_message)

        

    def modelMalaria_predict(self, img_path, model):
        print('Predicting...')
        img = image.load_img(img_path, target_size=(224, 224))

        # Preprocessing the image
        x = image.img_to_array(img)
        x = x / 255  # Scaling
        x = np.expand_dims(x, axis=0)

        # Be careful how your trained model deals with the input
        # otherwise, it won't make the correct prediction!
        x = preprocess_input(x)

        preds = model.predict(x)
        print(preds)
        preds = np.argmax(preds, axis=1)
        if preds == 0:
            preds = " UnInfected"
        else:
            preds = "Infected"

        return preds

    def browse_image(self):
        if self.model_loaded:
            image_path = filedialog.askopenfilename()
            self.label_path.config(text=f"{image_path}")
            self.show_image(image_path)

    def show_image(self, image_path):
        image = Image.open(image_path)
        image = image.resize((300, 300))
        img_tk = ImageTk.PhotoImage(image)
        self.img_label.config(image=img_tk)
        self.img_label.image = img_tk

    def predict(self):
        if self.model_loaded:
            img_path = self.label_path.cget("text")
            if img_path is not None:
                result = self.modelMalaria_predict(img_path, self.model)
                self.result_label.config(text=result)
                self.show_doctor('malaria')
                print("Prediction: {}".format(result))
                 
            print("Performing prediction...")
    
    def show_doctor(self,disease_name):
        # Open the CSV file
        with open('doctors_disease.csv', newline='') as csvfile:
            # Create a CSV reader object
            reader = csv.reader(csvfile)
            # Create an empty list to store matching rows
            matches = []
            # Loop through each row in the CSV file
            for row in reader:
                # Check if the doctor name matches the search query
                if disease_name.lower() in row[4].lower():
                    # If it matches, add the row to the matches list
                    matches.append(row)
                    print(row)
        
        # Create a new Tkinter window
        doctor_list_screen = tk.Toplevel()
        # Set the window title
        doctor_list_screen.title("Matching Doctors")
        doctor_list_screen.geometry("600x400")
        # Create a Treeview widget
        tree = ttk.Treeview(doctor_list_screen)
        # Define columns
        tree["columns"] = ("ID", "Doctor", "Phone", "Specialist", "Disease", "Address", "Pincode")
        # Format columns
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("ID", anchor=tk.CENTER, width=40)
        tree.column("Doctor", anchor=tk.CENTER, width=120)
        tree.column("Phone", anchor=tk.CENTER, width=100)
        tree.column("Specialist", anchor=tk.CENTER, width=100)
        tree.column("Disease", anchor=tk.CENTER, width=100)
        tree.column("Address", anchor=tk.CENTER, width=100)
        tree.column("Pincode", anchor=tk.CENTER, width=60)
        # Create headings
        tree.heading("#0", text="", anchor=tk.CENTER)
        tree.heading("ID", text="ID", anchor=tk.CENTER)
        tree.heading("Doctor", text="Doctor", anchor=tk.CENTER)
        tree.heading("Phone", text="Phone", anchor=tk.CENTER)
        tree.heading("Specialist", text="Specialist", anchor=tk.CENTER)
        tree.heading("Disease", text="Disease", anchor=tk.CENTER)
        tree.heading("Address", text="Address", anchor=tk.CENTER)
        tree.heading("Pincode", text="Pincode", anchor=tk.CENTER)
        # Add data to the treeview
        for row in matches:
            tree.insert("", tk.END, values=row)

        # Pack the treeview widget
        tree.pack(fill=tk.BOTH, expand=1)

        # Run the main Tkinter event loop
        doctor_list_screen.mainloop()


def start_ui():
    root = tk.Tk()
    root.title('Welcome to disease predictor')
    root.iconbitmap('icon.ico')

    root.configure(background='steelblue')
    app = MalariaDetectionUI(root)
    root.mainloop()


if __name__ == "__main__":
    start_ui()

                
