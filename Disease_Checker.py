from tkinter import *
import tkinter as tk

dis = Tk()

#Title for window
dis.title('Disease Checker')

#Set size of window
dis.geometry('400x250')

#function to check symptoms
def diseasecheck():
    symptoms = [
    ['fever', 'cough', 'fatigue', 'body aches'],
    ['excessive thirst', 'frequent urination', 'fatigue'],
    ['chest pain', 'shortness of breath', 'fatigue'],
    ['headaches', 'dizziness', 'blurred vision'],
    ['wheezing', 'shortness of breath', 'coughing'],
    ['memory loss', 'confusion', 'difficulty in tasks'],
    ['joint pain', 'swelling', 'stiffness'],
    ['chronic cough', 'shortness of breath', 'wheezing'],
    ['fragile bones', 'fractures', 'loss of height'],
    ['jaundice', 'fatigue', 'abdominal pain'],
    ['unexplained weight loss', 'fatigue', 'pain'],
    ['persistent sadness', 'loss of interest', 'fatigue']]

    diseases = ['Influenza (Flu)','Diabetes Mellitus','Coronary Artery Disease (CAD)','Hypertension',
    'Asthma',
    "Alzheimer's Disease",
    'Rheumatoid Arthritis',
    'Chronic Obstructive Pulmonary Disease (COPD)',
    'Osteoporosis',
    'Hepatitis B',
    'Cancer (various types)',
    'Depression']
    #Getting user input values into function
    sym1 = sympvar1.get().lower()
    sym2 = sympvar2.get().lower()
    sym3 = sympvar2.get().lower()
    #Checking symptoms are in predefined list
    for i in range(len(symptoms)):
        if sym1 in symptoms[i] and sym2 in symptoms[i] and sym3 in symptoms[i]:
            result = Label(dis,text = 'May be you are suffering from '+diseases[i]).grid(padx = 20)
            break
    else:
        result = Label(dis,text = 'Sorry we Could not found the disease! Please consult a doctor!!').grid(padx = 30)
            
            
#Label -> displayed on tkinter windoe
label = Label(dis,text='Enter three symptoms you have').grid(padx = 50)
sympvar1 = tk.StringVar()
sympvar2 = tk.StringVar()
sympvar3 = tk.StringVar()

#Taking input from user 
symp_Entry1 = Entry(dis,text = sympvar1).grid(row = 1,column = 0,padx = 90,pady = 10)
symp_Entry2 = Entry(dis,text = sympvar2).grid(row = 2,column = 0,padx = 90,pady = 10)
symp_Entry3 = Entry(dis,text = sympvar3).grid(row = 3,column = 0,padx = 90,pady = 10)

#Button to call the diseasecheck function
button = Button(dis,text = 'Check Disease',command=diseasecheck).grid(row = 4,column = 0,padx = 90,pady = 10)
    
dis.mainloop()
