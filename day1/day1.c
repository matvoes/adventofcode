#include<stdio.h>
#include<stdlib.h>

int main(){

    FILE *fptr;
    fptr = fopen("trebuchet.txt", "r");
    int sum=0;

    for (int i=0; i < 4; i++)
    {
        int tmp[2], k=0, count=0;
        char myarray[100];
        fgets(myarray, 100, fptr);

        for (int i=0; myarray[i]!='\0'; i++){
            int number = myarray[i]-'0'; //make number from char to int by subtracting ascii value 0
            if (number<10 && number >= 0) //only for numbers 0-9
            {
                tmp[count] = number;
                count++;  
            }
        }

        if (count==1){tmp[1] = tmp[0];} //if theres only one number use it twice
        for (int i = 0; i < 2; i++){k = k*10 + tmp[i];} //join the two numbers to one number
        
        printf("Tallet er %d\n", k);
        sum += k;
    }

    printf("Summen er %d", sum);

    return 0;
}

/*
'\0' = 0
'0' = 36
"\0" = 0x9834798532 -> ['\0', '\0']
"0" = 0x9834798532 -> ['0', '\0'] 
*/