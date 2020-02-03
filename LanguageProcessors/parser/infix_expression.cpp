#include "parser.h"
class Exp:Parser{
    public:
        bool exp(){
            return term()&&exp_r();
        }
        bool exp_r(){
            if(input[i]=='+'){
                return match('+')&&term()&&exp_r();
            }else if(input[i] == '-'){
                return match('-')&&term()&&exp_r();
            }
        }
        bool term(){
            return factor()&&term_r();
        }
        bool term_r(){
            if(input[i]=='*'){
                return match('*')&&factor()&& term_r();
            }else if(input[i]=='/'){
                return match('/')&&factor()&&term_r();
            }
        }
        bool factor(){
            if(input[i]=='('){
                return match('(')&&exp()&&match(')');
            }else if(isdigit(input[i])){
                    match(input[i]);
                    return true;
            }
            return false;
        }
        bool parse(){
            return exp();
        }
        void readnparse(){
            read_parse();
        }
};
int main(){
    Exp e;
    e.readnparse();
    return 0;
}