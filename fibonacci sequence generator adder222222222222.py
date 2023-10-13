from tkinter import*
root=Tk()
root.title("Fibonacci") 
root.geometry("600x300")


label2 = Label(root,text="FIBONOCCIS SERIES",fg='white',bg='black')
label2.pack()


entry_box = Entry(root)
entry_box.pack()


label = Label(root,text="<<RESULT>>")
label.pack()


label3 = Label(root,text="Sum is : ")
label3.pack()

def fibonacci() :
    first_num = 0
    second_num = 1
    sum = 0
    sum_final = 0
    num = int(entry_box.get())
    ##print(num)
    counter = 0
    
    while(counter<num):
          label["text"]+=str(sum)+"  "
          label3["text"]=str(sum_final)+"  "
          counter = counter+1
          first_num = second_num
          second_num = sum
          sum = first_num+second_num
          sum_final = sum+sum_final
          print(sum_final)
          
def Reset():
    label["text"]="RESET"
    ##label2["text"]="RESET"
    label3["text"]="RESET"

        
btn = Button(root,text="Do fibonacci",command=fibonacci,bg='red',fg='white')
btn.pack()

btn_reset = Button(root,text="RESET",command=Reset,bg='blue',fg='white')
btn_reset.pack()


root.mainloop()