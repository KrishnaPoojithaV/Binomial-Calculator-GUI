# command to run the program:  python3 181IT223_IT302_P7.py 

import tkinter as tk                    # module imported for creating GUI
window= tk.Tk()                           # instance of module created
window.title('GUI')

base = tk.Canvas(window, width = 550, height = 600)
base.pack()

# Creating fields and spaecifying their positions where users enter the values
value1 = tk.Entry (window) 
base.create_window(300, 200, window=value1)
value2 = tk.Entry (window) 
base.create_window(300, 260, window=value2)
value3 = tk.Entry (window) 
base.create_window(300, 320, window=value3)
value4 = tk.Entry (window) 
base.create_window(300, 500, window=value4)

# Creating the labels which are displayed and whose values are to be entered
name0 = tk.Label(window, text='Binomial Calculator', fg = 'teal')
name0.config(font=('georgia', 30))
base.create_window(280, 100, window=name0)
name1 = tk.Label(window, text='Enter P:')
name1.config(font=('georgia', 20))
base.create_window(160, 200, window=name1)
name2 = tk.Label(window, text='Enter N:')
name2.config(font=('georgia', 20))
base.create_window(160, 260, window=name2)
name3 = tk.Label(window, text='Enter M:')
name3.config(font=('georgia', 20))
base.create_window(160, 320, window=name3)
name4 = tk.Label(window, text='Result:')
name4.config(font=('georgia', 20))
base.create_window(160, 500, window=name4)

def calclateFactorial(num):                 # function calculating factorial of number
    fact = 1
    for no in range(1,num+1):
        fact*=no
    return fact

def solution():  
    probability = value1.get()
    N = value2.get()
    M = value3.get()
    try:
        survive = float(probability)           # checks if float value is entered as probability - otherwise return ValueError
        n = int(N)                          # checks if integer value is entered as N - otherwise return ValueError
        m = int(M)                          # checks if integer value is entered as M - otherwise return ValueError
    except ValueError:
        name5 = tk.Label(window, text= "Invalid input",font=('georgia', 14, 'bold'), bg='white', width = 12)  # display invalid message at the result
        base.create_window(300, 500, window=name5)
    if((survive<0) or (survive>1)):                               # check if probability <0 or >1                
        name5 = tk.Label(window, text= "Invalid input",font=('georgia', 14, 'bold'), bg='white', width = 12)  # display invalid message at the result
        base.create_window(300, 500, window=name5)
    elif((m<0) or (n<0)):                                   # check if m and n are negative
        name5 = tk.Label(window, text= "Invalid input",font=('georgia', 14, 'bold'), bg='white', width = 12)  # display invalid message at the result
        base.create_window(300, 500, window=name5)
    elif(m>n):                                              # check if m > n s
        name5 = tk.Label(window, text= "Invalid input",font=('georgia', 14, 'bold'), bg='white', width = 12)  # display invalid message at the result
        base.create_window(300, 500, window=name5)
    else:
        die = 1-survive
        result = (calclateFactorial(n)/(calclateFactorial(m)*calclateFactorial(n-m))) * pow(survive,m) * pow(die,n-m)

        name5 = tk.Label(window, text= round(result,10),font=('calbiri', 14, 'bold'), bg='white', width = 12) # display calculated value at the result
        base.create_window(300, 500, window=name5)
      
buttonAdd = tk.Button(text='Click Here', command=solution, bg='teal', fg='white', font=('georgia', 18, 'bold'), width = 12) # result is calculated on clicking the button
base.create_window(270, 400, window=buttonAdd)

window.mainloop()