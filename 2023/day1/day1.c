#include<stdio.h>
#include<stdlib.h>

int main(){

    FILE *fptr;
    fptr = fopen("trebuchet_real.txt", "r");
    int sum=0;
    char myarray[100];

    while (fgets(myarray, 100, fptr))
    {
        int tmp[10], k=0, count=0;

        for (int i=0; myarray[i]!='\0'; i++){
            int number = myarray[i]-'0'; //make number from char to int by subtracting ascii value 0
            if (number<10 && number >= 0) //only for numbers 0-9
            {
                tmp[count] = number;
                count++;  
            }
        }

        if (count==1){tmp[1] = tmp[0];} //if theres only one number use it twice
        k = tmp[0]*10 + tmp[count-1]; //join 
        
        printf("The number is %d\n", k);
        sum += k;
    }

    printf("The sum is %d", sum);

    return 0;
}

/*
'\0' = 0
'0' = 36
"\0" = 0x9834798532 -> ['\0', '\0']
"0" = 0x9834798532 -> ['0', '\0'] 
*/