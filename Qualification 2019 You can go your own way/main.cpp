#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);
    int t,n;
    char c;
    cin>>t;
    for(int i=1;i<=t;i++){
        cin>>n;
        cout<<"Case #"<<i<<": ";
        for(int aux=1;aux<=n*2-2;aux++){
            cin>>c;
            if(c=='E') cout<<'S';
            else cout<<'E';
        }
        cout<<'\n';
    }

    return 0;
}
/// xD
