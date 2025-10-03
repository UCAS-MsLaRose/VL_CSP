// VL 6th Varibles Notes
/*
this is a comment
*/
#include <stdio.h>

int main(void){
    int num;
    const float pi = 3.14; //constants cannot be changed
    char grade; //Will only hold 1 letter
    char name[20];
    //bool passing = true;
    printf("What is your letter grade: ");
    scanf("%c", &grade);

    printf("Tell me a number: ");
    scanf("%d", &num);
    //This imput lets me get a space
    printf("Tell me your name: ");
    fgets(name, sizeof(name), stdin);

    printf("%d\n", num);
    printf("%s has a %c grade in the class!\n", name, grade);

    return 0;
}