from Config import *
import math


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

        self.canvas_norm = Canvas(notebook)
        notebook.add(self.canvas_norm, text = "Normal Dist")
        ttk.Button(self.canvas_norm, width = 10,
                         text = 'Graph', command=self.click_graph).place(x = 100, y = 200)
        ttk.Label(self.canvas_norm, text = 'Input Mean and Standard Deviation for Normal Curve', 
              font=('calibri',10,'bold')).place(x = 50, y = 10)
        ttk.Label(self.canvas_norm, text = 'Mean: ').place(x = 60, y=50)
        ttk.Label(self.canvas_norm, text = 'Std Dev: ').place(x = 200, y=50)
        ttk.Label(self.canvas_norm, text = 'Area Lbound: ').place(x = 20, y=150)
        ttk.Label(self.canvas_norm, text = 'Area UBound: ').place(x = 170, y=150)
        self.entry_mean = ttk.Entry(self.canvas_norm, width = 10)
        self.entry_mean.place(x = 100, y = 50)
        self.entry_std = ttk.Entry(self.canvas_norm, width = 10)
        self.entry_std.place(x = 250, y = 50)
        self.entry_area_a = ttk.Entry(self.canvas_norm, width = 10)
        self.entry_area_a.place(x = 100, y = 150)
        self.entry_area_b = ttk.Entry(self.canvas_norm, width = 10)
        self.entry_area_b.place(x = 250, y = 150)
        self.radio1 = ttk.Radiobutton(self.canvas_norm, text = 'NormalCDF')
        self.radio1.place(x = 100, y = 100)
        self.radio2 = ttk.Radiobutton(self.canvas_norm, text = 'NormalPDF')
        self.radio2.place(x = 100, y = 120)

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
        mean = float(self.entry_mean.get())
        std = float(self.entry_std.get())
        normalfunc = lambda x: normalpdf(x, mean, std)
        normalcurve = GraphFunc(normalfunc, mean - 3 * std, mean + 3 * std,
                                -2 * normalfunc(mean), 2 * normalfunc(mean),
                                self.entry_area_a.get(), self.entry_area_b.get())
        
 #------------------------------------------------------------------------------------------------------
class GraphFunc:
    def __init__(self, func, x_Lbound, x_Ubound, y_Lbound, y_Ubound, area_a, area_b):
        self.top = Toplevel()
        self.top.resizable(False, False)
        self.func = func
        self.xL = x_Lbound
        self.xU = x_Ubound
        self.yL = y_Lbound
        self.yU = y_Ubound
        self.area_a = area_a
        self.area_b = area_b
        self.height, self.width = 500, 600
        self.draw_canvas()
             

    def draw_canvas(self):    

        h, w = self.height, self.width
        centerX, centerY = w / 2, h / 2
        self.canvas = Canvas(self.top, height = h, width = w)
        self.canvas.pack()
        self.window_open = ttk.Button(self.canvas, text='Window', command=self.draw_window_frame)
        self.window_open.place(x=self.width - 100, y=self.height - 30)
        
        iteration, n = 0, 400
        a, b = float(self.xL), float(self.xU)
        c, d = float(self.yL), float(self.yU)
        step = (b - a) / n
        x1, x2 = a - step, a
        unitX, unitY = 1, 1
        if (b - a) > 100: unitX = 10
        if (d - c) > 100: unitY = 10
        scaleY, scaleX = h / (d - c), w / (b - a)
        
        #draw x & y axes
        x_axis, y_axis = (d * scaleY), w - (b * scaleX)
        self.canvas.create_line(y_axis,0,y_axis,h, fill='black')
        self.canvas.create_line(0,x_axis,w,x_axis,fill='black')

        while(True):
            if iteration == n or round(x2,8) == b: break
            x1 += step
            x2 += step
            y1, y2 = -1 * self.func(x1), -1 * self.func(x2)
            
            #draw area (if inputted)
            if self.area_a != "" and self.area_b != "" and self.area_a != self.area_b:
                if x1 > float(self.area_a) and x1 <= float(self.area_b): 
                    self.canvas.create_line(x1 * scaleX + y_axis, x_axis,
                                               x1 * scaleX + y_axis, y1 * scaleY + x_axis + 1
                                               , fill='grey', width=2)
            #draw curve
            self.canvas.create_line(x1 * scaleX + y_axis,y1 * scaleY + x_axis,x2 * scaleX + y_axis,
                               y2 * scaleY + x_axis,fill='black',width=2)
            iteration += 1

        #draw unit sublines
        subline_len, xpos, ypos = 5, y_axis + (math.floor(a) * scaleX * unitX), x_axis - (math.ceil(d) * scaleY * unitX)
        while(True):
            xpos += scaleX * unitX
            if xpos > w: break
            if xpos == y_axis: continue
            self.canvas.create_line(xpos, x_axis, xpos, x_axis - subline_len)
        while(True):
            ypos += scaleY * unitY
            if ypos > h: break
            if ypos == x_axis: continue
            self.canvas.create_line(y_axis, ypos, y_axis + subline_len, ypos)
       
        if self.area_a != "" and self.area_b != "" and self.area_a != self.area_b:
                area = round(Sareaundercurve(self.func, float(self.area_a), float(self.area_b)), 5)
                Label(self.canvas, text = 'Area: ' + str(area), font = ('calibri', 8)).place(x = self.width - 250, y = self.height - 20)

        Label(self.canvas, text = 'x: [' + str(round(a,4)) + ', ' + str(round(b,4)) + '], units: ' + str(unitX),
              font = ('calibri',8)).place(x = self.width - 250, y = self.height - 60)
        Label(self.canvas, text = 'y: [' + str(round(c,4)) + ', ' + str(round(d,4)) + '], units: ' + str(unitY),
              font = ('calibri',8)).place(x = self.width - 250, y = self.height - 40)


    def draw_window_frame(self):
        self.canvas.destroy()
        self.frame_window = ttk.Frame(self.top)
        self.frame_window.place(x=self.width / 2 - 150, y=self.height / 2 - 100)
        ttk.Button(self.frame_window, width = 10, text = 'Recalculate',
            command=self.recalc_canvas).grid(row = 8, column = 2, pady=5)
        ttk.Button(self.frame_window, width = 10, text = 'Recalculate',
            command=self.recalc_canvas).grid(row = 8, column = 2, pady=5)
        ttk.Label(self.frame_window, text = 'Lower x-boundary: ', 
              font=('calibri',10)).grid(row = 3, column = 0, sticky='sw')
        ttk.Label(self.frame_window, text = 'Upper x-boundary: ', 
              font=('calibri',10)).grid(row = 3, column = 1)
        ttk.Label(self.frame_window, text = 'Lower y-boundary: ', 
              font=('calibri',10)).grid(row = 6, column = 0, sticky='sw')
        ttk.Label(self.frame_window, text = 'Upper y-boundary: ', 
              font=('calibri',10)).grid(row = 6, column = 1)
        ttk.Label(self.frame_window, text = 'Window', 
              font=('calibri',10,'bold')).grid(row = 2, column = 0, sticky = 'ne')
        self.x_Lbound = ttk.Entry(self.frame_window, width = 10)
        self.x_Lbound.grid(row = 4, column = 0)
        self.x_Lbound.insert(END,round(self.xL,5))
        self.x_Ubound = ttk.Entry(self.frame_window, width = 10)
        self.x_Ubound.grid(row = 4, column = 2, sticky='ne')
        self.x_Ubound.insert(END,round(self.xU,5))
        self.y_Lbound = ttk.Entry(self.frame_window, width = 10)
        self.y_Lbound.grid(row = 7, column = 0)
        self.y_Lbound.insert(END, round(self.yL,5))
        self.y_Ubound = ttk.Entry(self.frame_window, width = 10)
        self.y_Ubound.grid(row = 7, column = 2, sticky='ne')
        self.y_Ubound.insert(END, round(self.yU,5))
    

    def recalc_canvas(self):
        self.xL = self.x_Lbound.get()
        self.xU = self.x_Ubound.get()
        self.yL = self.y_Lbound.get()
        self.yU = self.y_Ubound.get()
        if float(self.xL) == float(self.xU) or float(self.yL) == float(self.yU):
            Label(self.frame_window, text = "x-bounds or y-bounds are incorrect",
                  font = ('calibri', 10, 'bold')).grid(row = 9, column = 0, columnspan = 2)
        else:
            if float(self.xL) > float(self.xU): 
                self.xL, self.xU = self.xU, self.xL
            if float(self.yL) > float(self.yU):
                self.yL, self.yU = self.yU, self.yL
            self.canvas.destroy()
            self.frame_window.destroy()
            self.draw_canvas()
 


#---------------------------------------------------------------------------------------------------
def main():
    root = Tk()
    app = CalcApp(root)
    root.mainloop()
  
if __name__ == "__main__":
    main()
