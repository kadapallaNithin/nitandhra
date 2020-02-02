#include "./parser.h"
class Par:Parser{
	public:
		bool par(){
			if(input[i] == '('){
				return match('(') && par() && match(')') && par() && par();
			}
			return true;
		}
		bool parse(){
			return par();
		}
		void readnparse(){
			read_parse();
		}
};
int main(){
Par p;
p.readnparse();
return 0;
}
