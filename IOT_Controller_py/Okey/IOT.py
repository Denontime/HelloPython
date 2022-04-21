'''
Descripttion: Null
version: 1.0
Author: Mar Ping
Date: 2021-03-18 11:50:11
LastEditors: Mar Ping
LastEditTime: 2021-03-28 21:13:56
'''
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.figure import Figure
import PySimpleGUI as sg
import random
import sys

STEP_SIZE = 1
SAMPLES = 10000
SAMPLE_MAX = 5500
CANVAS0_SIZE = (1250, 300)
CANVAS_SIZE = (400, 300)

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def DifferentScales():
    import numpy as np
    import matplotlib.pyplot as plt

    # Create some mock data
    t = np.arange(0.01, 10.0, 0.01)
    data1 = np.exp(t)
    data2 = np.sin(2 * np.pi * t)

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('exp', color=color)
    ax1.plot(t, data1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
    ax2.plot(t, data2, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    return fig


sg.theme('BrownBlue')

Frame_Left_Layout = sg.Frame("Left", [[sg.Column([[sg.Listbox(['ip '+str(i) for i in range(1, 16)], key='-ACCT-LIST-', size=(18, 30))],
                                                [sg.Button("Connect"), sg.Exit()]],
                                                size=(150,700), element_justification='center')]]
)

Frame0 = sg.Frame("Voltage",[[ sg.Graph(CANVAS0_SIZE, (0, 0), (SAMPLES, SAMPLE_MAX),
                            background_color='black', key='graph0')]])

Frame1 = sg.Frame("UP_Motor",[[ sg.Graph(CANVAS_SIZE, (0, 0), (SAMPLES, SAMPLE_MAX),
                            background_color='black', key='graph1')]])

Frame2 = sg.Frame("Mid_Motor",[[ sg.Graph(CANVAS_SIZE, (0, 0), (SAMPLES, SAMPLE_MAX),
                            background_color='black', key='graph2')]])

Frame3 = sg.Frame("Down_Motor",[[ sg.Graph(CANVAS_SIZE, (0, 0), (SAMPLES, SAMPLE_MAX),
                            background_color='black', key='graph3')]])

Frame_Right_Layout = sg.Frame("Right",[[Frame0],[Frame1,Frame2,Frame3]])

layout = [[Frame_Left_Layout,Frame_Right_Layout]]

Window = sg.Window("IOT", layout, finalize=True)

V_canvas = Window["graph0"]
Up_canvas = Window["graph1"].TKCanvas
Mid_canvas = Window["graph2"].TKCanvas
Down_canvas = Window["graph3"].TKCanvas

V_canvas.draw_line((SAMPLES//2, 0), (SAMPLES//2,SAMPLE_MAX),color='yellow')
V_canvas.draw_line((0,SAMPLE_MAX//2), (SAMPLES, SAMPLE_MAX//2),color='red')

#/**************************************  *************************************/
fig = Figure(figsize=(4,3))
ax = fig.add_subplot(111)
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.grid()
Fig_Up = draw_figure(Up_canvas, fig)
Fig_Mid = draw_figure(Mid_canvas, fig)
Fig_Down = draw_figure(Down_canvas, fig)
#/**************************************  *************************************/

prev_response_time = None
i = 0
prev_x, prev_y = 0, 0
graph_value = 2000
figures = []
data_points = 40
while True:
    event, values = Window.read(timeout=0)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
#/**************************************  *************************************/
    # slider_elem.update(i)       # slider shows "progress" through the data points
    ax.cla()                    # clear the subplot
    ax.grid()                   # draw the grid
    # data_points = int(values['-SLIDER-DATAPOINTS-']) # draw this many data points (on next line)
    # ax.plot(range(data_points), dpts[i:i+data_points], color='purple')
    Fig_Up.draw()
    Fig_Mid.draw()
    Fig_Down.draw()
#/**************************************  *************************************/

    # graph_offset = random.randint(-10, 10)
    # graph_value = graph_value + graph_offset

    # if graph_value > SAMPLE_MAX:
    #     graph_value = SAMPLE_MAX
    # if graph_value < 0:
    #     graph_value = 0

    # new_x, new_y = i, graph_value
    # prev_value = graph_value

    # if i >= SAMPLES:
    #     V_canvas.delete_figure(figures[0])
    #     figures = figures[1:]
    #     for count, figure in enumerate(figures):
    #         V_canvas.move_figure(figure, -STEP_SIZE, 0)
    #     prev_x = prev_x - STEP_SIZE

    # last_figure = V_canvas.draw_line((prev_x, prev_y), (new_x, new_y), color='white')
    # figures.append(last_figure)
    # prev_x, prev_y = new_x, new_y
    # i += STEP_SIZE if i < SAMPLES else 0

Window.close()


