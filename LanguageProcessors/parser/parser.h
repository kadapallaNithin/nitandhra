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
		void read(char deli){
			char c = ' ';
			while(c != deli && len < MAX_SI){
				c = getchar();
				input[i++] = c;
				len++;
			}
		}
		void read(){
			read('\n');
		}
		void parse(){
			i = 0;
		}
		/*void read_parse(){
			read();
			parse();
//			pre();
		}*/
};
