from collections import OrderedDict
from turtle import *
global current_line

def start_up(locW,locH):
    #positions turtle at the top left of the screen
    #the /16 is needed in the positioning, because 0,0 centre co-ord means w + h
    # both need to be halfed to use correct fractions
    # locW, locH = 'local width/height' used in func
    pu()
    setup(width = locW, height = locH)
    setx(-(locW*(7/16))) #  sets turtle to the top left of screen
    sety(locH*(5/16))
    seth(90) #  points the turtle north
    pd()


class stencil:
    instr = "PDSH000FW100SH100FW100PU"  # draws a straight line
    reset = "PDSH000FW100SH100FW100PU"
    starter = "PDSH000FW100SH100FW100PU"
    name = 'XX'
    #placeholders

    def count_self(self):
        # counts number of unique instructions (non-start/end) and returns them as a single string
        self.cntPU, self.cntPD = stencil.instr.count('PU'), stencil.instr.count("PD")

        self.Uinstr = self.instr[2:(len(self.instr) - 2)]
        if len(self.Uinstr) % 5 == 0:
            self.noUinstr = int(len(self.Uinstr) / 5)
        else:
            raise Exception("The instructions for {} were not entered as 5 chars".format(self.name))


    def get_startend_instr(self):
        # this function gets the start and end functions from the instructions
        self.start_instr = self.instr[0:2]
        self.end_instr = self.instr[len(self.instr) - 2:len(self.instr)]

def set_size(in_size):
    #used in conjunction with MyCircle()
    global size
    size = int(in_size)


def MyCircle(circle_input):
    #to use this function: digit[0] is direction and digit[1,2] are is degree /10
    global size
    #this is to correctly convert the int value of 18 to string of '018' so it can be handeled correctly
    if circle_input - 100 < 0:
        temp = '0'
    else:
        temp = ''

    circle_input = str(circle_input)
    circle_input = temp + circle_input

    loc_size = size / 4

    #selects direction based on instruction
    if circle_input[0] == '1':
        direct = 1
    elif circle_input[0] == '0':
        direct = -1

    angle_deg = 10*int(circle_input[1:3])

    circle(loc_size, (direct * angle_deg))

class stencil_data:
    #this class contains the dictionaries which hold all the character instructions, currently if a character is added
    #into 'symbols' it must be added in 'starter' and 'reset' even if they are blank
    symbols = OrderedDict({
        "A": "PDSH068FW108SH292FW054SH000BW040FW040SH292FW054PU",
        "B": "PDSS100SH090FW100SH180CR018SH180CR018PU",
        "C": "PDSS100SH090CR118FW050CR118PU",
        "D": "PDSH090FW100SH180SS200CR018SS100PU",
        "E": "PDSH090FW100SH000FW030SH180FW030SH270FW050SH000FW030SH180FW030SH270FW050SH000FW030PU",
        "F": "PDSH090FW100SH000FW030SH180FW030SH270FW050SH000FW030SH180FW030SH270FW050PU",
        "G": "PDSH090SS080CR118FW060CR118FW010SH180FW030SH000FW040PU",
        "H": "PDSH090FW100SH270FW050SH000FW040SH090FW050SH270FW100PU",
        "I": "PDSH000FW025SH090FW100SH180FW025SH000FW050SH180FW025SH270FW100SH000FW025PU",
        "J": "PDBW050FW025SH270FW080SH090SS080CR018SH090FW010PU",
        "K": "PDSH090FW100BW050SH059FW058BW058SH301FW058PU",
        "L": "PDSH090FW100SH270FW100SH000FW035PU",
        "M": "PUSH073FW104SH287FW070SH073FW070SH287FW104PU",
        "N": "PDSH090FW100SH299FW114SH090FW100PU",
        "O": "PDSS140SH270CR118FW030CR118FW030PU",
        "Q": "PDSS100SH270CR118SH135FW030BW060FW030SH090FW050CR118FW050PU",
        "R": "PDSH090FW100SH180SS080CR018SH288FW065PU",
        "S": "PDSH180SS100FW025CR118SH180CR018SH180FW025PU",
        "T": "PDSH090FW100SH180FW025SH000FW050SH180FW025SH270FW100PU",
        "U": "PDSH270FW070SS120CR118FW070PU",
        "V": "PDSH287FW104SH073FW104PU",
        "W": "PDSH287FW104SH073FW070SH287FW070SH073FW104PU",
        "X": "PDSH063FW112BW056SH117FW056BW112PU",
        "Y": "PDSH063FW112BW056SH117FW056PU",
        "Z": "PDSH000FW040SH248FW108SH000FW040PU",
        "P": "PDSS100SH090FW100SH180CR018SH270FW050PU",
        " ": "PDPU"
    })

    starter = OrderedDict({
        "A": "",
        "B": "",
        "C": "SH000FW050SH090FW075",
        "D": "",
        "E": "",
        "F": "",
        "G": "SH000FW015SH090FW080SH000FW50",
        "H": "",
        "I": "",
        "J": "SH000FW050SH090FW100SH000",
        "K": "",
        "L": "",
        "M": "",
        "N": "",
        "O": "SH090FW035",
        "Q": "SH090FW025",
        "R": "",
        "S": "FW050SH090FW100",
        "T": "SH000FW45",
        "U": "SH090FW100",
        "V": "SH090FW100",
        "W": "SH090FW100",
        "X": "",
        "Y": "",
        "Z": "SH090FW100",
        "P": "",
        " ": "SH000FW060"

    })

    reset = OrderedDict({
        "A": "",
        "B": "FW025",
        "C": "SH270FW025",
        "D": "SH000FW050",
        "E": "",
        "F": "SH000FW030",
        "G": "SH270FW035SH000BW10",
        "H": "SH000FW015",
        "I": "",
        "J": "SH270FW030SH000FW070",
        "K": "",
        "L": "",
        "M": "",
        "N": "SH270FW100",
        "O": "SH000FW070SH270FW035",
        "Q": "SH000FW050SH270FW025",
        "R": "",
        "S": "SH000FW050",
        "T": "SH000FW015",
        "U": "SH270FW100",
        "V": "SH270FW100",
        "W": "SH270FW100",
        "X": "",
        "Y": "SH117BW112SH000BW015",
        "Z": "",
        "P": "SH000FW025",
        " ": ""

    })


directions = OrderedDict({  # this dictionary works as a case statement based on current instruction
    "FW": fd,
    "BW": bk,
    "CR": MyCircle,
    "SH": seth,
    "SS": set_size

})

pen_instructions = OrderedDict({
    "PD": pd,
    "PU": pu
})


def move_turtle(instr_type,instr_val):
    # this function takes the instruction and calls the relevant function inside the 'directions' dictionary
    for i,j in directions.items():
        if instr_type == i:
            directions[i](instr_val)
            break

def carry_instr(stencil):
    pu()
    seth(0)
    for i in range(int(len(stencil.starter)/5)):
        move_turtle(stencil.starter[(i * 5):(i * 5 + 2)], int(stencil.starter[(i * 5 + 2):(i * 5 + 5)]))
        #looks funky but essentially moves the function along the string in sets of five and moves the first 2 chars and
        #last 3 chars into separate parts of the move_turtle() function :)
    pd()
    for i, j in pen_instructions.items():
        if stencil.start_instr == i:
            pen_instructions[i]

            break

    for i in range(stencil.noUinstr):
        move_turtle(stencil.Uinstr[(i*5):(i*5 + 2)], int(stencil.Uinstr[(i*5 + 2):(i*5 + 5)]))

    pu() #even though i have 'instructions' to do this, occasionally they don't stick, so this is here!
    seth(0)#myers
    for i in range(int(len(stencil.reset)/5)):
        move_turtle(stencil.reset[(i * 5):(i * 5 + 2)], int(stencil.reset[(i * 5 + 2):(i * 5 + 5)]))



def assign_stencil(lett):
    #goes through the assignment of a new character to the current_stencil
    current_stencil.name = lett
    current_stencil.starter = stencil_data.starter[lett]
    current_stencil.instr = stencil_data.symbols[lett]
    current_stencil.reset = stencil_data.reset[lett]
    current_stencil.count_self()
    current_stencil.get_startend_instr()

def get_curr_pos(locW,locH):
    global current_line
    curr_x , curr_y = pos()
    if curr_x + 100 > locW /2:
        current_line = current_line + 1
        setx(-(locW * (7 / 16)))  # sets turtle to the top left of screen
        sety((locH * (5 / 16)-150*current_line))


start_up(1200,800) # x and y dimensions of screen
current_line = 0 #current line of drawing
size = 100 #see MyCircle()
speed(0) #got to go at great velocities



current_stencil = stencil()
user_input = textinput('Input','Enter text to print')

for i in range(len(user_input)):
    assign_stencil(user_input[i])
    carry_instr(current_stencil)
    pu()
    seth(0)
    fd(35)
    get_curr_pos(1200, 800)
    pd()

ht()
done()

