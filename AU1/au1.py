 #grupp 9 
 #import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import time

docked = 0  # Flag for controlling if the satellites
            # have docked (docked = 1) or not (docked = 0)
t_lim = 40  # The duration in seconds the simulation lasts.
            # Should be around 40 s at hand in, but can be changed during
            # the development of the function.
def update_sat(x1,x2,v1,v2,F,dt):
    global docked
    
    # Remove the dummy codes below (lines 70-73) and replace with
    # the correct function.
    xnew1 = x1 + (v1*dt) 
    vnew1 = v1 + ((F/m1)*dt)
    xnew2 = x2 + (v2*dt)
    vnew2 = v2

    if abs(xnew2 - xnew1) < 5:
     if abs(vnew2 - vnew1) < 2:
        docked = 1
   
    # Completely inelastic collision
        total_mass = m1 + m2
        v_combined = (m1 * vnew1 + m2 * vnew2) / total_mass

        vnew1 = v_combined
        vnew2 = v_combined

        print("space 1 place: ", vnew1)
        print("space 2 place: ", vnew2)

     else:
        docked = 2
        # Elastic collision 

        print("Rocket speed before collision: ", vnew1)
        print("Satellite speed before collision: ", vnew2)

        collisionm = (m1 - m2) * vnew1
        bothm = m1 + m2
        raketV = vnew1

        vnew2 = (2 * m1 * raketV) / bothm
        vnew1 = collisionm / bothm

        print("Rocket speed after collision: ", vnew1)
        print("Satellite speed after collision", vnew2)
       
    return xnew1,xnew2,vnew1,vnew2

# Initialisation of some parameters (don't change)
F = 300

m1 = 500
x1 = -100
v1 = 0

m2 = 1000
x2 = 0
v2 = 0

fig, ax = plt.subplots()
# Adjust figure to make room for buttons
fig.subplots_adjust(bottom=0.25)

# Create button which decrease force with 50 N.
decrax = fig.add_axes([0.2, 0.05, 0.2, 0.08])
decr_button = Button(decrax, 'Decrease Thrust', hovercolor='0.975')

def decr(event):
    global F
    F = F - 50.0
    
decr_button.on_clicked(decr)

# Create button which increase force with 50 N.
incrax = fig.add_axes([0.65, 0.05, 0.2, 0.08])
incr_button = Button(incrax, 'Increase Thrust', hovercolor='0.975')

def incr(event):
    global F
    F = F + 50.0
    
incr_button.on_clicked(incr)

tstart = time.time()
telapsed = 0
told = tstart
# Main loop startshere
while telapsed <= t_lim:
    # Deduce time and time step
    tnew = time.time()
    dt = tnew - told
    told = tnew
    
    # Call to function update_sat
    x1,x2,v1,v2 = update_sat(x1,x2,v1,v2,F,dt)
    
    telapsed = time.time() - tstart
    
    # Update plot
    ax.plot(x1,0,'wo')
    ax.plot(x2,0,'ro',markersize=10)
    ax.set_xlabel('x (m)',fontsize=12)
    ax.set_xlim([-150,50])
    ax.set_facecolor("black")
    ax.tick_params(labelsize=12, left = False, labelleft = False)
    
    # Update text
    textstr = '\n'.join((
    'Time: %6.2f s' % (telapsed,),
    'Distance: %6.2f m' % (abs(x2-x1), ),
    'Relative  velocity: %6.2f m/s' % (abs(v2-v1), )))
    props = dict(boxstyle='round', facecolor='wheat', alpha=1.0)
    ax.text(0.25, 0.9, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)
    textstr2 = ('Force: %4.1f N' % (F))
    ax.text(0.4, -0.225, textstr2, transform=ax.transAxes, fontsize=12,
        verticalalignment='top')
    
    # If succesful docking
    textstring = "Docking succesful!!"
    if docked == 1:
        ax.text(0.5, 0.2, textstring, transform=ax.transAxes, color="white", fontsize=12,
        verticalalignment='top')
        
    textstring2 = "Crashed!!!"
    if docked == 2:
        ax.text(0.5, 0.2, textstring2, transform=ax.transAxes, color="white", fontsize=12,
        verticalalignment='top')
    plt.pause(0.1)
    
    # Don't clear the last plot
    if telapsed < t_lim:
        ax.cla()
    

    
    