from Config import *

#Written by Eric Bland
class CalcApp:

    def __init__(self, master):    
        
        master.title('Statistics Functions')
        master.resizable(False, False)

        self.frame_main = ttk.Frame(master)
        self.frame_main.pack()

        Label(self.frame_main, text = 'Input data delimited by commas. Seperate lists by semi-colon \";\"', 
              font=('calibri',10,'bold')).grid(row = 0, column = 0, sticky = 'w')
        Button(self.frame_main, width = 10, height = 1, text = 'Calculate', command=self.click_calculate).grid(column = 0, row = 3)

        self.textbox1 = Text(self.frame_main, width = 40, height = 4, wrap = 'word')
        self.textbox1.grid(column = 0, row = 2)

        self.frame_data = ttk.Frame(master)
        self.frame_data.pack()

        Label(self.frame_data, text = 'Output').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        self.textbox2 = Text(self.frame_data, width = 50, height = 10, wrap = 'word')
        self.textbox2.grid(row = 3, column = 0)
        #self.textbox2.config(state='disabled')
        Label(self.frame_data, text = 'written by Eric Bland', font = ('calibri', 8)).grid(row = 10, column = 0, padx = 5, sticky = 'ne')

    def click_calculate(self):
        datastr = self.textbox1.get(1.0, 'end')
        datastr = datastr.rstrip()
        datastr = datastr.lstrip()
        datastr = datastr.split(sep=";")
        try:
            for str in datastr:
                str = str.lstrip()
                str = str.rstrip()
                str = str.split(sep=",")
                for val in str:
                    val = val.lstrip()
                    val = val.rstrip()
                    if val.isnumeric: val = float(val)
                    str = str[1:]
                    str.append(val)
                datastr = datastr[1:]
                datastr.append(str)
            try:
                result = ANOVA(*datastr)
                self.textbox2.delete(1.0, 'end')
                self.textbox2.insert(END, ("F-statistic = {0}\nMean Square between = {1}\n"
                                           "Sum of Squares between = {2}\ndf Numerator = {3}\nMean Square within = {4}"
                                           "\nSum of Squares within = {5}\ndf Denominator = {6}\nGrand Mean = {7}").format(*result))
            except ZeroDivisionError:
                self.textbox2.delete(1.0, 'end')
                self.textbox2.insert(END,"Must have at least two lists of data to calulate ANOVA")
        except ValueError:
            self.textbox2.delete(1.0, 'end')
            self.textbox2.insert(END, "Invalid input")


def main():
    
    root = Tk()
    app = CalcApp(root)
    root.mainloop()
    
main()