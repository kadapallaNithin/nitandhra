#include "./parser.h"
class Pre:Parser{
	public:
		bool pre(){
			cout<<"\n"<<input[i];
			if(input[i]=='+'){
				match('+');
				pre();
				pre();
			}else if(input[i] == '-'){
				match('-');
				pre();
				pre();
			}else{
				match('a');
			}
		}
		bool parse(){
			i = 0;
			pre();
			return i == len-1;
		}
		void readnparse(){
			read_parse('\n');
		}
};/*
bool Pre::parse(){
			i = 0;
			pre();
			return i == len-1;
}
*/
int main(){
	Pre p;
	p.readnparse();
//cout<<"Hello world";
	return 0;
}
