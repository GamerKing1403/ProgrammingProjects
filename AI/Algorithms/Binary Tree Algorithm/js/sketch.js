var tree;
var input;
var button;

function find() {
	var val = input.value();
	result = tree.search(val);
	if (result != null) {
		createP("Found " + result.value);
	}else{
		createP("Not Found");
	}
};

function keyPressed(){
	if (keyCode == ENTER){
		find();
	}
}

function setup(){
	noCanvas();
	input = createInput().attribute('placeholder','Input The Number you Want To Search For!!');
	button = createButton('submit');
	tree = new Tree();
	for (var i = 0; i < 10; i++) {
		var value = floor(random(0,100));
		tree.addValue(value);
	}
	button.mousePressed(find);
};