#include<iostream>
using namespace std;
#define MAX_SI 300
class Parser{
	public:
		char input[MAX_SI];
		int i;
		int len;

		Parser(){
			i = 0;
			len = 0;
		}
		bool match(char ch){
			if(ch == input[i]){
				i++;
				return true;
			}else{
				cout<<"Error "<<ch<<endl;				
				return false;
			}
		}
		void read(char deli = '\n'){
			char c = ' ';
			while(c != deli && len < MAX_SI){
				c = getchar();
				input[i++] = c;
				len++;
			}
		}
		virtual bool parse() = 0;//			i = 0;
		
		bool parse_f(int* pos){
			i = 0;
			if(parse()&& (i == len - 1)){
				return true;
			}else{
				*pos = i;
				return false;
			}
		}
		/*void read_parse(){
			read();
			parse();
//			pre();
		}*/
		void read_parse(char deli = '\n'){
			read('\n');
			int pos;
			if(parse_f(&pos))
				cout<<"Success";
			else
				cout<<"Error at "<<pos;
//			i = 0;
//			pre();
		}
};
