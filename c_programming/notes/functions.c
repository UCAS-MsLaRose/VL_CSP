// VL 6th Functions Notes
#include <stdio.h>

void birthday(char* name, int age){
    printf("Happy Birthday to you\n");
    printf("Happy Birthday to you\n");
    printf("Happy Birthday dear %s\n", name);
    printf("Happy Birthday to you!\n");
    printf("Happy Birthday %s is now %d\n", name, age);
}

int add(int num_one, int num_two){
    return num_one + num_two;
}

char* get_name(void){
    char *name;
    printf("What is your name: ");
    scanf("%s",name);
    return name;
}
float get_num(void){
    float num;
    printf("Tell me a number: ");
    scanf("%f", &num);
    return num;
}

int main(void){
    birthday("Mykel", 15);
    birthday("Lucas", 40);
    birthday("Victoria", 19);
    char* user = get_name();
    birthday(user, 5);
    int addition = add(5,4);
    printf("%d\n", addition);
    printf("%d\n", add(50,37));
    float our_number = get_num();
    printf("%f\n", our_number);

    return 0;
}