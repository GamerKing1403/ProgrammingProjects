var result = false;

function newPage(){
	document.location.href = 'html/homePage.html';
}

function insert(num){
	if(!result){
		document.form.textview.value += num;
	}else{
		document.form.textview.value = "";
		result = false;
		document.form.textview.value += num;
	}
}

function equal(){
	var exp = document.form.textview.value;
	if(exp){
		document.form.textview.value = eval(document.form.textview.value);
		if(exp != document.form.textview.value){
			result = true;
		}
	}
}

function clean(){
	document.form.textview.value = "";
}

function back(){
	var doc = document.form.textview.value;
	document.form.textview.value = doc.substring(0,doc.length-1);

}
