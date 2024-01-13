from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def odes_trifle (x,t, kt, kr, kdeg):

    """Solves and plots ODEs for the irreversible reaction C -> CT-> C + T """


    # assign each ODE to an element of the vector x

    C = x[0]      # Idle cooks
    CT = x[1]     # Cooks making trifle
    T = x[2]     # Trifles on table

    # define each ODE

    dCdt = kr*CT - kt*C
    dCTdt = kt*C - kr*CT
    dTdt = kr*CT - kdeg*T

    return [dCdt, dCTdt, dTdt]

def odes_trifle_scan_kt (x,t,kt_list):

    """ Runs a parameter scan for kt: rate of trifle initiation"""

    kt_C = []  # will collect the last value of C from each time course
    kt_T = []  # will collect the last value of T from each time course
    kt_data = []


    for kt in kt_list:

        rates = (kt, 0.1, 0.05)  # (0.2, 0.1, 0.05)
        data = odeint(odes_trifle,x,t,(rates))# data is a "table" with three columns and t rows.

        #Extract various things from the "data" table.

        endC = data[-1,0]  # This collects the last row (index -1) of the first column
        kt_C.append (endC)  # puts it in the list kr_C

        endT = data[-1,2]  # This collects the last row (index -1) of the third column
        kt_T.append (endT)  # puts it in the list kr_T
        kt_data.append (data)


    return kt_C, kt_T, kt_data  # each of kt1-4 is a "table" with three columns and t rows.

def odes_trifle_scan_kr (x,t, kr_list, kt):

    """ Runs a parameter scan for kr: rate of trifle release"""

    kr_C = []  # will collect the last value of C from each time course
    kr_T = []  # will collect the last value of T from each time course
    kr_data = []


    for kr in kr_list:

        rates = (kt, kr, 0.05)  # (0.2, 0.1, 0.05)
        data = odeint(odes_trifle,x,t,(rates))# data is a "table" with three columns and t rows.

        #Extract various things from the "data" table.

        endC = data[-1,0]  # This collects the last row (index -1) of the first column
        kr_C.append (endC)  # puts it in the list kr_C

        endT = data[-1,2]  # This collects the last row (index -1) of the third column
        kr_T.append (endT)  # puts it in the list kr_T

        kr_data.append (data)


    return kr_C, kr_T, kr_data


def odes_trifle_scan_kt_kr (x,t, kr_list, kt_list):

    """ Runs a double parameter scan for kt and kr"""

    kt_kr_C = []  # will collect array of C
    kt_kr_T = []  # will collect arrat of T


    for kt in kt_list:

        kr_C, kr_T, kr_data = odes_trifle_scan_kr (x,t,kr_list,kt)
        kt_kr_C.append(kr_C)
        kt_kr_T.append(kr_T)

    return kt_kr_C, kt_kr_T

#------------------------------------------------------------
# Plotting functions

def timecourse_plot(C,CT,T):

    """ Plots timecourse data """

    plt.figure()
    plt.plot(t,C,'k',label = 'C, Idle cooks')
    plt.plot(t,CT,'r',label = 'CT, Cooks making trifle')
    plt.plot(t,T,'b',label = 'T, Trifles on table')
    plt.xlabel('Time (Min)')
    plt.ylabel('Number of cooks or trifles')
    plt.legend()
    plt.title('Time course for trifle production')

def scan_plot (kt_data, kr_data, kt_list, kr_list):

    """ Extracts timecourse data from parameter scans \
        and plots for 4 values of kt and kr"""

    kt1 = kt_data [1]
    kt2 = kt_data [3]
    kt3 = kt_data [5]
    kt4 = kt_data [7]

    kr1 = kr_data [1]
    kr2 = kr_data [3]
    kr3 = kr_data [5]
    kr4 = kr_data [7]

    plt.figure()
    plt.subplot (2,2,1)
    plt.plot(t,kt1[:,0],'k',label = 'C, Idle cooks')
    plt.plot(t,kt1[:,1],'r',label = 'CT, Cooks making trifle')
    plt.plot(t,kt1[:,2],'b',label = 'T, Trifles on table')
    #plt.xlabel('Time (Min)')
    plt.ylabel('Number of cooks or trifles')
    plt.ylim (0,100)
    plt.legend()
    plt.title('kt = {}'.format(kt_list[1])) # this is very useful for labelling plots according to a list of values.

    plt.subplot (2,2,2)
    plt.plot(t,kt2[:,0],'k')
    plt.plot(t,kt2[:,1],'r')
    plt.plot(t,kt2[:,2],'b')
    #plt.xlabel('Time (Min)')
    #plt.ylabel('Number of cooks or trifles')
    plt.ylim (0,100)
    plt.title('kt = {}'.format(kt_list[3]))

    plt.subplot (2,2,3)
    plt.plot(t,kt3[:,0],'k')
    plt.plot(t,kt3[:,1],'r')
    plt.plot(t,kt3[:,2],'b')
    plt.xlabel('Time (Min)')
    plt.ylabel('Number of cooks or trifles')
    plt.ylim (0,100)
    plt.title('kt = {}'.format(kt_list[5]))

    plt.subplot (2,2,4)
    plt.plot(t,kt4[:,0],'k')
    plt.plot(t,kt4[:,1],'r')
    plt.plot(t,kt4[:,2],'b')
    plt.xlabel('Time (Min)')
    #plt.ylabel('Number of cooks or trifles')
    plt.ylim (0,100)
    plt.title('kt = {}'.format(kt_list[7]))

    plt.figure()

    plt.subplot (2,2,1)
    plt.plot(t,kr1[:,0],'k',label = 'C, Idle cooks')
    plt.plot(t,kr1[:,1],'r',label = 'CT, Cooks making trifle')
    plt.plot(t,kr1[:,2],'b',label = 'T, Trifles on table')
    #plt.xlabel('Time (Min)')
    plt.ylabel('Number of cooks or trifles')
    plt.ylim (0,200)
    plt.legend()
    plt.title('kr = {}'.format(kr_list[1])) # this is very useful for labelling plots according to a list of values.

    plt.subplot (2,2,2)
    plt.plot(t,kr2[:,0],'k')
    plt.plot(t,kr2[:,1],'r')
    plt.plot(t,kr2[:,2],'b')
    #plt.xlabel('Time (Min)')
    #plt.ylabel('Number of cooks or trifles')
    plt.ylim (0,200)
    plt.title('kr = {}'.format(kr_list[3]))

    plt.subplot (2,2,3)
    plt.plot(t,kr3[:,0],'k')
    plt.plot(t,kr3[:,1],'r')
    plt.plot(t,kr3[:,2],'b')
    plt.xlabel('Time (Min)')
    plt.ylabel('Number of cooks or trifles')
    plt.ylim (0,200)
    plt.title('kr = {}'.format(kr_list[5]))

    plt.subplot (2,2,4)
    plt.plot(t,kr4[:,0],'k')
    plt.plot(t,kr4[:,1],'r')
    plt.plot(t,kr4[:,2],'b')
    plt.xlabel('Time (Min)')
    #plt.ylabel('Number of cooks or trifles')
    plt.ylim (0,200)
    plt.title('kr = {}'.format(kr_list[7]))


def bigscan_plot (kt_C, kt_T, kr_C, kr_T, kt_list, kr_list):

    """plots end values of C and T against parameter scan for kt and kr"""

    plt.figure()

    plt.subplot (2,2,1)
    plt.plot(kt_list,kt_C,'k')
    plt.xlabel('kt rate of initiation')
    plt.ylabel('Number of idle cooks ')
    plt.ylim (0,50)
    plt.title('Number of idle cooks vs. kt')

    plt.subplot (2,2,2)
    plt.plot(kt_list,kt_T,'k')
    plt.xlabel('kt rate of initiation')
    plt.ylabel('Number of trifles on table ')
    plt.ylim (0,200)
    plt.title('Trifles on table vs. kt')

    plt.subplot (2,2,3)
    plt.plot(kr_list,kr_C,'k')
    plt.xlabel('kr rate of release')
    plt.ylabel('Number of idle cooks')
    plt.ylim (0,50)
    plt.title('Number of idle cooks vs. kr')

    plt.subplot (2,2,4)
    plt.plot(kr_list,kr_T,'k')
    plt.xlabel('kr rate of release')
    plt.ylabel('Number of trifles on table ')
    plt.ylim (0,200)
    plt.title('Trifles on table vs. kr')

def heatmap_plot (kt_kr_C, kt_kr_T, kt_list, kr_list):
    """plots a heat map for double parameter scan of kt and kr\
       showing end values of C and T"""

    plt.figure()
    plt.subplot (1,2,1)
    plt.imshow(kt_kr_C, cmap = 'viridis', interpolation = 'none')# alternative cmap: bone, viridis, inferno, hot, rainbow
    plt.clim(0,50)
    plt.colorbar()
    plt.title('Idle cooks',fontsize = 12)

    step_x = 1 # step between consecutive labels
    x_positions = np.arange(0,len (kr_list),step_x) # pixel count at label position
    x_labels = kr_list # labels you want to see
    plt.xticks(x_positions, x_labels)

    step_y = 1 # step between consecutive labels
    y_positions = np.arange(0,len (kt_list),step_y) # pixel count at label position
    y_labels = kt_list # labels you want to see
    plt.yticks(y_positions, y_labels)

    plt.xlabel('kr: Trifle release',fontsize = 12) # the inner loop
    plt.ylabel('kt: Trifle initiation',fontsize = 12) # the outer loop

    plt.subplot (1,2,2)
    plt.imshow(kt_kr_T, cmap = 'viridis', interpolation = 'none')# alternative cmap: bone, viridis, inferno, hot, rainbow
    plt.clim(0,200)
    plt.colorbar()
    plt.title('Trifles on table',fontsize = 12)

    step_x = 1 # step between consecutive labels
    x_positions = np.arange(0,len (kr_list),step_x) # pixel count at label position
    x_labels = kr_list # labels you want to see
    plt.xticks(x_positions, x_labels)

    step_y = 1 # step between consecutive labels
    y_positions = np.arange(0,len (kt_list),step_y) # pixel count at label position
    y_labels = kt_list # labels you want to see
    plt.yticks(y_positions, y_labels)

    plt.xlabel('kr: Trifle release',fontsize = 12) # the inner loop
    plt.ylabel('kt: Trifle initiation',fontsize = 12) # the outer loop


# Main program.
#----------------------------------------------------------------------------------
# 1) Set initial conditions [C, CT, T], here units are single people or trifles

x = [50,0,0]

# 2) Declare a time vector (range 0-60 mins, 100 steps).

t = np.linspace (0,120,200)

# 3) Declare the rates

kt = 0.2 # trifle intitiation: 0.2 per minute
kr = 0.1 # trifle release: 0.1 per minute
kdeg = 0.05 # trifle consumption: 0.05 per minute

rates = (kt, kr, kdeg)

kt_list = [0.005, 0.01, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8]

kr_list = [0.005, 0.01, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8]

# 4) Set conditions for what to run.

timecourse = 'yes'  # 'yes' or 'no'
scan = 'yes'        # 'yes' or 'no'
bigscan = 'yes'     # 'yes' or 'no'
doublescan = 'no'   # 'yes' or 'no'

# 3) If you want to see the timecourse, run odes_trifle and plot the results

if timecourse == 'yes':

    data = odeint(odes_trifle, x,t,(rates))

    C = data[:,0]
    CT = data[:,1]
    T = data[:,2]

    timecourse_plot (C, CT, T)

# 5) Fi you want to scan kt and kr, Call the scan functions for kt and kr, plot results.

if scan or bigscan == 'yes':

    kt_C, kt_T, kt_data  = odes_trifle_scan_kt (x,t, kt_list)
    kr_C, kr_T, kr_data  = odes_trifle_scan_kr (x,t, kr_list,kt)

    #Extract data (here for every second parameter value).
if scan  == 'yes':

    scan_plot (kt_data, kr_data, kt_list, kr_list)

if bigscan == 'yes':

    bigscan_plot (kt_C, kt_T, kr_C, kr_T, kt_list, kr_list)

if doublescan == 'yes':

    kt_kr_C, kt_kr_T = odes_trifle_scan_kt_kr (x,t, kr_list, kt_list)

    heatmap_plot (kt_kr_C, kt_kr_T, kt_list, kr_list)

plt.show()


