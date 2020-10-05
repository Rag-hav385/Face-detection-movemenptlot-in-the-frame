from script import  df

from bokeh.plotting import figure,show,output_file

p = figure(x_axis_type = "datetime" , height = 200 , width = 1000 , title = "Motion Detector")

q = p.quad(left = df["Start"],right = df["End"],bottom = 0,top = 1,color = "Blue")

output_file("Graph.html")

show(p)

