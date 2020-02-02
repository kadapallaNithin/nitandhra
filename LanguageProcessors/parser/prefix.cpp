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
		void read_parse(){
			read();
			if(parse())
				cout<<"Success";
			else
				cout<<"Error";
//			i = 0;
//			pre();
		}

};
int main(){
	Pre p;
	p.read_parse();
//cout<<"Hello world";
	return 0;
}
