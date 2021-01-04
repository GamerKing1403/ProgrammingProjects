package lesson1

fun main(args: Array<String>){
	println("Hello World")
	
	var b: Int
	b = 5
	
	val c: Int
	c = 6
	
	// Error -> c = 7
	
	var a = 0
	if(a == 1){
		println(a)
	}else if(a != 1){
		println("a " + a)
	}
	
	for(i in 10..5 step 2){
		print("" + i + "")
	}
	
	/*Same as Above ->
 
 	for(i in 10 downTo 5 step 2) {
		print("" + i + " ")
	}
 
	 */
	
	println()
	
	var j = 0
	
	while(j<=5){
		print(""+j+" ")
		j++
	}
	
	
}

