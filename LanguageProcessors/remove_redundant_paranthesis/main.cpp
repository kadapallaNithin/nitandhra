#include<iostream>
#include<string>
#define STACK_SIZE 256
using namespace std;
class Stack{
	char s[STACK_SIZE];
	int top;
	public:
	Stack(){
		top = 0;
		//cout<<"Created stack";
	}
	void push(char c){
		if(top == STACK_SIZE )
			return ;
		s[top++] = c;
	}
	char pop(){
		if(top == 0)
		    return '\0';
		return s[--top];
	}
	string contents(){
		char cont[STACK_SIZE+1];
		for(int i = 0;i< top; i++){
			cont[i] = s[i];
		}
		cont[top] = '\0';
		return cont;
	}
	void print(){
		for(int i=0; i<top; i++){
			cout<<s[i]<<" ";
		}
		cout<<endl;
	}
};
int priority(char op){
	if(op=='('){
		return 0;
	}else if(op=='+' || op=='-')
		return 1;
	else if(op == '*' || op == '/'){
		return 2;
	}
	return -1;
}
void rm_red_par(string exp){
	char c = exp[0];
	int i =1;
	while(c != '\0'){
		cout<<c;
		c = exp[i++];
	}
}
int main(){
	Stack s;
	rm_red_par("(a+b)");	
	return 0;
}
