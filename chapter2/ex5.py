
class Ex5Parser:

    #should handling commands get really complex, start moving code more and more towards a bunch of strategies that the Parser delegates to.
    def __init__(self):
        self.commandHandler = {'p':self.selectPen, 
        'd':self.penDown, 
        'w':self.drawDirection, 
        'n':self.drawDirection,
        's':self.drawDirection,
        'e':self.drawDirection,
        'u':self.penUp,
        'q':self.exitCalled
        }
        
    def selectPen(self, command, argument):
        if (argument != None):
            print "selected pen " + str(argument)
        else:
            print "you must select a pen with a specific number"  
        
    def penDown(self, command, argument):
        print "pen down"

    
    def drawDirection(self, command, argument):
        if (argument != None):
          print "drawing " + str(command) + " " + str(argument)
        else:
          print "this command requires a numeric argument"

    def penUp(self, command, argument):
        print "pen up"
        
    def exitCalled(self, command, argument):
        print "G'day!"
        exit(0)

    #todo would be adding error handling / user input sanitizing that's better
    def parse(self,inputStr):
        formattedStr = self.formatStr(inputStr)
        command, argument = self.splitInput(formattedStr)
        self.handle(command, argument)
        
    def formatStr(self, inputStr):
        return inputStr.strip().lower()

    def splitInput(self, formattedStr):
        #in theory this could get more complicated, thus the method
        #but python's split is actually _very_ smart in how it deals with whitespace
        #'h    ey   '.split() returns ['h','ey'] with no '' fields 
        #a la Java if memory serves
        ar = formattedStr.split()
        if len(ar) == 1:
            ar += [None]
        return ar[0:2]
        
    def handle(self, command, argument):
      if self.commandHandler.has_key(command):
          self.commandHandler[command](command, argument)
      else:
          print "Invalid command"
        


if (__name__ == "__main__"):
    print "Enter your paint program input, hit q to exit"
    parser = Ex5Parser()
    while (True):
        inputStr = raw_input()
        parser.parse(inputStr)
        
