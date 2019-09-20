#CSC11300 Programming Languages Final Project by Mahin Khan and Danish Faruqi
from tkinter import *
from turtle import Turtle, Screen
from itertools import cycle


# Storing the n into a var using tKinter
root = Tk()
root.title('Input the amount of letters you want to measure')
root.geometry("640x640+0+0")

heading = Label(root, text="Enter N", font=("arial", 40, "bold"), fg="black").pack()
label = Label(root, text="Enter a number, N, that returns the top n letters that appeared ", font = (20)).pack()
label2 = Label(root, text="in the file \"Words.txt\" ", font = (20)).pack()
n = IntVar()
entry_box = Entry(root, textvariable=n, width = 25, bg = "lightgrey").pack()


def do_it():
    if n.get() >0:
        # collecting all the frequencies
        words = open('Words.txt', "r")
        words.seek(0)
        var = words.read()
        words.close()

        arr = [0]*27
        freq_arr = [0]*27
        for i in var:
            if i == " ":
                arr[26] = arr[26] + 1
                freq_arr[26] = freq_arr[26] + 1

            if ord(i) > 64 and ord(i) < 91:
                arr[ord(i.lower()) - 97] = arr[ord(i.lower()) - 97] + 1
                freq_arr[ord(i.lower()) - 97] = freq_arr[ord(i.lower()) - 97] + 1

            if ord(i) > 96 and ord(i) < 123:
                arr[ord(i) - 97] = arr[ord(i) - 97] + 1
                freq_arr[ord(i) - 97] = freq_arr[ord(i) - 97] + 1

        # Converted them into probabilities - can't do len of string so just create another var and do it that way
        #  have two lists, one that has the letter positions, and the other that holds their probabl
        sum_of_all = 0
        for i in range(27):
            sum_of_all = sum_of_all+arr[i]
        for i in range(27):
            freq_arr[i] = freq_arr[i] / sum_of_all

#          Finding max ns
        top_ns = [" "]*int(n.get())
        freq_arr.sort(reverse = True)  # already sorted array of probabilities
        for i in range(0, n.get()):
            index = arr.index(max(arr)) # get the index of maz
            if index == 26:
                top_ns[i] = "Space"
                arr[index] = -1
            else:
                top_ns[i] = chr(int(index + 97))   # put the index of max in top n list
                arr[index] = -1 # remove that spot from actual array so it doesn't come up as max the next time


        freq_arr = freq_arr[0:n.get()]

        label3 = Label(root, text=n.get()).pack()
        label4 = Label(root, text=top_ns).pack()
        label5 = Label(root, text=freq_arr).pack()

        #  End of Tkinter use -  now making the pie chart

        prob_of_letters = [0]*int(n.get()+1)
        for i in range(0,n.get()):
            prob_of_letters[i] = (top_ns[i], freq_arr[i])
        prob_of_letters[n.get()] = ("All other letters", 1-sum(freq_arr))

        colors = cycle(['red', 'green', 'blue', 'yellow', 'white', 'purple', 'orange'])

        radius = 150
        radius2 = radius * 1.25


        all = sum(fraction for _, fraction in prob_of_letters)

        pie_chart = Turtle()
        pie_chart.clear()
        pie_chart.penup()
        pie_chart.sety(-radius)
        pie_chart.pendown()

        for _, fraction in prob_of_letters:
            pie_chart.fillcolor(next(colors))
            pie_chart.begin_fill()
            pie_chart.circle(radius, fraction * 360 / all)
            pos = pie_chart.position()
            pie_chart.goto(0, 0)
            pie_chart.end_fill()
            pie_chart.setposition(pos)


        pie_chart.penup()
        pie_chart.sety(-radius2)


        for label, fraction in prob_of_letters:
            pie_chart.circle(radius2, fraction * 360 / all / 2)
            pie_chart.write(label,  align="right")
            pie_chart.circle(radius2, fraction * 360 / all / 2)

        for label, fraction in prob_of_letters:
            pie_chart.circle(radius2, fraction * 360 / all / 2)
            pie_chart.write(fraction, align="left")
            pie_chart.circle(radius2, fraction * 360 / all / 2)

        pie_chart.hideturtle()

        screen = Screen()
        screen.exitonclick()


        return
    else:
        label3 = Label(root, text=n.get()).pack()

        prob_of_letters = [("All other letters", 1)]

        colors = cycle(['red', 'green', 'blue', 'yellow', 'white', 'purple', 'orange'])

        radius = 150
        radius2 = radius * 1.25


        all = sum(fraction for _, fraction in prob_of_letters)

        pie_chart = Turtle()
        pie_chart.penup()
        pie_chart.sety(-radius)
        pie_chart.pendown()

        for _, fraction in prob_of_letters:
            pie_chart.fillcolor(next(colors))
            pie_chart.begin_fill()
            pie_chart.circle(radius, fraction * 360 / all)
            pos = pie_chart.position()
            pie_chart.goto(0, 0)
            pie_chart.end_fill()
            pie_chart.setposition(pos)


        pie_chart.penup()
        pie_chart.sety(-radius2)

        for label, fraction in prob_of_letters:
            pie_chart.circle(radius2, fraction * 360 / all / 2)
            pie_chart.write(label, align="right")
            pie_chart.circle(radius2, fraction * 360 / all / 2)

        for label, fraction in prob_of_letters:
            pie_chart.circle(radius2, fraction * 360 / all / 2)
            pie_chart.write(fraction, align="left")
            pie_chart.circle(radius2, fraction * 360 / all / 2)

        pie_chart.hideturtle()

        screen = Screen()
        screen.exitonclick()
        return


work = Button(root, text ="Enter", width = 15, height = 1, bg= "white", command = do_it).pack()


root.mainloop()