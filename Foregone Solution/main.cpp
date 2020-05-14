#include <bits/stdc++.h>
using namespace std;
string N,a,b;
int pos;

void SumaCadena(string &cadena,short sumar,int pos){
    int i=cadena.size()-1;
    while(pos>1){
        pos--;
        i--;
    }
    if(i<0){
        i++;
        while(i<0){
            cadena.insert(0,"0");
            i++;
        }
        cadena.insert(0,"1");
        return;
    }
    cadena[i]+=sumar;
    if(cadena[i]>'9'){
        while(cadena[i]>'9'){
            cadena[i]='0';
            if(i-1>=0) cadena[i-1]++;
            i--;
        }
        if(cadena[0]=='0') cadena.insert(0,"1");
    }else if(cadena[i]<'0'){
        while(cadena[i]<'0'){
            cadena[i]='9';
            if(i-1>=0) cadena[i-1]--;
            i--;
        }
        if(cadena[cadena.size()-1]<'0') cadena.erase(1,1);
    }
}

int Buscar4(string &cadena){
    int pos=1;
    int i=cadena.size()-1;
    while(cadena[i]!='4' && i>=0){
        pos++;
        i--;
    }
    if(i>-1) return pos;
    else return -1;
}

void Compute(int &i){
    a=N;
    SumaCadena(a,-1,1);
    b="1";
    while(true){
        pos=Buscar4(a);
        if(pos!=-1){
            SumaCadena(a,-1,pos);
            SumaCadena(b,1,pos);
            continue;
        }
        pos=Buscar4(b);
        if(pos!=-1){
            SumaCadena(a,-1,pos);
            SumaCadena(b,1,pos);
        }else break;
    }
    cout<<"Case #"<<i<<": "<<a<<" "<<b<<'\n';
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T;
    cin>>T;
    for(int i=1;i<=T;i++){
        cin>>N;
        Compute(i);
    }
    return 0;

}
/// xD
/**
210434104
**/