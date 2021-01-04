function Node(val){
  	this.right = null;
  	this.left = null;
  	this.value = val;
};

Node.prototype.addNode = function(n){
	if (n.value > this.value){
		if (this.right == null){
			this.right = n;
		}else {
			this.right.addNode(n);
		}
	}else if(n.value < this.value) {
		if (this.left == null){
			this.left = n;
		}else {
			this.left.addNode(n);
		}
	}
};

Node.prototype.visit = function() {
	if (this.left != null) {
		this.left.visit();
	}

	console.log(this.value);

	if (this.right != null) {
		this.right.visit();
	}
};

Node.prototype.search = function(val) {
	if (val == this.value){
		return this;
	}else if (val < this.value && this.left != null){
		return this.left.search(val);
	}else if (val > this.value && this.right != null){
		return this.right.search(val);
	}
	return null;
};