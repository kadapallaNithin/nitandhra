#include<iostream>
using namespace std;
#define SIZE 256
char inp[SIZE];
int lah = 0;
char pr[][4] = {"aSa","aa"};
int len[] = {3,2};
int s(int tlah,int n){
    cout<<"s";
    int error = 0;
    int k = 0;
    do{
        error = 0;
        cout<<"\ntrying "<<2*n+k<<' ';
        for(int i = 0; i<len[k] && !error; i++){
            if(pr[k][i] == inp[lah]){
                lah++;
                cout<<lah;
            }else if(pr[k][i] == 'S'){
                error = s(lah,2*n+k);
            }else{
                error = 1;
                cout<<"\tlah = "<<lah;
            }
        }
        if(error){
            lah = tlah;
        }
        k++;
    }while(error && k < 2);
    if(error && k == 2){
        cout<<" returning "<<error<<' '<<k;
        return error;
    }
//    lah = tlah;
    return 0;

}
int main(){
    cout<<"Enter string ";
    char c = getchar();
    int i = 0;
    while(c != EOF && i < SIZE){
        inp[i] = c;
        c = getchar();
        i++;
        if(c == '\n'){
            inp[i] = '\n';
            break;
        }
    }
    cout<<inp;
    cout<<s(0,1)<<'\t'<<lah;
    return 0;
}