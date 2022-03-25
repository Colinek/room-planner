from guizero import App, Text, TextBox, TitleBox, PushButton

def calculation():
  carpet.value = str(int(length.value) * int(width.value)) + "m\u00b2"
  skirting.value = str((int(length.value) * 2) +(int(width.value) * 2)) +"m"
  paint.value = str(( (int(length.value) * int(height.value)) * 2 ) + ( (int(width.value) * int(height.value)) * 2 )) + "m\u00b3"
app = App('Room Planner', layout = 'grid')
dimensions = TitleBox(app, 'Dimensions', layout = 'grid', grid = [0,0])

length_text = Text(dimensions, "Length: ", grid = [0,0], align = 'left')
length = TextBox(dimensions, '', grid = [1,0], align = 'top')
width_text = Text(dimensions, "Width: ", grid = [0,1], align = 'left')
width = TextBox(dimensions, '', grid = [1,1])
height_text = Text(dimensions, "Height: ", grid = [0,2], align = 'left')
height = TextBox(dimensions, '', grid = [1,2])

calculate = PushButton(app, command = calculation, text = 'Calculate', grid = [1,0])

materials = TitleBox(app, 'Materials', layout = 'grid', grid = [2,0] )
carpet_text = Text(materials, "Carpet: ", grid = [0,0], align = 'left')
carpet = TextBox(materials, '', grid = [1,0])
skirting_text = Text(materials, "Skirting: ", grid = [0,1], align = 'left')
skirting = TextBox(materials, '', grid = [1,1])
paint_text = Text(materials, "Paint: ", grid = [0,2], align = 'left')
paint = TextBox(materials, '', grid = [1,2])
app.display()

