Made by Yale Zhang

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

    render() returns a list of all the different branch points withing the lightning
