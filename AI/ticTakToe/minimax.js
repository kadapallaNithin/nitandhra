//JavaScript

/*

`root` of the minimax (sub)tree
*/
function mini(root) {
	if (root.children.length > 0) {
		var minkey = root.children[0].key;
		var minim = root.children[0].obj[0];
		for (var child in root.children) {
			if (minim > root.children[child].obj[0]) {
				minim = root.children[child].obj[0];
				minkey = root.children[child].key;
			}
		}
		return [minim, minkey];
	}
	return [];
}
function maxi(root) {
	if (root.children.length > 0) {
		var maxkey = root.children[0].key;
		var maxim = root.children[0].obj[0];
		for (var child in root.children) {
			if (maxim < root.children[child].obj[0]) {
				maxim = root.children[child].obj[0];
				maxkey = root.children[child].key;
			}
		}
		return [maxim, maxkey];
	}
	return []
}
/*
returns -1 if O wins
		0  if draw
		1  if x wins
		NaN otherwise i.e unknownerror
	state of board
	count of number of steps

	//assumptions
	state[.][.] is  0 if X is there
					1 if O is there
*/
function evalu(state, count) {
	for (var i = 0; i < state.length; i++) {
		if (state[i][0] == state[i][1] && state[i][1] == state[i][2]) {
			if (state[i][0] == 0) {// X won
				return 1;
			} else if (state[i][0] == 1) { // O won
				return -1;
			}
		}
	}
	for (var j = 0; j < 3; j++) {
		if (state[0][j] == state[1][j] && state[1][j] == state[2][j]) {
			if (state[0][j] == 0) { // X won
				return 1;
			} else if (state[0][j] == 1) { // O won
				return -1;
			}
		}
	}
	if (state[0][0] == state[1][1] && state[0][0] == state[2][2]) {
		if (state[0][0] == 0) { // X won
			return 1;
		} else if (state[0][0] == 1) { // O won
			return -1;
		}
	}
	if (state[0][2] == state[1][1] && state[1][1] == state[2][0]) {
		if (state[0][2] == 0) { // X won
			return 1;
		} else if (state[0][2] == 1) { // O won
			return -1;
		}
	}
	if (count == 9)
		return 0;
	return NaN;
}
function mini_build(root,state,count){
	var ev = evalu(state,count);
	if( isNaN(ev) ){
		for(var i=0; i<9; i++){
			var s = state[parseInt(i/3)][i%3];
			if(s != 0 && s != 1){
				state[parseInt(i/3)][i%3] = 0;
				count++;
				var t = new tree_node(i,[]);
				maxi_build(t,state,count);
				root.children.push(t);
				count--;
				state[parseInt(i/3)][i%3] = NaN;
			}
		}
		var M = mini(root);
		root.obj = M;
	}else{
		root.obj = [ev,NaN];
	}
}
function maxi_build(root,state,count){
	var ev = evalu(state,count);
	if( ev == NaN ){
		for(var i=0; i<9; i++){
			var s = state[parseInt(i/3)][i%3];
			if(s != 0 && s != 1){
				state[parseInt(i/3)][i%3] = 1;
				count++;
				var t = new tree_node(i,[]);
				mini_build(t,state,count);
				root.children.push(t);
				count--;
				state[parseInt(i/3)][i%3] = NaN;
			}
		}
		var M = maxi(root);
		root.obj = M;
	}else{
		root.obj = [ev,NaN];
	}

}
/*

*/
function minimax(key, state, count) {
	var evl = evalu(state, count);
	if (evl == NaN) {
	} else {
		var root = new tree_node(key, []);
		root.obj = [evl, NaN];
		return root;
	}
}
(function () {
	var tree_board = [[9, 8, 7], [6, 5, 4], [3, 2, 10]];
	var count = 0;
	minimaxtree = minimax(root, tree_board, count);
})();