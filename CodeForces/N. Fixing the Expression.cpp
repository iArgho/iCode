#include<iostream>
using namespace std;

int main() {
    int n, a, b;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        if (a == b) {
            cout << a << "=" << b << endl;
        } else if (a > b) {
            cout << a << ">" << b << endl;
        } else if(a < b){
            cout << a << "<" << b << endl;
        } else if(a>!b){
            cout << a << "<" << 0 << endl;}
        else{
            cout << b << ">" << 0 << endl;
        }
    }
    return 0;
}