from tkinter import *     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import importlib.util
import sys
import os
import pyperclip
import pathlib
from time import sleep
# spec = importlib.util.spec_from_file_location("generalfunctions", r"E:\GitHub\AdobeScripts\functionsOnly\classes\generalfunctions.py")
# mac path
# spec = importlib.util.spec_from_file_location("generalfunctions", r"/Users/miguelsalvador1/Documents/GitHub/AdobeScripts/functionsOnly/classes/generalfunctions.py")
# spec = importlib.util.spec_from_file_location("generalfunctions", r"C:\Users\Migue\Documents\GitHub\AdobeScripts\functionsOnly\classes\generalfunctions.py")
# gf = importlib.util.module_from_spec(spec)
# sys.modules["generalfunctions"] = gf
# spec.loader.exec_module(gf)
# from generalfunctions import generalFunctions as gfi
# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# print(filename)




def fn_find_file():
    global filename 
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    
    
root = Tk()
root.title('myversion_namingConventions17')

frame_file_decision = LabelFrame(root, text = "Choose file or copy to clipboard?",padx=20,pady=20)
frame_file_decision.grid(row=0,column=0)

g = IntVar()
g.set("1")
default_final_button_text = StringVar()
# global bool_clipboard = False
def update_btn_rename_file_text(value):
    if value ==1:
        txt_fieldName0_2.grid_forget()
        default_final_button_text.set("Copy Name to Clipboard")
    else:
        txt_fieldName0_2.grid_forget()
        default_final_button_text.set("Rename File")
def extension_widget(value):
    # bool_clipboard = False
    if value==1:
        # print("e")
        update_btn_rename_file_text(1)
        #!frame3_extension.grid(row=2,column=1)
        btn_find_file.pack_forget()
        # bool_clipboard = True
    else:
        update_btn_rename_file_text(2)
        #!frame3_extension.grid_remove()
        btn_find_file.pack()
        # bool_clipboard = False

Radiobutton(frame_file_decision,text="Copy to clipboard", variable=g,value=1,command=lambda: extension_widget(1)).pack()
Radiobutton(frame_file_decision,text="Choose File", variable=g,value=2, command=lambda: extension_widget(2)).pack()


frame = LabelFrame(root, text = "rename_files_17_0.1",padx=20,pady=20)
frame.grid(row=0,column=1)
frame2 = LabelFrame(root, text = "What file are you naming?",padx=20,pady=20)
frame2.grid(row=1,column=0)
frame3 = LabelFrame(root, text = "Naming Work in Progress",padx=20,pady=20)
# frame3.grid(row=2,column=0)
frame3_1 = LabelFrame(root, text = "Naming - Final Exports",padx=20,pady=20)
frame3_extension = LabelFrame(root, text = "Extension",padx=20,pady=20)
# frame3_extension.grid(row=2,column=1)
# frame3_1.grid(row=2,column=0)
frame4 = LabelFrame(root, text = "",padx=20,pady=20)
frame4.grid(row=3,column=0)

btn_find_file = Button(frame_file_decision, text="Find File", padx =20,pady=10, command=fn_find_file)#.grid(row=0,column=1)
# btn_find_file.pack()

def set_Array_fromTxtFile(fileChosen):
    array_AllLines = []
    with open(fileChosen,encoding='latin-1') as fr:
        linesSplit = fr.read().split("\n")
    for x in range(len(linesSplit)):
        array_AllLines.append(linesSplit[x])
    return array_AllLines

desktop = os.path.expanduser('~') + '/Desktop'
array_gameName = (set_Array_fromTxtFile( os.path.join(desktop, r"scripts/file_naming17/fields/gameName.txt" )))
array_platform = (set_Array_fromTxtFile(os.path.join(desktop, r"scripts/file_naming17/fields/platform.txt")))

array_versionNumber = (set_Array_fromTxtFile(  os.path.join(desktop, r"scripts/file_naming17/fields/versionNumber.txt")))
array_trailerTitle = (set_Array_fromTxtFile(  os.path.join(desktop, r"scripts/file_naming17/fields/trailer.txt")))
array_dimensions = (set_Array_fromTxtFile( os.path.join(desktop, r"scripts/file_naming17/fields/dimensions.txt")))
array_ageRating = (set_Array_fromTxtFile(os.path.join(desktop, r"scripts/file_naming17/fields/ageRating.txt")))
array_duration = (set_Array_fromTxtFile(os.path.join(desktop, r"scripts/file_naming17/fields/duration.txt")))
array_language = (set_Array_fromTxtFile(os.path.join(desktop, r"scripts/file_naming17/fields/language.txt")))
array_extension = (set_Array_fromTxtFile(os.path.join(desktop, r"scripts/file_naming17/fields/extension.txt")))

def show_namingConvention(number):
    frame3.grid_remove()
    frame3_1.grid(row=2,column=0)
    # frame3_extension.grid(row=2,column=1)

def show_workInProgress(number):
    if number==1:
        frame3_1.grid_remove()
        frame3.grid(row=2,column=0)
        
txt_fieldName0 = Label(frame3, text ="Game Name", pady=5).grid(row=1,column=1)
txt_fieldName1 = Label(frame3, text ="Trailer", pady=5).grid(row=1,column=2)
txt_fieldName2 = Label(frame3, text ="Version Number ", pady=5).grid(row=1,column=3)
txt_fieldName3 = Label(frame3_extension, text ="Extension", pady=5).grid(row=1,column=4)
input_fieldName0 = Entry(frame3,border= 2)
input_fieldName1 = Entry(frame3,border= 2)
input_fieldName2 = Entry(frame3,border= 2)
input_fieldName3 = Entry(frame3_extension,border= 2)
input_fieldName0.grid(row=2,column=1)
input_fieldName1.grid(row=2,column=2)
input_fieldName2.grid(row=2,column=3)
input_fieldName3.grid(row=2,column=4)
clicked0 ,clicked1 ,clicked2,clicked3 = StringVar(),StringVar(),StringVar(),StringVar()
clicked0.set(array_gameName[0])
clicked1.set(array_trailerTitle[0])
clicked2.set(array_versionNumber[0])
clicked3.set(array_extension[0])
drop0 = OptionMenu(frame3,clicked0,*array_gameName).grid(row=3,column=1)
drop1 = OptionMenu(frame3,clicked1,*array_trailerTitle).grid(row=3,column=2)
drop2 = OptionMenu(frame3,clicked2,*array_versionNumber).grid(row=3,column=3)
drop3 = OptionMenu(frame3_extension,clicked3,*array_extension).grid(row=3,column=4)


txt_fieldName0_2 = Label(frame3_1, text ="Game Name", pady=5).grid(row=1,column=1)
txt_fieldName1_2 = Label(frame3_1, text ="Trailer", pady=5).grid(row=1,column=2)
txt_fieldName2_2 = Label(frame3_1, text ="Platform", pady=5).grid(row=1,column=3)
txt_fieldName3_2 = Label(frame3_1, text ="Dimensions", pady=5).grid(row=1,column=4)
txt_fieldName4_2 = Label(frame3_1, text ="Age Rating", pady=5).grid(row=1,column=5)
txt_fieldName5_2 = Label(frame3_1, text ="Duration", pady=5).grid(row=1,column=6)
txt_fieldName6_2 = Label(frame3_1, text ="Language", pady=5).grid(row=1,column=7)
# txt_fieldName7_2 = Label(frame3_extension, text ="Extension", pady=5).grid(row=1,column=8)

input_fieldName0_2 = Entry(frame3_1,border= 2)
input_fieldName1_2 = Entry(frame3_1,border= 2)
input_fieldName2_2 = Entry(frame3_1,border= 2)
input_fieldName3_2 = Entry(frame3_1,border= 2)
input_fieldName4_2 = Entry(frame3_1,border= 2)
input_fieldName5_2 = Entry(frame3_1,border= 2)
input_fieldName6_2 = Entry(frame3_1,border= 2)
# input_fieldName7_2 = Entry(frame3_extension,border= 2)
input_fieldName0_2.grid(row=2,column=1)
input_fieldName1_2.grid(row=2,column=2)
input_fieldName2_2.grid(row=2,column=3)
input_fieldName3_2.grid(row=2,column=4)
input_fieldName4_2.grid(row=2,column=5)
input_fieldName5_2.grid(row=2,column=6)
input_fieldName6_2.grid(row=2,column=7)
# input_fieldName7_2.grid(row=2,column=8)

# test = ["a","b"]

clicked0_2 ,clicked1_2 ,clicked2_2 ,clicked3_2 ,clicked4_2 ,clicked5_2 ,clicked6_2 ,clicked7_2 = StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
clicked0_2.set(array_gameName[0])
clicked1_2.set(array_trailerTitle[0])
clicked2_2.set(array_platform[0])
clicked3_2.set(array_dimensions[0])
clicked4_2.set(array_ageRating[0])
clicked5_2.set(array_duration[0])
clicked6_2.set(array_language[0])
# clicked7_2.set(array_extension[0])

drop0_2 = OptionMenu(frame3_1,clicked0_2,*array_gameName).grid(row=3,column=1)
drop1_2 = OptionMenu(frame3_1,clicked1_2,*array_trailerTitle).grid(row=3,column=2)
drop2_2 = OptionMenu(frame3_1,clicked2_2,*array_platform).grid(row=3,column=3)
drop3_2 = OptionMenu(frame3_1,clicked3_2,*array_dimensions).grid(row=3,column=4)
drop4_2 = OptionMenu(frame3_1,clicked4_2,*array_ageRating).grid(row=3,column=5)
drop5_2 = OptionMenu(frame3_1,clicked5_2,*array_duration).grid(row=3,column=6)
drop6_2 = OptionMenu(frame3_1,clicked6_2,*array_language).grid(row=3,column=7)
# drop7_2 = OptionMenu(frame3_1,clicked7_2,*array_extension).grid(row=3,column=8)

r = IntVar()
r.set("1")

Radiobutton(frame2,text="Work in Progress", variable=r,value=1,command=lambda: show_workInProgress(1)).pack()
Radiobutton(frame2,text="Final Exports", variable=r,value=2, command=lambda: show_namingConvention(1)).pack()


def fn_generate_button():
    if r.get() == 1:
        # ! conditions to check if input box is empty
        # ! Clear
        if input_fieldName0.get() != "":
            str_game_name = input_fieldName0.get()
        else:
            str_game_name = clicked0.get()
        if input_fieldName1.get() != "":
            str_trailer = input_fieldName1.get()
        else:
            str_trailer = clicked1.get()
        if input_fieldName2.get() != "":
            str_version_number = input_fieldName2.get()
        else:
            str_version_number = clicked2.get()
        if input_fieldName3.get() !="":
            str_extension = input_fieldName3.get()
        else:
            str_extension = clicked3.get()
        if g.get() == 1:
            final_file_name = (f'{str_game_name}_{str_trailer}_{str_version_number}')    
            #! final_file_name = (f'{str_game_name}_{str_trailer}_{str_version_number}_{str_extension}')    
            pyperclip.copy(final_file_name)
            print(final_file_name)
            txt_fieldName0_2.grid(row=1,column=1)
            txt_fieldName0_2.config(text="Filename copied to clipboard!")

        elif g.get() ==2:

            filename_only,extension = os.path.splitext(str(filename))
            final_file_name = (f'{str_game_name}_{str_trailer}_{str_version_number}')    
            print(final_file_name)
            os.rename(filename,os.path.join(os.path.dirname(filename_only),final_file_name+extension))
            txt_fieldName0_2.grid(row=1,column=1)
            txt_fieldName0_2.config(text="File renamed!")

            # input_fieldName0.delete(0,END)

    if r.get() ==2:
        # print(filename)
        # filename_only,extension = os.path.splittext(filename)
        # print(filename_only)
        if input_fieldName0_2.get() != "":
            str_game_name = input_fieldName0_2.get()
        else:
            str_game_name = clicked0_2.get()
        if input_fieldName1_2.get() != "":
            str_trailer = input_fieldName1_2.get()
        else:
            str_trailer = clicked1_2.get()
        if input_fieldName2_2.get() != "":
            str_platform = input_fieldName2_2.get()
        else:
            str_platform = clicked2_2.get()
        if input_fieldName3_2.get() != "":
            str_dimensions = input_fieldName3_2.get()
        else:
            str_dimensions = clicked3_2.get()
        if input_fieldName4_2.get() != "":
            str_age_rating = input_fieldName4_2.get()
        else:
            str_age_rating = clicked4_2.get()
        if input_fieldName5_2.get() != "":
            str_duration = input_fieldName5_2.get()
        else:
            str_duration = clicked5_2.get()
        if input_fieldName6_2.get() != "":
            str_language = input_fieldName6_2.get()
        else:
            str_language = clicked6_2.get()
        if input_fieldName3.get() !="":
            str_extension = input_fieldName3.get()
        else:
            str_extension = clicked3.get()
        if g.get() == 1:
            final_file_name = (f'{str_game_name}_{str_trailer}_{str_platform}_{str_dimensions}_{str_age_rating}_{str_duration}_{str_language}')    
           #! final_file_name = (f'{str_game_name}_{str_trailer}_{str_platform}_{str_dimensions}_{str_age_rating}_{str_duration}_{str_language}_{str_extension}')    
            pyperclip.copy(final_file_name)
            
            print(final_file_name)
            txt_fieldName0_2.grid(row=1,column=1)
            txt_fieldName0_2.config(text="Filename copied to clipboard!")

            
            

        elif g.get() ==2:
            
            filename_only,extension = os.path.splitext(str(filename))
            final_file_name = (f'{str_game_name}_{str_trailer}_{str_platform}_{str_dimensions}_{str_age_rating}_{str_duration}_{str_language}')    
            print(final_file_name)
            os.rename(filename,os.path.join(os.path.dirname(filename_only),final_file_name+extension))
            txt_fieldName0_2.grid(row=1,column=1)
            txt_fieldName0_2.config(text="File renamed!")

        # txt_fieldName0_2.after(3000,txt_fieldName0_2.grid_remove())
    
    #   print("f {drop})
    

btn_generate_name = Button(frame4, textvariable= default_final_button_text, padx =20,pady=10, command=fn_generate_button).grid(row=0,column=1)
if g.get() ==1:
    default_final_button_text.set("Copy Filename to clipboard")
else:
    default_final_button_text.set("Rename File")
txt_fieldName0_2 = Label(frame4, text ="File renamed!", pady=5)

# txt_fieldName0_2.config(text="tres")
# input_fieldName0.get()
# myLabel.pack()
show_workInProgress(1)
root.mainloop()
