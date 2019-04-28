#proc page
	backgroundcolor: transparent
#endproc

// specify data using proc getdata
#proc getdata
	file: weatherData.txt
	fieldnames: dt temp dew bar rain wind vis cond
	delim: tab
	showresults: no
#endproc

// set up the plotting area	
#proc areadef
	rectangle: 1 0.7 4 2
	xscaletype: datetime mm/dd/yy.hh:mm
	xautorange: datafield=dt
	yscaletype: linear
	yautorange: datafield=temp,dew nearest=1
#endproc
	

// run it again to do the grid at every hour
#proc xaxis
	stubs: inc 4 hours
	stubformat: hhA
	grid: color=coral
	stubdetails: size=6
#endproc   

// first time- do month stubs every day
#proc xaxis
	stubs: inc 1 day
	stubformat: MMMdd
	location: 0.6
	axisline: no
	tics: none
	stubdetails: size=6
#endproc   

#proc yaxis
	stubs: inc 4
	grid: style=1 color=coral
	stubdetails: size=6
#endproc
	
// plot the data
#proc bars
	locfield: dt
	lenfield: temp
	barwidth: 0.01
	color:	red
	outline: no
	cluster: 1/2
	clustersep: 0.02
#endproc

// plot the data
#proc bars
	locfield: dt
	lenfield: dew
	barwidth: 0.01
	color:	blue
	outline: no
	cluster: 2/2
	clustersep: 0.02
#endproc