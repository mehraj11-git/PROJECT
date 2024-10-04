# in this project 
# first we will import the useful method and modules
import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
main_app = tk.Tk()
main_app.geometry('1200x800')
main_app.title('NJF text editor')
main_app.wm_iconbitmap('icon.ico')

# so we gonna do step by step for easy understanding
# step 1---main menu ----end of the main menu
# step 2 --tool bar----end of the tool bar
# step 3---text editor ----end of the text editor
# step 4 --main status bar----end of the main status bar
# step 5 --main menu functionality----end of the main menu functionality


# in this first step-1 we donot use the grid or pack method while we create the menu instead we use the config method
# first we make the menu for the file and we give the tear value and other value
# bcz we dont want to tear off the file commands and use ,hence we give false value 1

# now we have to cascade it,if we donot do that then it will not showed #2
# in cascade method we have to give the label and the menu detail where we have to do.

# now we have to add the commands for file,edit,view and color theme 
# for this drop down commands we use the icons ,hence we write the code first for icons #3

# now gives the command for this icons #4
# in command code first we have to give the label and a image  
# after that we use the command=tk.left ,bcz of this code the icons will not overlap with each other
# we use accelerator for short cut key

# we followed the same code for edit as we used for file
# now, in view we gonna add two drop down commands 
# ---tool bar---
# ---status bar---

# we make a icons for the view !!!but we will also make check button here
# bcz,the user gonna select or not [for instance :as it upto us to use navigation buttons or not in our mobile phone]

# color theme 
# in this color theme
# first we give the icon path
# then we make the variable followed by tuple
# after that we make the dictionary ,we make this to make the color diff btw text and background.
# in dict---in the position of key we write the code for text and on the position of value we write the code for the background
# you can get the color code on google by searching the colot picker code something like that..
# we make a another varibale to iterate the dict in order to get the colors 

# after that, we change the positions of commands that we add in every steps of menubar(file,edit,view and color theme)
# why we chamge the positions of that commands???
# bcz we donot use the OOP we are using simple method to create the project,hence,for clear understanding we make it simple.
# where will we move that codes ???
# we make one section main menu functionality --- in that section we add this codes  
main_menu=tk.Menu()
file =tk.Menu(main_menu,tearoff=False)  #1

# icons code #3
# ---file icons---
new_icon=tk.PhotoImage(file='icons2/new.png')
open_icon=tk.PhotoImage(file='icons2/open.png')
save_icon=tk.PhotoImage(file='icons2/save.png')
save_as_icon=tk.PhotoImage(file='icons2/save_as.png')
exit_icon=tk.PhotoImage(file='icons2/exit.png')





# icon code  #3
# ---edit icon---
copy_icon=tk.PhotoImage(file='icons2/copy.png')
paste_icon=tk.PhotoImage(file='icons2/paste.png')
cut_icon=tk.PhotoImage(file='icons2/cut.png')
clear_all_icon=tk.PhotoImage(file='icons2/clear_all.png')
find_icon=tk.PhotoImage(file='icons2/find.png')

edit =tk.Menu(main_menu,tearoff=False)  #1


# --view icons-- #5
tool_bar_icon=tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')

view =tk.Menu(main_menu,tearoff=False)  #1


# ---color theme---
light_default_icon=tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon=tk.PhotoImage(file='icons2/light_plus.png')
dark_icon=tk.PhotoImage(file='icons2/dark.png')
red_icon=tk.PhotoImage(file='icons2/red.png')
monokai=tk.PhotoImage(file='icons2/monokai.png')
night_blue=tk.PhotoImage(file='icons2/night_blue.png')
color_theme =tk.Menu(main_menu,tearoff=False)  #1

color_choice=tk.StringVar()
color_tuple=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai,night_blue,)
color_dict={
    'light Default': ('#000000','#ffffff'),
    'light plus' :('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Monokai':('#d3b774','#474747'),
    'Night blue':('#ededed','#6b9dc2')

}



# cascade #2
main_menu.add_cascade(label='file',menu=file)
main_menu.add_cascade(label='edit',menu=edit)
main_menu.add_cascade(label='view',menu=view)
main_menu.add_cascade(label='color_theme',menu=color_theme)



###########**********tool bar*********###########

# we import the font ,with this help we will get the font family (diff families of font ---aerial,roman ect....)
# first we make the variable and store that font families in that
tool_bar=ttk.Label(main_app)
tool_bar.pack(side=tk.TOP,fill=tk.X)

font_tuples=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuples
font_box.current(font_tuples.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

# print(tk.font.families()) 

# now we make the tool bar to arjust the size of the font
# we have to follow the same steps but with diff values
size_tuple=tuple(range(8,80,2))
size_family=tk.IntVar()
size_box=ttk.Combobox(tool_bar,width=14,textvariable=size_family,state='readonly')
size_box['values']=size_tuple
size_box.current(0)
size_box.grid(row=0,column=1,padx=5)


# now we make the buttons bold,italic ,underline and font color button with their icons
# we make the buttons with their icons it means we want the path of that icons  #10
# after that we set the position of the btn and set the icon --this will done by using the button method

bold_icon=tk.PhotoImage(file='icons2/bold.png') #10
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

italic_icon=tk.PhotoImage(file='icons2/italic.png') #10
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

underline_icon=tk.PhotoImage(file='icons2/underline.png') #10
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

font_color_icon=tk.PhotoImage(file='icons2/font_color.png') #10
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

# align buttons
align_left_icon=tk.PhotoImage(file='icons2/align_left.png')
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

align_center_icon=tk.PhotoImage(file='icons2/align_center.png')
align_centre_btn=ttk.Button(tool_bar,image=align_center_icon)
align_centre_btn.grid(row=0,column=7,padx=5)

align_right_icon=tk.PhotoImage(file='icons2/align_right.png')
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)

##########*********end of the tool bar********###############


##########**********TEXT EDITOR******##################

# we must follow tthis step if we want to make a text editor
# we have a class called as text in tkinter 
# we have to call this class and store in a variable look at 11
# after that we have to make a scroll bar
# we have a class scrollbar 
# we use the pack method here fill with both expand (means=horizontal and vertical)
# we have to show ,we make this scroll bar for text editor look at 12

# sometime we use grid and sometime pack ?/y???
# it depends on the situetion means if we want to add row and column we use the grid
# whereas if we are talkinng about the sides then we use the pack
text_editor=tk.Text(main_app)
text_editor.config(wrap='word',relief=tk.FLAT)
scroll_bar=tk.Scrollbar(main_app)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)

scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

###########**********END of the TEXT EDITOR*********############

# font family and font size functionality
# we difine the func to change the font of the text editor
# we can use any parameters here the main func done by bind 
# after that we bind this func with combobox
current_font_family='Arial'
current_font_size=12

def change_font(event=  None):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)

def change_fontsize(event=  None):
    global current_font_size
    current_font_size=size_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

size_box.bind("<<ComboboxSelected>>",change_fontsize)

# ###########   BUTTON FUNCTIONALITY##########
# --bold functionality---
# we have a font class in tk inter we call it and set the text editor in font 
# and store in a variable 
# we have to this step in func..for that first define the func
def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
bold_btn.configure(command=change_bold)

# italic functionaility 
def change_italic():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['weight']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))
italic_btn.configure(command=change_italic)

# underline functionality 
def change_underline():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline']==1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
underline_btn.configure(command=change_underline)

# change color font functionality
# we import the class colorchooser to change the color font
# first def the func
# and variaable as well followed by configured the test editor and we have to give the index of the color var 
# after that configure the font color btn that we made already and give the command 
def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
font_color_btn.configure(command=change_font_color)

# align functionality
# to make it in func first the make the variable and store that text editor in that 
# first we have to delete the test editor data and then have to insert
def align_func_left():
    text_contant=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_contant,'left')

align_left_btn.configure(command=align_func_left)    

# center align functionality
def align_func_center():
    text_contant=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_contant,'center')
    
align_centre_btn.configure(command=align_func_center)    
# right aling functonality
def align_func_right():
    text_contant=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_contant,'right')
    
align_right_btn.configure(command=align_func_right)    

# now we make the status bar functionality

text_editor.configure(font=('Arial',12))
# --------------STATUS BAR------------------------------
# first def the func and get the values of text editor 
# we use 'end-1c' in order to get just character and word counts.
# and then split them ,for that we must know the length of the text editor.
# hence,we sue the len func and store it in a variable 13
# we have to modified the text editor otherwise it just count as 1
# if we dont want to count the space then use the replace method #14
status_bar=ttk.Label(main_app,text='status bar')
status_bar.pack(side=tk.BOTTOM)
text_changed=False
def changed(event=None):
    global text_changed
    text_changed=True
    if text_editor.edit_modified():
        words=len(text_editor.get(1.0,'end-1c').split())
        charactors=len(text_editor.get(1.0,'end-1c')) #.replace(' ','') 14
        status_bar.config(text=f'charactors : {charactors} words : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',changed)


#############********main menu functionility*********######################

# to work for main menu func we have to make a global variable
# and then we have to def a func that will be use as command 
# we use event=none bcz if we wanna bind then we use this
# we first add the functionality to the new file
# previous data will be deleted and open a new file for that we have to make a variable again 15

# new functionality

url=''
def new_file(event=None):
    global url
    url='' #15
    text_editor.delete(1.0,tk.END)

#  commands for file with icon #4
file.add_command(label='new',image=new_icon,compound=tk.LEFT,accelerator='ctrl+N',command=new_file)

# open functionality  
# we are making a func for new file ,hence we have to ask the user what type of file it want to open 
# for that we have a class and we will use the os module as well
# we give the title and select the type of file 
# we use the *----it means that any type of file but we mention the txt as well 
# we use try and except method to handle the type error.
# if user selcect the file and he read it and he want to insert it another file how willbe do ??
# by using the try and except func
# we use the except func to handle the file not found error and if user didnt select any file 
# and lastly we have to give the title name 
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='select file',filetypes=(('text file','*.txt'),('All files','*.*'))) #16
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_app.title(os.path.basename(url))        
file.add_command(label='open',image=open_icon,compound=tk.LEFT,accelerator='ctrl+O',command=open_file)

# save functionality

# first change the global url 
# if file exist ,first read the content and changed it in string 
# for the first we ahve to get the text editor data ..we know how to get the data
# after that we have to open that file in write mode
# and encode that file and we have to write in the content
# if file doesnot exist 16
def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='txt',filetypes=(('Text File','*.txt'),('All files''*.*'))) #16
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return                
file.add_command(label='save',image=save_icon,compound=tk.LEFT,accelerator='ctrl+S',command=save_file)
    # save as functionality 
def save_as(event=None):
    global url
    try:
        content=text_editor.get(1.0,tk.END)
        url=filedialog.asksaveasfile(mode='w',defaultextension='txt',filetypes=(('Text File','*.txt'),('All files''*.*'))) #16
        url.write(content)
        url.close()
    except:
        return
    
file.add_command(label='save_as',image=save_as_icon,compound=tk.LEFT,accelerator='ctrl+Alt+S',command=save_as)

# exit functionality
# we have to do alot in this section 
# we have to ask the user whether he want to save the file or not and whether he want stay at that file or not 
# if he did some changes and want to save it..
def exit_func(event=None):
    global url
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel('Warning','Do you want to save the file ?')
            if mbox is True:
                if url:
                  content=text_editor.get(1.0,tk.END)
                  with open(url,'w',encoding='utf-8') as fw:
                    fw.write(content)
                    main_app.destroy()
                else:
                    content2=str(text_editor.get(1.0,tk.END))    
                    url=filedialog.asksaveasfile(mode='w',defaultextension='txt',filetypes=(('Text File','*.txt'),('All files''*.*'))) #16
                    url.write(content2)
                    url.close()   
                    main_app.destroy()
            elif mbox is False:
                 main_app.destroy()
        else:
           main_app.destroy()
    except:
        return       

file.add_command(label='exit',image=exit_icon,compound=tk.LEFT,accelerator='ctrl+Q',command=exit_func)

########find functionality#############


def find_func(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')
    def replace():
        word = find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    find_dialogue=tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

##creating frame
    find_frame=ttk.LabelFrame(find_dialogue,text='Find/Replace')    
    find_frame.pack(pady=20)
##labels
    text_find_label=ttk.Label(find_frame,text='Find : ')
    text_replace_label=ttk.Label(find_frame,text='Replace')
##entry
    find_input=ttk.Entry(find_frame,width=30)
    replace_input=ttk.Entry(find_frame,width=30)
#button
    find_button=ttk.Button(find_frame,text='Find',command=find) 
    replace_button=ttk.Button(find_frame,text='Replace',command=replace)
##label grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)
##entry grid
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)
##button grid
    find_button.grid(row=2,column=0,padx=8,pady=4)                       
    replace_button.grid(row=2,column=1,padx=8,pady=4)                       

    find_dialogue.mainloop()
# commands for edit with icon #4
edit.add_command(label='copy',image=copy_icon,compound=tk.LEFT,accelerator='ctrl+c',command=lambda:text_editor.event_generate('<Control c>'))
edit.add_command(label='paste',image=paste_icon,compound=tk.LEFT,accelerator='ctrl+v',command=lambda:text_editor.event_generate('<Control v>'))
edit.add_command(label='cut',image=cut_icon,compound=tk.LEFT,accelerator='ctrl+x',command=lambda:text_editor.event_generate('<Control x>'))
edit.add_command(label='clear_all',image=clear_all_icon,compound=tk.LEFT,accelerator='ctrl+alt+x',command=lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label='find',image=find_icon,compound=tk.LEFT,accelerator='ctrl+f',command=find_func)

# check button commands
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True



view.add_checkbutton(label='tool_bar',onvalue=True,offvalue=0,variable=show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label='status_bar',onvalue=1,offvalue=False,variable=show_statusbar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)

# color theme 
def change_theme():
    chosen_theme=color_choice.get()
    color_tuple=color_dict.get(chosen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)
count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_tuple[count],variable=color_choice,compound=tk.LEFT,command=change_theme)
    count+=1


main_app.config(menu=main_menu)

# bind shortcut keyssss
main_app.bind('<Control-n>',new_file)
main_app.bind('<Control-o>',open_file)
main_app.bind('<Control-s>',save_file)
main_app.bind('<Control-Alt-s>',save_as)
main_app.bind('<Control-Q>',exit_func)
main_app.bind('<Control-f>',find_func)
main_app.mainloop()