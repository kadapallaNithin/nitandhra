//JavaScript
function mini(root){
	if(root.children.length > 0){
		minkey = root.children[0].key;
		minim = root.children[0].obj[0];
		for(var child in root.children){
			if(minim > root.children[child].obj[0]){
		  		minim = root.children[child].obj[0];
		  		minkey = root.children[child].key;
			}
	  	}
	  	return [minim,minkey];
	}
	return [];
}
function maxi(root){
	if(root.children.length > 0){
		maxkey = root.children[0].key;
	  	maxim = root.children[0].obj[0];
	  	for(var child in root.children){
			if(maxim < root.children[child].obj[0]){
		  		maxim = root.children[child].obj[0];
		  		maxkey = root.children[child].key;
			}
	  	}
	  	return [maxim,maxkey];
	}
	return []
}
function minimax(root,state){
	if(evalu(state) == NaN){

	}else{

	}

}
(function(){ 
var b=[[9,8,7],[6,5,4],[3,2,10]];
var minimaxtree = minimax(root,b);

})()
