#SingleInstance force
^+a::
x := 0.84 * A_screenWidth
y := 0.625 * A_screenHeight
Click %x%, %y%
return
^+b::
x := 0.90 * A_screenWidth
y := 0.625 * A_screenHeight
Click %x%, %y%
return
^+c::
x := 0.84 * A_screenWidth
y := 0.73 * A_screenHeight
Click %x%, %y%
return
^+d::
x := 0.90 * A_screenWidth
y := 0.73 * A_screenHeight
Click %x%, %y%
return
^+q::
x := 0.72 * A_screenWidth
y := 0.96s * A_screenHeight
Click %x%, %y%
return
^q::
x := 0.69 * A_screenWidth
y := 0.96 * A_screenHeight
Click %x%, %y%
return
^+h::
x := 0.92 * A_screenWidth
y := 0.35 * A_screenHeight
Click %x%, %y%
Send {Tab}
Send {Right}
return
^h::
x := 0.81 * A_screenWidth
y := 0.35 * A_screenHeight
Click %x%, %y%
Send {Tab}
Send {Right}
return
^Escape::
ExitApp
return