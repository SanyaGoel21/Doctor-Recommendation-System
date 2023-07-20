from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
import os
import csv
import sys
from doctor_class import DoctorManagementSystem
import subprocess
import patient_Info as p
import tkinter as tk
from tkinter import ttk
 
def show_malaria():
        subprocess.Popen(["python", "MalariaDetectionUI.py"])        
 

def show_doctor_info():
    # Create an instance of the DoctorManagementSystem class
    dms=DoctorManagementSystem()
    dms.load_data()
 
    
# -----------------------------------GUI-------------------------------------------------

def DP():
    root = Tk()
    root.title('Welcome to disease predictor')
    root.iconbitmap('icon.ico')

    root.configure(background='steelblue')
    
    # ----------GUI dropdown  entry variables-------------------------------------------
    global Symptom_option1
    Symptom_option1 = StringVar()
    Symptom_option1.set(None)
    global Symptom_option2
    Symptom_option2 = StringVar()
    Symptom_option2.set(None)
    global Symptom_option3
    Symptom_option3 = StringVar()
    Symptom_option3.set(None)
    global Symptom_option4
    Symptom_option4 = StringVar()
    Symptom_option4.set(None)
    global Symptom_option5
    Symptom_option5 = StringVar()
    Symptom_option5.set(None)
    global Symptom_option6
    Symptom_option6 = StringVar()
    Symptom_option6.set(None)
    global Symptom_option7
    Symptom_option7 = StringVar()
    Symptom_option7.set(None)
    global Symptom_option8
    Symptom_option8 = StringVar()
    Symptom_option8.set(None)
    global Symptom_option9
    Symptom_option9 = StringVar()
    Symptom_option9.set(None)
    global Symptom_option10
    Symptom_option10 = StringVar()
    Symptom_option10.set(None)
    global Name
    Name = StringVar()
   

    # -----------GUI labels Heading------------------------------------------------------


    lbl_heading = Label(root, justify=CENTER, text="welcome to disease predictor", fg="white", bg="steelblue")
    lbl_heading.config(font=("Arial", 40 , "bold"))
    lbl_heading.grid(row=2, column=3, columnspan=5, padx=40, pady=10)


    # ---------GUI labels---------------------------------------------------------------

    lbl_symptom1 = Label(root, text="Symptom 1", fg="white" , bg= "steelblue")
    lbl_symptom1.config(font=("lucida bright", 14))
    lbl_symptom1.grid(row=7, column=1, padx=30, pady=20, sticky=W)

    lbl_symptom2 = Label(root, text="Symptom 2", fg="white" , bg= "steelblue")
    lbl_symptom2.config(font=("lucida bright", 14))
    lbl_symptom2.grid(row=9, column=1, padx=30, pady=20, sticky=W)

    lbl_symptom3 = Label(root, text="Symptom 3", fg="white" , bg= "steelblue")
    lbl_symptom3.config(font=("lucida bright", 14))
    lbl_symptom3.grid(row=11, column=1, padx=30, pady=20, sticky=W)

    lbl_symptom4 = Label(root, text="Symptom 4", fg="white" , bg= "steelblue")
    lbl_symptom4.config(font=("lucida bright", 14))
    lbl_symptom4.grid(row=13, column=1, padx=30, pady=20, sticky=W)

    lbl_symptom5 = Label(root, text="Symptom 5", fg="white" , bg= "steelblue")
    lbl_symptom5.config(font=("lucida bright", 14))
    lbl_symptom5.grid(row=15, column=1, padx=30, pady=20, sticky=W)

    lbl_symptom6 = Label(root, text="Symptom 6", fg="white" , bg= "steelblue")
    lbl_symptom6.config(font=("lucida bright", 14))
    lbl_symptom6.grid(row=7, column=7, padx=30, pady=20, sticky=W)

    lbl_symptom7 = Label(root, text="Symptom 7", fg="white" , bg= "steelblue")
    lbl_symptom7.config(font=("lucida bright", 14))
    lbl_symptom7.grid(row=9, column=7, padx=30, pady=20, sticky=W)

    lbl_symptom8 = Label(root, text="Symptom 8", fg="white" , bg= "steelblue")
    lbl_symptom8.config(font=("lucida bright", 14))
    lbl_symptom8.grid(row=11, column=7, padx=30, pady=20, sticky=W)

    lbl_symptom9 = Label(root, text="Symptom 9", fg="white" , bg= "steelblue")
    lbl_symptom9.config(font=("lucida bright", 14))
    lbl_symptom9.grid(row=13, column=7, padx=30, pady=20, sticky=W)

    lbl_symptom10 = Label(root, text="Symptom 10", fg="white" , bg= "steelblue")
    lbl_symptom10.config(font=("lucida bright", 14))
    lbl_symptom10.grid(row=15, column=7, padx=30, pady=20, sticky=W)

    # ------------GUI Text entries----------------------------------
    OPTIONS = sorted(symtoms_arraylist)

    comb1_symptom_option = OptionMenu(root, Symptom_option1, *OPTIONS)
    comb1_symptom_option.grid(row=7, padx=150, pady=10, column=5)

    comb2_symptom_option = OptionMenu(root, Symptom_option2, *OPTIONS)
    comb2_symptom_option.grid(row=9, pady=10, column=5)

    comb3_symptom_option = OptionMenu(root, Symptom_option3, *OPTIONS)
    comb3_symptom_option.grid(row=11, pady=10, column=5)

    comb4_symptom_option = OptionMenu(root, Symptom_option4, *OPTIONS)
    comb4_symptom_option.grid(row=13, pady=10, column=5)

    comb5_symptom_option = OptionMenu(root, Symptom_option5, *OPTIONS)
    comb5_symptom_option.grid(row=15, pady=10, column=5)



    comb6_symptom_option = OptionMenu(root, Symptom_option6, *OPTIONS)
    comb6_symptom_option.grid(row=7, padx=10, pady=10, column=7)

    comb7_symptom_option = OptionMenu(root, Symptom_option7, *OPTIONS)
    comb7_symptom_option.grid(row=9, pady=10, column=7)

    comb8_symptom_option = OptionMenu(root, Symptom_option8, *OPTIONS)
    comb8_symptom_option.grid(row=11, pady=10, column=7)

    comb9_symptom_option = OptionMenu(root, Symptom_option9, *OPTIONS)
    comb9_symptom_option.grid(row=13, pady=10, column=7)

    comb10_symptom_option = OptionMenu(root, Symptom_option10, *OPTIONS)
    comb10_symptom_option.grid(row=15, pady=10, column=7)



    btn_dst = Button(root, text="DIAGNOSE", command=DecisionTree, bg="white", fg="black")
    btn_dst.grid(row=20, column=5 )

    # btn_dst2 = Button(root, text="NaiveBayes DIAGNOSE", command=NaiveBayes, bg="deepskyblue", fg="white")
    # btn_dst2.grid(row=21, column=5  )

    btn_dst = Button(root, text="DISEASE DESCRIPTION AND RECOMMEND DOCTOR", command=DiseaseDescription, bg="white", fg="black")
    btn_dst.grid(row=22, column=5 )


    
  
    btn_dst6 = Button(root, text="Malaria Test", command=show_malaria, bg="orange", fg="white")
    btn_dst6.grid(row=2, column=1)
    btn_dst4 = Button(root, text="Patient Info", command=p.HomePage, bg="orange", fg="white")
    btn_dst4.grid(row=2, column=2)

    # btn_dst5 = Button(root, text="Doctor Info", command=show_doctor_info, bg="green", fg="white")
    # btn_dst5.grid(row=2, column=2)



    # ---------GUI textfileds-----------------------------------------------
    global t1
    t1 = Text(root, height=2, width=30, bg="black", fg="white")
    t1.grid(row=20, column=7, padx=100, pady=20)
    
    # global t2
    # t2 = Text(root, height=2, width=30, bg="black", fg="white")
    # t2.grid(row=21, column=7, padx=100, pady=20)

    global t3
    t3 = Text(root, height=5, width=50, bg="black", fg="white")
    t3.grid(row=22, column=7, padx=100, pady=20)
 
# ---------------------Below is symtoms list array----------------------
symtoms_arraylist = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
      'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
      'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
      'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
      'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
      'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
      'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
      'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
      'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
      'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
      'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
      'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
      'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
      'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria',
      'family_history', 'mucoid_sputum',
      'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
      'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
      'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
      'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
      'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
      'yellow_crust_ooze']
# --------------------------below is disease_arraylist list array----------------------------------------------
disease_arraylist = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
           'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
           ' Migraine', 'Cervical spondylosis',
           'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
           'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
           'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
           'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis',
           'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection', 'Psoriasis',
           'Impetigo']

l2 = []  # we define the blank array
for x in range(0, len(symtoms_arraylist)):  # here symtoms_arraylist is symtoms list, simply initilize l2 list as symtoms_arraylist with 0 value
    l2.append(0)

# -------------------------TESTING DATA df ------------------------------------------------------------
df = pd.read_csv("Training.csv")  # here we read the trainging csv data set into memory panda
# print(df.head())

# Bellow 'prognosis'(means rog ka nidaan) is last column name in training.csv file, means i have to convert string to numbervalue
df.replace({'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                          'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8,
                          'Bronchial Asthma': 9, 'Hypertension ': 10,
                          'Migraine': 11, 'Cervical spondylosis': 12,
                          'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                          'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                          'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                          'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                          'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                          'Varicose veins': 30, 'Hypothyroidism': 31,
                          'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                          '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                          'Psoriasis': 39,
                          'Impetigo': 40}}, inplace=True)  # here we replace the the arare with like this

# print(df.head())

X = df[symtoms_arraylist]

y = df[["prognosis"]]
np.ravel(y)

# The returned array will have the same type as that of the input array.
# print(y)

# -----------------------------TRAINING DATA tr ---------------------------------------------------
tr = pd.read_csv("Testing.csv")
tr.replace({'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                          'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8,
                          'Bronchial Asthma': 9, 'Hypertension ': 10,
                          'Migraine': 11, 'Cervical spondylosis': 12,
                          'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                          'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                          'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                          'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                          'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                          'Varicose veins': 30, 'Hypothyroidism': 31,
                          'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                          '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                          'Psoriasis': 39,
                          'Impetigo': 40}}, inplace=True)

X_test = tr[symtoms_arraylist]
y_test = tr[["prognosis"]]
np.ravel(y_test)


# ------------------Below is DecisionTree Algorithm-------------------------------------
def DecisionTree():
    psymptoms = [Symptom_option1.get(), Symptom_option2.get(), Symptom_option3.get(), Symptom_option4.get(),
                 Symptom_option5.get(), Symptom_option6.get(), Symptom_option7.get(), Symptom_option8.get(),
                 Symptom_option9.get(), Symptom_option10.get()]

    num_selected_symptoms = psymptoms.count('None')
    if num_selected_symptoms >7:
        alert_message = "Please select a minimum of 3 symptom options."
        messagebox.showwarning("Alert", alert_message)
        return

    from sklearn import tree
    clf3 = tree.DecisionTreeClassifier()  # empty model of the decision tree
    clf3 = clf3.fit(X, y)

# -------------------calculating accuracy-------------------------------------
    '''from sklearn.metrics import accuracy_score
    y_pred = clf3.predict(X_test)
    print("accuracy_score :{}".format(accuracy_score(y_test, y_pred)))
    print("accuracy_score (false):{}".format(accuracy_score(y_test, y_pred, normalize=False)))'''

# -------------get value---------------------------------------------------------



    print("==============sytemp entry=====================")
    print(psymptoms)
    for k in range(0, len(symtoms_arraylist)):
        # print (k,)
        for z in psymptoms:
            if (z == symtoms_arraylist[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    print("==============Test Value=====================")
    print(inputtest)
    print("==============Predict Value=====================")
    print(predict)
    predicted = predict[0]

    h = 'no'
    for a in range(0, len(disease_arraylist)):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease_arraylist[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")

# --------Below is Random forest Algorithm----------------------------

def randomforest():

    psymptoms = [Symptom_option1.get(), Symptom_option2.get(), Symptom_option3.get(), Symptom_option4.get(),
                 Symptom_option5.get(), Symptom_option6.get(), Symptom_option7.get(), Symptom_option8.get(),
                 Symptom_option9.get(), Symptom_option10.get()]

    num_selected_symptoms = psymptoms.count('None')
    if num_selected_symptoms >7:
        alert_message = "Please select a minimum of 3 symptom options."
        messagebox.showwarning("Alert", alert_message)
        return


    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X, np.ravel(y))  # X=The number of trees in the forest.,np=

# --------------calculating accuracy-------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred = clf4.predict(X_test)
    print("accuracy_score:{}".format(accuracy_score(y_test, y_pred)))
    print("accuracy_score (false):{}".format(accuracy_score(y_test, y_pred, normalize=False)))
  

    for k in range(0, len(symtoms_arraylist)):
        for z in psymptoms:
            if (z == symtoms_arraylist[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted = predict[0]
    predict

    h = 'no'
    for a in range(0, len(disease_arraylist)):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease_arraylist[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")

# ------------Below is naive bayes Algorithm-------------------------------
'''def NaiveBayes():
    psymptoms = [Symptom_option1.get(), Symptom_option2.get(), Symptom_option3.get(), Symptom_option4.get(),
                 Symptom_option5.get(), Symptom_option6.get(), Symptom_option7.get(), Symptom_option8.get(),
                 Symptom_option9.get(), Symptom_option10.get()]

    num_selected_symptoms = psymptoms.count('None')
    if num_selected_symptoms >7:
        alert_message = "Please select a minimum of 3 symptom options."
        messagebox.showwarning("Alert", alert_message)
        return
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb = gnb.fit(X, np.ravel(y))

# ---------calculating accuracy-------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict(X_test)
    print("accuracy_score :{}".format(accuracy_score(y_test, y_pred)))
    print("accuracy_score (false):{}".format(accuracy_score(y_test, y_pred, normalize=False)))



# -----------Here we get the user enter value ------------------------------------------

    psymptoms = [Symptom_option1.get(), Symptom_option2.get(), Symptom_option3.get(), Symptom_option4.get(), Symptom_option5.get(), Symptom_option6.get(), Symptom_option7.get(), Symptom_option8.get(), Symptom_option9.get(), Symptom_option10.get()]
    for k in range(0, len(symtoms_arraylist)):
        for z in psymptoms:
            if (z == symtoms_arraylist[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(0, len(disease_arraylist)):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease_arraylist[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")

# ---------------Below is SVM Algorithm------------------------------------

def mysvm():
    psymptoms = [Symptom_option1.get(), Symptom_option2.get(), Symptom_option3.get(), Symptom_option4.get(),
                 Symptom_option5.get(), Symptom_option6.get(), Symptom_option7.get(), Symptom_option8.get(),
                 Symptom_option9.get(), Symptom_option10.get()]

    num_selected_symptoms = psymptoms.count('None')
    if num_selected_symptoms >7:
        alert_message = "Please select a minimum of 3 symptom options."
        messagebox.showwarning("Alert", alert_message)
        return

    from sklearn import svm
    clf4 = svm.SVC(kernel='linear', C=1.0)
    svms = clf4.fit(X, np.ravel(y))
    print(svms)
# ---------calculating accuracy--------------------------------

    from sklearn.metrics import accuracy_score
    y_pred = clf4.predict(X_test)
    print("accuracy_score :".format(accuracy_score(y_test, y_pred)))
    print("accuracy_score (false):".format(accuracy_score(y_test, y_pred, normalize=False)))


# -----get value------------------------------------------------

    psymptoms = [Symptom_option1.get(), Symptom_option2.get(), Symptom_option3.get(), Symptom_option4.get(), Symptom_option5.get()]

    for k in range(0, len(symtoms_arraylist)):
        # print (k,)
        for z in psymptoms:
            if (z == symtoms_arraylist[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted = predict[0]
    print(predicted)
    h = 'no'
    for a in range(0, len(disease_arraylist)):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease_arraylist[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")
'''

#Disease Description 
def DiseaseDescription(): 
    import csv
    import sys
    # Get the input from the GUI (assuming it's a tkinter Text widget named "t1")
    disease_name = t1.get("1.0", "end-1c").strip().upper()

    # Read the CSV file and search for the disease name
    with open('disease_description.csv', 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0].strip().upper() == disease_name:
                # Found the disease description
                t3.delete("1.0", "end")
                #  description is in the second column
                t3.insert("1.0", row[1].strip())             
                break
            else:
                # Disease not found
                t3.delete("1.0", "end")
                t3.insert("1.0", "Disease Description Not Found")
                
    show_doctor(disease_name)
 
 
#Disease based doctor 
def show_doctor(disease_name):
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
    
    global doctor_list_screen
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
    #########
     
    

def doctor_search(disease_name):
    import csv
    import sys
    
    print(disease_name)
    #read csv, and split on "," the line
    csv_file = csv.reader(open('doctors_disease.csv', "rt"), delimiter=",")
    #loop through csv list
    flag=True
    result_set="Doctor Not Found"
    for row in csv_file:
        #if current rows 2nd value is equal to input, print that row
        if disease_name.strip().upper() == row[4].strip().upper():
            flag=True                       
            result_set=row[4]
            print(result_set)            
            break 


    return flag 
 
        
# --------------------Login and Register Page---------------------

def register():
    global register_screen
    register_screen = Toplevel(root)
    register_screen.title("Register")
    register_screen.geometry("300x250")
    register_screen.configure(background='green')
    

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="deepskyblue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="deepskyblue", command=register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(root)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    login_screen.configure(background='palegreen')
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
    root.destroy()    
    DP()
    #p.HomePage()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window
root = Tk()
root.title('Disease Prediction using machine learning')
root.iconbitmap('icon.ico')
root.configure(background='palegreen')
root.geometry("300x250")
root.title("Account Login")
Label(text="Welcome to Predictor", bg="white", width="300", height="2", font=("Calibri bold", 13)).pack()
Label(text="").pack()
Button(text="Login", height="2", width="30", command=login).pack()
Label(text="").pack()
Button(text="Register", height="2", width="30", command=register).pack()

root.mainloop()
