from Config import *

#Written by Eric Bland
class CalcApp:

    def __init__(self, master):    
        
        master.title('Statistical Function Calculator')
        master.resizable(False, False)

        notebook = ttk.Notebook(master)
        notebook.pack()
        self.frame_ANOVA = ttk.Frame(notebook)
        notebook.add(self.frame_ANOVA, text = "ANOVA")

        ttk.Label(self.frame_ANOVA, text = 'Input data delimited by commas. Seperate lists by semi-colon \";\"', 
              font=('calibri',10,'bold')).grid(row = 0, column = 0, sticky = 'w')
        ttk.Label(self.frame_ANOVA, text = 'Output').grid(row = 3, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_ANOVA, text = 'written by Eric Bland', font = ('calibri', 8)).grid(row = 10, column = 0, padx = 5, sticky = 'ne')

        ttk.Button(self.frame_ANOVA, width = 10, text = 'Calculate', command=self.click_calculate).grid(column = 0, row = 3, sticky = 'sw')
        
        self.textbox1 = Text(self.frame_ANOVA, width = 40, height = 6, wrap = 'word')
        self.textbox1.grid(column = 0, row = 2)
        self.textbox2 = Text(self.frame_ANOVA, width = 50, height = 12, wrap = 'word')
        self.textbox2.grid(row = 5, column = 0)


        self.frame_graph = ttk.Frame(notebook)
        notebook.add(self.frame_graph, text = "Graph Function")
        ttk.Button(self.frame_graph, width = 10,
                         text = 'Graph', command=self.click_graph).grid(column = 1, row = 8, sticky = 'ne')
        ttk.Label(self.frame_graph, text = 'Input single variable function', 
              font=('calibri',10,'bold')).grid(row = 0, column = 0, pady=5)
        ttk.Label(self.frame_graph, text = 'x1: ', 
              font=('calibri',10)).grid(row = 2, column = 0, sticky='sw')
        ttk.Label(self.frame_graph, text = 'x2: ', 
              font=('calibri',10)).grid(row = 2, column = 1)
        ttk.Label(self.frame_graph, text = 'x-axis scale: ', 
              font=('calibri',10)).grid(row = 5, column = 0, sticky='sw')
        ttk.Label(self.frame_graph, text = 'y-axis scale: ', 
              font=('calibri',10)).grid(row = 5, column = 1)
        self.scaleX = ttk.Entry(self.frame_graph, width = 10)
        self.scaleX.grid(row = 6, column = 0)
        self.scaleX.insert(END, '1')
        self.scaleY = ttk.Entry(self.frame_graph, width = 10)
        self.scaleY.grid(row = 6, column = 2, sticky='sw')
        self.scaleY.insert(END, '1')
        self.x1_bound = ttk.Entry(self.frame_graph, width = 10)
        self.x1_bound.grid(row = 3, column = 0)
        self.x1_bound.insert(END,'0')
        self.x2_bound = ttk.Entry(self.frame_graph, width = 10)
        self.x2_bound.grid(row = 3, column = 2, sticky='sw')
        self.x2_bound.insert(END,'0')



    def click_calculate(self):
        datastr = self.textbox1.get(1.0, END)
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
                self.textbox2.delete(1.0, END)
                self.textbox2.insert(END, ("F-statistic = {0}\nMean Square between = {1}\n"
                                           "Sum of Squares between = {2}\ndf Numerator = {3}\nMean Square within = {4}"
                                           "\nSum of Squares within = {5}\ndf Denominator = {6}\nGrand Mean = {7}"
                                           "\nData: ").format(*result))
                self.textbox2.insert(END, datastr)
            except ZeroDivisionError:
                self.textbox2.delete(1.0, END)
                self.textbox2.insert(END,"Must have at least two lists of data to calulate ANOVA")
        except ValueError:
            self.textbox2.delete(1.0, END)
            self.textbox2.insert(END, "Invalid input")


    def click_graph(self):
        top = Toplevel()
        h, w = 500, 500
        centerX, centerY = w / 2, h / 2
        scaleX, scaleY = float(self.scaleX.get()),float(self.scaleY.get())
        subline_X, subline_Y = scaleX * 10, scaleY * 10 #The scale of sublines
        canvas = Canvas(top, height = h, width = w)
        canvas.pack()
        canvas.create_line(0,centerY,w,centerY,fill='black')
        canvas.create_line(centerX,0,centerX,h)
        
        thickness, xpos, ypos = 5, -centerX, -centerX
        while(True):
            if round(ypos, 0) > h: break
            ypos += subline_Y
            canvas.create_line(centerX, ypos, centerX + thickness, ypos)
        while(True):
            if round(xpos, 0) > w: break
            xpos += subline_X
            canvas.create_line(xpos, centerY, xpos, centerY - thickness)


        a, b, iteration, n  = float(self.x1_bound.get()), float(self.x2_bound.get()), 0, 100
        step = (b - a) / n
        x1 = a - step
        x2 = a
        while(True):
            if iteration == 100 or round(x2,8) == b: break
            x1 += step
            x2 += step
            y1, y2 = -1 * thisfunc(x1), -1 * thisfunc(x2)
            canvas.create_line(x1 * scaleX + centerX,y1 * scaleY + centerY,x2 * scaleX + centerX,
                               y2 * scaleY + centerY,fill='black',width=2)
            iteration += 1
        return 1

def main():
    
    root = Tk()
    app = CalcApp(root)
    root.mainloop()
  
def thisfunc(x):
    val = x ** 2 + 2 #normalpdf(x, 0, 1)
    
    return val
  
main()