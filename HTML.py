import math
def convert100_to_col_12(width):
    if(((width*12)%100) > 50):
        return math.ceil(width*12/100)
    elif (((width*12)%100) < 50):
        return math.floor(width*12/100)
    # return "col-" + str (int( (width/100)*12))
#There was a problem with floating percentage, their sum would never equal 12 like 60 - 40

class HTML_Generator():
    def __init__(self):
        self.html_header = '''<!DOCTYPE html><html><head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Bootstrap</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
        crossorigin="anonymous"></head>
    '''
        self.html_footer = '''</html>'''
        self.body = ''' '''

    def addRow(self, rowContent):
        self.body += rowContent
    
    def print(self):
        print('Hello')
        print(self.body)


    def concatinateHTML(self):
        self.body = self.html_header + self.body + self.html_footer
        return self.html_header + self.body + self.html_footer


class Row():
    def __init__(self,height):
        self.div_openTag = '''<div class="row" width="100%" height="{}" >'''.format(height)
        self.div_closedTag = ''' </div> '''
        self.content = ''' '''
        print('New Row : '+self.div_openTag,self.content,self.div_closedTag)

    def addColumn(self, columnContent):
        self.content += columnContent

    def concatinateHTML(self):
        return self.div_openTag + self.content + self.div_closedTag

class Column():
    def __init__(self,Width):
        self.div_openTag = '''<div class="col-{}" height="100%" >'''.format(convert100_to_col_12(Width))
        self.div_closedTag = '''</div>'''
        self.content = ''' '''
        self.width = Width 
        print('New Column :'+self.div_openTag,self.content,self.div_closedTag)
 
    def concatinateHTML(self):
        return self.div_openTag + self.content + self.div_closedTag

    def addImage(self,width,height,alignment):
        self.content += '''<div  >
        <img src="https://sekatandsipter.com/wp-content/uploads/2019/08/sekat-and-sipter-letter-webpix-1.jpg">         
        </div>'''
    
    def addTextInput(self,width,height,alignment):
        self.content += '''<div> 
        <input width="{}" height="{}" placeholder="Enter ..">
        </div>'''
    
    def addNavbar(self,width,height,alignment):
        self.content += '''<div> 
        <navbar> </navbar>        
        </div>'''

    def addText(self,width,height,alignment):
        self.content += '''<div> 
        <text> </text> 
        </div>'''


class Shape:
    def __init__(self, name, x, y, width, height, radius):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.radius = radius
        self.widthRatio = 0
        self.heightRatio = 0
        # Right-Left
        self.allignment = ""
    def __repr__(self):
        return self.name

class HtmlRow:
    def __init__(self):
        self.shapesPerRow = []
        self.column1Shapes = []
        self.column2Shapes = []
        self.column1Ratio = 0
        self.column2Ratio = 0
        self.height = 0
        self.maxWidthIndex = 0
    
    def print(self):
        print(self.column1Shapes,self.column2Shapes)
row1 = HtmlRow()
# row2 = HtmlRow()
# create a new shape called image
image = Shape("image",1,1,30,50,1)
# create a new shape called textInput
textInput = Shape("textInput",1,1,40,40,1)
# create a new shape called navbar
navBar = Shape("navbar",1,1,100,50,1)
# create a new shape called text
text = Shape("text",1,1,80,30,1)

#Appended the shape image to column 1 in row 1
row1.column1Shapes.append(image)
#Appended the shape image to column 1 in row 1
row1.column1Shapes.append(textInput)

#Appended the shape image to column 2 in row 1
row1.column2Shapes.append(navBar)
#Appended the shape image to column 2 in row 1
row1.column2Shapes.append(text)
row1.height = 50
row1.column1Ratio = 90
row1.column2Ratio = 10

listOfRows = []
listOfRows.append(row1)

#testing the list of rows after adding elements
for row in listOfRows:
    row.print()
    for shape in row.column1Shapes:
        print(shape.name)
    for shape in row.column2Shapes:
        print(shape.name)

HTML_Page = HTML_Generator()

for row in listOfRows:
    New_row = Row(row.height)
    New_col1 = Column(row.column1Ratio)
    New_col2 = Column(row.column2Ratio)
    for shape in row.column1Shapes:
        # print(New_col1.width)
        pass
    for shape in row.column2Shapes:
        pass
print(((40*12)%100))
# HTML_Page.concatinateHTML()
# HTML_Page.print()
