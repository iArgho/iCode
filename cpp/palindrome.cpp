#include <iostream>
#include <string>
using namespace std;

int main() {
    int a;
    string b; 
    cin >> a;

    b = to_string(a);
    long int l=b.length();
    long int arr1[l],arr2[l];
    
    int temp=0;
    for(long int i=0;i<l;i++){
        arr1[i]=a%10;
        arr2[i]=arr1[i];
        temp=a/10;
        a=temp;
        }

    reverse(arr1, arr1 + l);
    bool boolFlag;

    for(long int i=0;i<l/2;i++)
    {
        if(arr1[i]==arr2[i]){
            boolFlag=true;
        }
        else
        {
            boolFlag=false;
            break;
        }
    }

    if(boolFlag==true){
        cout<<"The Number is Palindrome"<<endl;
    }
    else
    {
        cout<<"The Number is not Palindrome"<<endl;
    }
}