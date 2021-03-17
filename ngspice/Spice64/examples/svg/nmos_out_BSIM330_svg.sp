*****  NMOS Transistor BSIM3 (Id-Vds) with Rd ***

M1 2 1 3 4 n1 W=1u L=0.35u Pd=1.5u Ps=1.5u ad=1.5p as=1.5p
vgs 1 0 3.5 
vds 2 0 0.1 
vss 3 0 0
vbs 4 0 0

* drain series resistor
R2 2 22 1k
M2 22 1 32 4 n1 W=1u L=0.35u Pd=1.5u Ps=1.5u ad=1.5p as=1.5p
vss2 32 0 0


.options Temp=27.0

* BSIM3v3.3.0 model with modified default parameters 0.18�m
.model n1 nmos level=49 version=3.3.0 tox=3.5n nch=2.4e17 nsub=5e16 vth0=0.15
.model p1 pmos level=49 version=3.3.0 tox=3.5n nch=2.5e17 nsub=5e16 vth0=-0.15

.control
* sim
dc vds 0 2 0.05 vgs 0 2 0.4

* plot
set xgridwidth=2
set xbrushwidth=3

set nolegend

* the default settings
* "svgwidth", "svgheight",  "svgfont-size", "svgfont-width", "svguse-color", "svgstroke-width", "svggrid-width",
set svg_intopts = ( 1024, 768, 16, 0, 1, 2, 0 )
* "svgbackground", "svgfont-family", "svgfont"
set svg_stropts= ( )

*** svg ***
set hcopydevtype = svg
set color0=white
set color1=blue
set color2=green
hardcopy plot_4.svg vss#branch title 'Drain current versus drain voltage' xlabel 'Drain voltage' ylabel 'Drain current'

set svg_intopts = ( 512, 384, 16, 0, 1, 2, 0 )

set color0=blue
set color1=white
set color2=red
hardcopy plot_5.svg vss#branch title 'Drain current versus drain voltage' xlabel 'Drain voltage' ylabel 'Drain current'

set svg_intopts = ( 512, 384, 16, 0, 0, 2, 2 )

set color0=black
set color1=yellow
set color2=white
hardcopy plot_6.svg vss#branch title 'Drain current versus drain voltage' xlabel 'Drain voltage' ylabel 'Drain current'

* for MS Windows only
if $oscompiled = 1 | $oscompiled = 8
  shell Start plot_4.svg
  shell Start plot_5.svg
  shell Start plot_6.svg
else
* for CYGWIN
  shell xterm -e gs  plot_4.svg &
  shell xterm -e gs  plot_5.svg &
  shell xterm -e gs  plot_6.svg &  
end
.endc

.end




