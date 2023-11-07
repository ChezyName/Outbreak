import tkinter as tk

#-------------------------------------------------------------------------------
# GLOBALS
WINDOW_WIDTH=640
WINDOW_HEIGHT=480
#-------------------------------------------------------------------------------

#Host Game
def HostGame():
    print("Hosting Game")
    DestroyHostJoin()

def JoinGame():
    print("Joining Game")
    DestroyHostJoin()

def DestroyHostJoin():
    frame.destroy()

def CreateButtons():
    global frame, host, join, ip_title, ip_address
    frame = tk.Frame(mainFrame, width=1, height=1, background="#212121")
    frame.pack(expand=True, padx=0, pady=0)

    host = tk.Button(frame, text="Host Game", command=HostGame)
    join = tk.Button(frame, text="Join Game", command=JoinGame)

    ip_title = tk.Label(frame,text="IP Address",background="#212121",foreground="white")
    ip_address = tk.Entry(frame)

    #Gridding
    ip_title.grid(row = 0, column = 0,padx=5, pady=5)
    ip_address.grid(row = 0, column = 1,padx=5, pady=5)
    host.grid(row = 1, column = 0,padx=5, pady=5)
    join.grid(row = 1, column = 1,padx=5, pady=5)

# Create All HUD Elements
root = tk.Tk(screenName="Outbreak Client")
root.title("Outbreak Client")
root.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))

#CenterWindow
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (WINDOW_WIDTH/2))
y_cordinate = int((screen_height/2) - (WINDOW_HEIGHT/2))
root.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH, WINDOW_HEIGHT, x_cordinate, y_cordinate))

mainFrame = tk.Frame(root, width=1, height=1, background="#212121")
mainFrame.pack(fill="both", expand=True, padx=0, pady=0)

CreateButtons()

root.mainloop()