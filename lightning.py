import random
import pygame
pygame.init()

class lightning:

    def __init__(self,origin,xchange,ychange,deviation,length,streaks,surface,color,width):
        self.origin = origin
        self.xchange = xchange
        self.ychange = ychange
        self.deviation = deviation
        self.length = length
        self.streaks = streaks
        self.surface = surface
        self.color = color
        self.width = width
        
def render(lightning):
    branchpoints = [lightning.origin,]
    newxchange = lightning.xchange
    newychange = lightning.xchange
    
    for i in range(lightning.streaks):
        for j in range(lightning.length):
            point = branchpoints[j]
            
            newxchange = lightning.xchange + random.randint(-lightning.deviation,lightning.deviation)
            newychange = lightning.ychange + random.randint(-lightning.deviation,lightning.deviation)

            newbranchpoint = (point[0]+newxchange,point[1]+newychange)
            pygame.draw.line(lightning.surface,lightning.color,point,newbranchpoint,lightning.width)
            branchpoints.append(newbranchpoint)

    return branchpoints

instructions =  '''
This is a module that draws lightning in pygame.
Create a new lightning object with lightning(origin,xchange,ychange,deviation,length,streaks,surface,color)
    origin: a tuple containing coordinated for the base of the lightning
    xchange: how much the lightning changes on the x axis
    ychange: how much the lightning changes on the y axis
    deviation: how much the lightning deviates from a straight line
    length: how many times to apple xchange and ychange
    streaks: how many streaks of lightning
    surface: what surface to draw the lightning on
    color: an RGB tuple containing the color of the lightning
    width: how wide the lightning should be in pixels
Draw the lightning with render(lightning)
    render() returns a list of all the different branch points withing the lightning'''

print(instructions)
