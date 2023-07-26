#ifndef ATM_H_
#define ATM_H_
#include <stdbool.h>//function login kata gua pake bool aja return typenya mau gimana ni pake string aja? buat pwnya gitu maksudnya 
/*iya pw pake string aja, itu login gua return type int soalnya ntar ngereturn index dari account yg di login in aja gt gua mikirnya nah kalo -1 brarti gagal login okeh bb*/
#include <time.h>

typedef struct{
    struct tm *tm;
    char recordedTime[50];
    bool type;//true = mendiri account, false = non mendiri
    bool give;
    char accNum[20];
    char name[50];
    long long int amount;
}transferHistory;

typedef struct{
    struct tm *tm;
    char recordedTime[50];
    char paymentType[50];
    long long int amount;
}paymentHistory;

typedef struct{
    struct tm *tm;
    char recordedTime[50];
    bool type; //true = deposit, false = withdraw
    long long int amount;
}depositWithdrawHistory;

typedef struct{
    char name[50];
    char birth[20];
    char phoneNum[15];
    char address[100];
    char occupation[30];
    long long int balance;
    char accNum[6];
    char userID[50];
    char password[50];
    bool deleted;
    int totalTrans;
    int totalPay;
    int totalDepo;
    transferHistory * transH;
    paymentHistory * payH;
    depositWithdrawHistory * depoH;
}account;

account * addAccount(account * accounts);
int findAccount(account * accounts, char Id[50], int totalRegist);
int findAccountViaNum(account * accounts, char Id[50], int totalRegist);
int login(account * accounts, int index, int totalRegist); //if return -1, login unsuccessful.
void accountMenu(account * accounts, int index, int totalRegist, int *inactive);
void printCustomer(account * accounts, int totalRegist);
void printDelCustomer(account * accounts, int totalRegist);
void deposit(account * accounts, int index);
void withdraw(account * accounts, int index);
void transfer(account * accounts, int index, int totalRegist);
void payment(account * accounts, int index);
void printAccountHistory(account * accounts, int index);
void printAccInfo(account * accounts, int index);
void changePass(account * accounts, int index);
void editInfo(account * accounts, int index);
bool deactivate(account * accounts, int index, int *inactive);
void menuTransition();
void clrscr(); 

#endif