import customtkinter
import os
from cryptography.fernet import Fernet
from tkinter import filedialog

with open("key.key", "rb") as file:
    KEY = file.read()
fernet = Fernet(KEY)

def clearText():
    textbox.delete("0.0", "end")

def saveText():
    messageNum = 1
    while os.path.exists(f"message{messageNum}.txt"):
        messageNum += 1

    text = textbox.get("1.0", "end")
    with open(f"message{messageNum}.txt", "w") as file:
        file.write(text)

def encryptText():
    fernet = Fernet(KEY)
    message = textbox.get("1.0", "end")
    encryptedMessage = fernet.encrypt(message.encode())
    textbox.delete("1.0", "end")
    textbox.insert("1.0", encryptedMessage)

def decryptText():
    fernet = Fernet(KEY)
    text = textbox.get("1.0", "end").strip()
    decrypted = fernet.decrypt(text.encode()).decode()
    textbox.delete("1.0", "end")
    textbox.insert("1.0", decrypted)

def loadText():
    filename = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )

    with open(filename, "r") as file:
        text = file.read()
        textbox.delete("1.0", "end")
        textbox.insert("1.0", text)

app = customtkinter.CTk()
app.geometry("640x480")

sideBar = customtkinter.CTkFrame(app, width=150)
sideBar.pack(side="left", fill="y")

mainFrame = customtkinter.CTkFrame(app)
mainFrame.pack(side="left", fill="both", expand=True)

label = customtkinter.CTkLabel(sideBar, text="MSGCRYPT", fg_color="transparent", font=("Arial", 24, "bold"))
label.pack(padx=20, pady=8)

clearButton = customtkinter.CTkButton(sideBar, text="Clear Note", command=clearText)
clearButton.pack(padx=20, pady=8)

saveButton = customtkinter.CTkButton(sideBar, text="Save Note", command=saveText)
saveButton.pack(padx=20, pady=8)

loadButton = customtkinter.CTkButton(sideBar, text="Load Note", command=loadText)
loadButton.pack(padx=20, pady=8)

encryptButton = customtkinter.CTkButton(sideBar, text="Encrypt Note", command=encryptText)
encryptButton.pack(padx=20, pady=8)

decryptButton = customtkinter.CTkButton(sideBar, text="Decrypt Note", command=decryptText)
decryptButton.pack(padx=20, pady=8)

textbox = customtkinter.CTkTextbox(mainFrame, width=400, corner_radius=0)
textbox.pack(side="left", fill="both", expand=True)

app.mainloop()

#                                  :=:.                       
#                               =%%#=+*#:                     
#                            .#%%.     .#.                    
#                          :#%+.        +#:                   
#                         +%+.        *=  -**:                
#                       :%%.         :%:                      
#                      =%= -%:       :%- :.                   
#               .-*#%%%%- **    #    +%****##%**%%#+=:.       
#         .:+%%#*=.  -%= =%-   =%.  :%:             .=*%%=    
#       *%%*        .*#  =*   .%%    +.                 -%:   
#   .#%%:           :%=  =#  +#-    :*.             .:*%%%:   
#   -%%%%*=. .      =%.  :%*%+     :%*   .:::==+#%%%*--       
#      :=*++%%%%%%%%%%    #%=      :%%%%%%%##*=               
#                  -=*      :+=  .=*-                         
#                   -%%*=#%*=+##%%%*:                         
#                     :-:        :.::                         
                                                             
                                                             
