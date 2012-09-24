
class Ex5Parser:

    def __init__(self):
        self.commandHandler = {'p':self.selectPen, 
        'd':self.penDown, 
        'w':self.drawDirection, 
        'n':self.drawDirection,
        's':self.drawDirection,
        'e':self.drawDirection,
        'u':self.penUp
        'q':self.exitCalled
        }
        
    def selectPen(self, command, argument):
        print "selected pen " + str(argument)
        
    def penDown(self, command, argument):
        print "pen down"
        
    def drawDirection(self, command, argument):
        print "drawing " + str(command) + " " + str(argument)
    def penUp(self, command, argument):
        print "pen up"
        
    def exitCalled(self, command, argument):
        exit(0)
    
    def parse(self,inputStr):
        formattedStr = self.formatStr(inputStr)
        command, argument = self.splitInput(formattedStr)
        self.handle(command, argument)
        
    def formatStr(self, inputStr):
        return inputStr.strip().lower()

    def splitInput(self, formattedStr):
        #in theory this could get more complicated, thus the method
        #but python's split is actually _very_ smart in how it deals with whitespace
        #'h    ey   '.split() returns ['h','ey'] with no bullshit '' fields 
        #a la Java if memory serves
        ar = formattedStr.split()
        if len(ar) == 1:
            ar += [None]
        return ar
        
    def handle(self, command, argument):
        


if __name__ == "__main__":
    print "Enter your paint program input, hit q to exit"
    parser = new Ex5Parser()
    while (true):
        inputStr = raw_input()
        parser.parse(inputStr)
        
