#include <iostream>
#include <math.h>
using namespace std;
int t,limitDamage,i,currentDamage,hacks,damageByShot;
string atack;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin>>t;
    for(int caso=1;caso<=t;caso++){
        cin>>limitDamage;
        cin>>atack;
        currentDamage=hacks=0;
        damageByShot=1;
        for(char i:atack){
            if(i=='S') currentDamage+=damageByShot;
            else damageByShot*=2;
        }
        i=atack.size()-1;
        while(atack[i]=='C'){
            damageByShot/=2;
            i--;
        }
        if(i>atack.size()-2) i=atack.size()-2;
        while(currentDamage>limitDamage and i>=0){
            //cout<<i<<" "<<atack[i]<<endl;
            if(atack[i]=='C' and atack[i+1]=='S'){
                swap(atack[i],atack[i+1]);
                currentDamage-=(damageByShot/2);
                i++;
                if(i==atack.size()-1 or atack[i+1]=='C'){
                    i--;
                    damageByShot/=2;
                }
                hacks++;
            }else{
                i--;
            }
        }
        cout<<"Case #"<<caso<<": ";
        if(currentDamage<=limitDamage) cout<<hacks;
        else cout<<"IMPOSSIBLE";
        cout<<'\n';
    }

    return 0;
}
/***


***/