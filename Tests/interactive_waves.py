import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Initial parameters
initial_wavelength = 2 * np.pi
initial_amplitude = 1
initial_phase = 0

# Create the figure and the line that we will manipulate
fig, axes = plt.subplots(2, 1, figsize=(8, 6))
plt.subplots_adjust(bottom=0.25)
ax_wave1, ax_wave2 = axes
t = np.linspace(0, 10, 1000)
wave1_line, = ax_wave1.plot(t, np.zeros_like(t), lw=2)
wave2_line, = ax_wave1.plot(t, np.zeros_like(t), lw=2, color='red')
interference_line, = ax_wave2.plot(t, np.zeros_like(t), lw=2, color='green')

# adjust the main plot to make room for the sliders
plt.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the wavelength.
axcolor = 'lightgoldenrodyellow'
ax_wavelength = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
wavelength_slider = Slider(ax=ax_wavelength, label='Wavelength', valmin=0.1, valmax=10.0, valinit=initial_wavelength)

# Make a vertical slider to control the amplitude.
ax_amplitude = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
amplitude_slider = Slider(ax=ax_amplitude, label='Amplitude', valmin=0.1, valmax=2.0, valinit=initial_amplitude, orientation="horizontal")

# Make another slider to control the phase.
ax_phase = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
phase_slider = Slider(ax=ax_phase, label='Phase', valmin=0, valmax=2 * np.pi, valinit=initial_phase, orientation="horizontal")

# The function to be called anytime a slider's value changes
def update(val):
    wavelength = wavelength_slider.val
    amplitude = amplitude_slider.val
    phase = phase_slider.val
    wave1 = amplitude * np.sin(2 * np.pi / wavelength * t)
    wave2 = amplitude * np.sin(2 * np.pi / wavelength * t + phase)
    interference = wave1 + wave2
    wave1_line.set_ydata(wave1)
    wave2_line.set_ydata(wave2)
    interference_line.set_ydata(interference)
    fig.canvas.draw_idle()

# register the update function with each slider
wavelength_slider.on_changed(update)
amplitude_slider.on_changed(update)
phase_slider.on_changed(update)

# Set the layout of the plots and sliders
ax_wave1.margins(x=0)
ax_wave2.margins(x=0)
ax_wave1.set_title('Waves')
ax_wave2.set_title('Interference')

# Set the range of y-axis for the interference plot to be more visible
ax_wave1.set_ylim(-4, 4)
ax_wave2.set_ylim(-4, 4)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial parameters.
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    wavelength_slider.reset()
    amplitude_slider.reset()
    phase_slider.reset()
button.on_clicked(reset)

plt.show()

#%%

#%%
