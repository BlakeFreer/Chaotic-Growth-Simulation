# Created by Blake Freer, February 4, 2019

# Inspired by Veritasium's video: "This equation will change how you see the world"
# https://www.youtube.com/watch?v=ovJcsL7vyrk
# The simulation shows how a "population" changes according to the logistic mapfunction
# x_{n+1} = r*x_n(1 - x_n)
# Where x_{n+1} is the next generation population (as a percent of the capacity)
# r is the growth rate
# x_n is the current generation population

# Instructions:
# Drag UP and DOWN in the yellow region to adjust the initial population (0% to 100%)
# Drag LEFT and RIGHT in the red region to adjust the growth rate (from 0 to 4)

# CHANGE THE FIRST FOUR VARIABLES
numNodes = 50    # Number of nodes / generations
nodeSize = 5     # Size of node circle
sizeWidth = 800  # Screen Width
sizeHeight = 600 # Screen Height


# DO NOT CHANGE
rate = 2.66
nodes = [0.5] * numNodes

def clamp(num, minimum, maximum):
    if num < minimum:
        return minimum
    elif num > maximum:
        return maximum
    else:
        return num

nodes[0] = 0.1

def nextGen(cur):
    global rate
    return rate * cur * (1-cur)

def calcNodes(nds):
    out = [nds[0]]
    for i in range(0,len(nds)-1):
        out.append(nextGen(nds[i]))
    return out

def xPos(index):
    global numNodes
    return index * (width-50)/(numNodes-1)

def drawNodes():
    global nodes, nodeSize
    for index in range(len(nodes)):
        if index > 0:
            strokeWeight(1)
            stroke(105,255,255)
            line(xPos(index), sizeHeight/2-nodes[index]*sizeHeight/2, xPos(index-1), sizeHeight/2-nodes[index-1]*sizeHeight/2)
        
        noStroke()
        fill(105,255,255)
        ellipse(xPos(index), sizeHeight/2-nodes[index]*sizeHeight/2, nodeSize, nodeSize)

def setup():
    global sizeHeight
    size(sizeWidth,sizeHeight)
    
def draw():
    global nodes, rate
    background(10)
    
    translate(25, height/4)
    
    # Draw axis labels before scaling
    textSize(20)
    fill(105,255,255)
    fill(255,255,100)
    text("Initial Population: "+str(round(nodes[0]*100,2))+"% of capacity",0, -100)
    
    fill(255, 100, 100)
    text("Rate Factor: "+str(round(rate,2)),0, -70)
    
    # Invert y axis
    scale(1,-1)
    # Draw 0 and 1 lines
    stroke(105,255,255)
    scale(1,-1)
    line(-25, 0, width, 0)
    line(-25, sizeHeight/2, width, sizeHeight/2)
    
    # Draw panels for adjusting variables
    # Initial Population
    fill(255,255,100,100)
    noStroke()
    rect(-25, 0, 75, height/2)
    # Rate Factor
    fill(255, 100, 100, 100)
    rect(-25, height/1.8, width, height/4)
    
    
    # Take mouseInput
    if mousePressed and mouseX < 100 and mouseY == clamp(mouseY, height/4, height*3/4):
        nodes[0]= clamp(float(mouseY-3*sizeHeight/4)/(-sizeHeight/2), 0, 1)
    if mousePressed and mouseY > height-height/5.4:
        rate = clamp(float(mouseX)/width*4,0,4)
    
    nodes = calcNodes(nodes)
    drawNodes()
