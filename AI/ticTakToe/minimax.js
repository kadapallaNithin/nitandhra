//JavaScript
function mini(root){
	if(root.children.length > 0){
		minkey = root.children[0].key;
	  minim = root.children[0].obj[0];
	  for(var child in root.children){
		if(minim > child.obj[0]){
		  minim = child.obj[0];
		  minkey = child.key;
		}
	  }
	  return [minim,minkey];
	}
	return [];
}
function max(root){
	if(root.children.length > 0){
		maxkey = root.children[0].key;
	  	maxim = root.children[0].obj[0];
	  	for(var child in root.children){
			if(maxim < child.obj[0]){
		  		maxim = child.obj[0];
		  		maxkey = child.key;
			}
	  	}
	  	return [maxim,maxkey];
	}
	return []
}

function minimax(root){

}


