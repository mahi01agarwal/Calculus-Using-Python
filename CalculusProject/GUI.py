from tkinter import *
import Plot
import Limit
import DerivativeOfFunction
import CriticalPoints
import MaximaAndMinimaPOintsOfAFunction
import DoubleDerivative
import IncrDec
import Concavity
import HorizontalAndObliqueAsymptotes
import VerticalAsymptotes
import ttkbootstrap  as ttkb




root = Tk()
root.title("Properties of functions")
root.geometry("1500x800")

ttkb.Style(theme="superhero")


ttkb.Label(root,text="Graphing Calculator\n",font= ('Helvetica 30 underline'),bootstyle="warning").pack()


Label(root,text = "Enter the function : ",font=25,width=30).pack()
String = StringVar()
Entry(root,textvariable=String,font=22,width=30).pack()


Label(root,text = "Enter Range: ",font=25,width=30).pack()
FirstPoint = IntVar()
SecondPoint =IntVar()
Entry(root,textvariable=FirstPoint,font=22,width=30).pack()
Entry(root,textvariable=SecondPoint,font=22,width=30).pack()

Label(root,text="").pack()

First_Frame = Frame(root,width=50)
First_Frame.pack(side=LEFT,padx=15,pady=15)

Second_Frame = Frame(root,width=50)
Second_Frame.pack(side = RIGHT,padx=15,pady=15)


#Plotting the graph
Button(root,text="Plot",command=lambda:Plot.Plot(String.get()),font=" comicsans 13 bold ",fg="white",bg = "purple",width=30).pack()


#Finding Limit:
Label(root,text = "\n\n\nPoint at which you want limit : ",font =24,width=30).pack()
LimitingPoint = IntVar()
Entry(root,textvariable=LimitingPoint,font=22,width=30).pack()
def FindLimit():
    Ans =Limit.limit(String.get(),LimitingPoint.get())
    Label(root,text=f"\nLimit at {LimitingPoint.get()}: {Ans}",font="comicsans 15 ",width=30).pack()
Label(root,text="").pack()
Button(root,text="Find Limit",command=FindLimit,font=" comicsans 13 bold ",fg="white",bg = "purple",width=30).pack()


#Finding CriticalPoints
Label(First_Frame,text="").pack()
def FindCriticalPoints():
    Ans = CriticalPoints.criticalPoints(String.get())
    Label(First_Frame,text=f"Critical Points: {Ans}",font="comicsans 15 ",width=30).pack()
Button(First_Frame,text="Find CriticalPoints",command = FindCriticalPoints,font=" comicsans 13 bold ",fg="white",bg = "purple",width=30).pack()


#Finding Derivatives
Label(First_Frame,text="").pack()
def FindDerivative():
    der = DerivativeOfFunction.derivative(String.get())
    Label(First_Frame,text=f"Derivative : {der}",font="comicsans 15 ",width=30).pack()  
Button(First_Frame,text="Find Derivative",command = FindDerivative,font=" comicsans 13 bold ",fg="white",bg = "purple",width=30).pack()


#Finding DoubleDErivative
Label(First_Frame,text="").pack()
def FindDoubleDerivative():
    doubDer = DoubleDerivative.FindDoubleDerivative(String.get())    
    Label(First_Frame,text=f"Double Derivative : {doubDer}",font="comicsans 15 ",width=30).pack()
Button(First_Frame,text=" Find Double Derivative ",command = FindDoubleDerivative,font=" comicsans 13 bold ",fg="white",bg = "purple",width=30).pack()


#Finding Maxima and Minima points
Label(Second_Frame,text="").pack()
def FindMaximaAndMinima():
    Maxima = MaximaAndMinimaPOintsOfAFunction.FindMaxima(String.get())
    Label(Second_Frame,text=f"Points of Maxima : {Maxima}",font="comicsans 15 ",width=30).pack()
    Minima = MaximaAndMinimaPOintsOfAFunction.FindMinima(String.get())
    Label(Second_Frame,text=f"Points of Minima : {Minima}",font="comicsans 15 ",width=30).pack()
Button(Second_Frame,text="Find Maxima And Minima",command = FindMaximaAndMinima,font=" comicsans 13 bold ",fg="white",bg = "purple",width=30).pack()


#Finding Increasing Decreasing
Label(First_Frame,text="").pack()
def FindMaximaAndMinima():
    Increasing = IncrDec.Increasing(String.get(),FirstPoint.get(),SecondPoint.get())
    Label(First_Frame,text=f"Increasing: {Increasing}",font="comicsans 15 ").pack()
    Decreasing = IncrDec.Decreasing(String.get(),FirstPoint.get(),SecondPoint.get())
    Label(First_Frame,text=f"Decreasing : {Decreasing}",font="comicsans 15 ").pack()
Button(First_Frame,text="Find Increasing Decreasing Intervals",command = FindMaximaAndMinima,font=" comicsans 13 bold ",fg="white",bg = "purple",width=30).pack()



#Find Concavity
Label(Second_Frame,text="").pack()
def concavity():
    Concave_up= Concavity.ConcaveUp(String.get(),FirstPoint.get(),SecondPoint.get())
    Label(Second_Frame,text=f"Concave Up : {Concave_up}",font="comicsans 15 ").pack()
    Concave_down= Concavity.ConcaveDown(String.get(),FirstPoint.get(),SecondPoint.get())
    Label(Second_Frame,text=f"Concave Down : {Concave_down}",font="comicsans 15 ").pack()
Button(Second_Frame,text="Check Concavity",command = concavity,font=" comicsans 13 bold ",fg="white",bg = "purple",width=30).pack()




#Find Vertical asymptotes

Label(Second_Frame,text="").pack()
def Vertical_Asymptotes():
    Vertical_Asy = VerticalAsymptotes.Vertical(String.get(),FirstPoint.get(),SecondPoint.get())
    Label(Second_Frame,text=f"Vertical asymptotes are x = {Vertical_Asy}",font="comicsans 15 ").pack()
Button(Second_Frame,text="Find Vertical Asymptotes",command = Vertical_Asymptotes,font=" comicsans 13 bold ",fg="white",bg = "purple",width=30).pack()


Label(Second_Frame,text="").pack()
def Horizonatal_ObliqueAsymptotes():
    Asymptotes = HorizontalAndObliqueAsymptotes.Asymptotes(String.get())
    Label(Second_Frame,text=f"Horizontal , Oblique Asymptotes are y = {Asymptotes}",font="comicsans 15 ").pack()
Button(Second_Frame,text="Find Horizontal & Oblique Asymptotes",command = Horizonatal_ObliqueAsymptotes,font=" comicsans 13 bold ",fg="white",bg = "purple",width=30).pack()

root.mainloop()