#include <iostream>
#include <algorithm>
using namespace std;
long long int s1[50002];
long long int s2[50002];
int t,n,i,lS1,lS2,troubleIndice,anterior,actual,pS1,pS2;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin>>t;
    for(int caso=1;caso<=t;caso++){
        cin>>n;
        lS1=lS2=-1;
        for(i=0;i<n;i++){
            if(i%2==0) cin>>s1[++lS1];
            else cin>>s2[++lS2];
        }
        sort(s1,s1+lS1+1);
        sort(s2,s2+lS2+1);
        troubleIndice=-1;
        anterior=-1;
        pS1=pS2=i=0;
        while(true){
            if(i%2==0){
                if(pS1>lS1) break;
                actual=s1[pS1++];
            }else{
                if(pS2>lS2) break;
                actual=s2[pS2++];
            }
            if(actual<anterior){
                troubleIndice=i-1;
                break;
            }
            anterior=actual;
            i++;
        }
        cout<<"Case #"<<caso<<": ";
        if(troubleIndice!=-1)  cout<<troubleIndice;
        else cout<<"OK";
        cout<<'\n';
    }
    
    return 0;
}
/**
1
10
1 2 3 4 5 6 7 8 9 10
**/