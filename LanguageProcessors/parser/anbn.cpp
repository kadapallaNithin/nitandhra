#include "parser.h"
class anbn:Parser{
		bool anbn_f(){
			if(input[i]== 'a')
			{
				if(input[i+1]=='b')
				{	
					match('a');
					match('b');
					return true;
				}else
				{
					return match('a') && anbn_f() && match('b');
				}
				
			}
			return false;
		}
	public:

		bool parse(){
			return anbn_f();
		}
		void readnparse(){
			read_parse();
		}
		
};
int main(){
	anbn p;
	p.readnparse();
	return 0;
}
