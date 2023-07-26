#include "atm.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h> 
#include <time.h>
#include <ctype.h>
#include <conio.h>

account *addAccount(account *accounts)
{
    static int index = 0;
    srand(time(NULL));
    char cTemp;
    int tempInt;
    int i;
    if(index > 0)//for allocating more memory. Main.c will have malloc for the first index of the array.
    {
        accounts = realloc(accounts, (index + 1) * sizeof(account));
    }
    char temp[50];
    accounts[index].deleted = false;
    printf("==Fill Your Personal Data==\n");
    printf("Name : ");
    fgets(temp, 50, stdin);
    if ((strlen(temp) > 0) && (temp[strlen (temp) - 1] == '\n'))
        temp[strlen (temp) - 1] = '\0';
    strcpy(accounts[index].name, temp);
    printf("Birth : ");
    fgets(temp, 20, stdin);
    if ((strlen(temp) > 0) && (temp[strlen (temp) - 1] == '\n'))
        temp[strlen (temp) - 1] = '\0';
    strcpy(accounts[index].birth, temp);
    printf("Phone Number : ");
    fgets(temp, 15, stdin);
    if ((strlen(temp) > 0) && (temp[strlen (temp) - 1] == '\n'))
        temp[strlen (temp) - 1] = '\0';
    strcpy(accounts[index].phoneNum, temp);
    printf("Current Address : ");
    fgets(temp, 100, stdin);
    if ((strlen(temp) > 0) && (temp[strlen (temp) - 1] == '\n'))
        temp[strlen (temp) - 1] = '\0';
    strcpy(accounts[index].address, temp);
    printf("Occupation : ");
    fgets(temp, 30, stdin);
    if ((strlen(temp) > 0) && (temp[strlen (temp) - 1] == '\n'))
        temp[strlen (temp) - 1] = '\0';
    strcpy(accounts[index].occupation, temp);
    printf("\n<<Personal Data Input Successful>>\n");
    printf("\nFirst Deposit Amount (Mandatory): Rp");
    scanf("%lld", &accounts[index].balance);
    printf("\n<<First Deposit Successful>>\n");
    printf("\n==Create Account for Mendiri E-Banking==\n");
    printf("User ID(Space not allowed!): ");
    scanf("%s", accounts[index].userID);
    printf("Password(Space not allowed!): ");
    scanf("%s", accounts[index].password);
    //Initialize some member
    accounts[index].totalDepo = 0;
    accounts[index].totalPay = 0;
    accounts[index].totalTrans = 0;
    printf("\n<<M-Banking Account Creation Successful>>\n\n");
    //ACCOUNT NUMBER GENERATION. It is Randomly Generated//
    for(i = 0 ; i < 5 ; i++)
    {
      tempInt = rand() % 10;
      cTemp = tempInt + '0';
      accounts[index].accNum[i] = cTemp;
    }
    accounts[index].accNum[5] = '\0';
    printf("<<Account Creation Successful!>>\n");
    printf("<<Your account's number is: %s>>", accounts[index].accNum);
    index++;
    return accounts;
}

void printCustomer(account * accounts, int totalRegist){
  int i;
  for(i = 0; i < totalRegist; i++){
    if((accounts + i)->deleted == false){
      printf("Name           : %s\n", (accounts + i)->name);
      printf("Account Number : %s\n", (accounts + i)->accNum);
      printf("\n");
    }
  }
}
//Function for deactivated account or blocked account
void printDelCustomer(account * accounts, int totalRegist){
  int i;
  for(i = 0; i < totalRegist; i++){
    if((accounts + i)->deleted){
      printf("Name           : %s\n", (accounts + i)->name);
      printf("Account Number : %s\n", (accounts + i)->accNum);
      printf("\n");
    }
  }
}

int login(account * accounts, int index, int totalRegist){//if return -1, login unsuccessful.
  int i;
  char name[50], password[50];
  for(i = 2 ; i > -1 ; i--)
  {
    printf("Enter Account name     : ");
    getchar();
    fgets(name, 50, stdin);
    if ((strlen(name) > 0) && (name[strlen (name) - 1] == '\n'))
      name[strlen (name) - 1] = '\0';
    printf("Enter Account Password : ");
    scanf("%s", password);
    if(strcmp(name, (accounts + index)->name) == 0 && strcmp(password, (accounts + index)->password) == 0)
    {
      return index;
    }
    else
    {
      printf("Incorrect Account Name or Password. Try Again! (%d attempt(s) left)\n", i);
    }
  }
  //After 3 attempt, failed to login, aaccount will be deactivated
  printf("<<Login Unsuccessful!>>\n");
  accounts[index].deleted = true;
  return -1;
} 
//finding account by the userID
int findAccount(account * accounts, char Id[50], int totalRegist){
  int i;
  for(i = 0; i < totalRegist; i++){
    if(strcmp(Id, (accounts + i)->userID) == 0 && strlen((accounts + i)->name) > 0){
      if((accounts + i)->deleted == false){
        return i;
      	}
      }
    }
    return -1;
}
//Main menu for Personal Account after Log in  
void accountMenu(account * accounts, int index, int totalRegist, int *inactive)
{ 
	int indicator;
	bool deactive = false;
  	do{
      printf("============%s's Account============\n", accounts[index].name);
      printf("--Current Balance: Rp%lld--\n", accounts[index].balance);
      printf("--Account Number: %s--\n", accounts[index].accNum);
      printf("(1) Deposit\n");
      printf("(2) Withdraw\n");
      printf("(3) Transfer\n");
      printf("(4) Payment\n");
      printf("(5) Show Account History\n");
      printf("(6) Show Account Info\n");
      printf("(7) Change Password\n");
      printf("(8) Edit Account Info\n");
      printf("(9) Deactivate Account\n");
      printf("(10) Clear Screen\n");
      printf("(99) Log Out\n");
      printf("> ");
      scanf("%d", &indicator);
      getchar();
      if(indicator == 1)
      {
      	clrscr();
        deposit(accounts, index);
        menuTransition();
      } 
      else if(indicator == 2)
      {
      	clrscr();
        withdraw(accounts, index);
        menuTransition();
      }
      else if(indicator == 3)
      {
      	clrscr();
        transfer(accounts, index, totalRegist);
        menuTransition();
      }
      else if(indicator == 4)
      {
      	clrscr();
        payment(accounts, index);
        menuTransition();
      }
      else if(indicator == 5)
      {
      	clrscr();
        printAccountHistory(accounts, index);
        menuTransition();
      }
      else if(indicator == 6)
      {
      	clrscr();
        printAccInfo(accounts, index);
        menuTransition();
      }
      else if(indicator == 7)
      {
      	clrscr();
        changePass(accounts, index);
        menuTransition();
      }
      else if(indicator == 8)
      {
      	clrscr();
        editInfo(accounts, index);
        menuTransition();
      }
      else if(indicator == 9)
      {
      	clrscr();
        deactive = deactivate(accounts, index, inactive);
        if(deactive)
        {
        	printf("\n");
        	return;
    	}
        menuTransition();
	}
      else if(indicator == 10)
      {
        clrscr();	
      }
      else if(indicator == 99)//log out
        break;
  }while(indicator != 99);
  printf("\n<<Log out Successful>>");
}

void deposit(account * accounts, int index){
  long long int amountTemp;
  do{
  printf("====Deposit Menu====\n");
  printf("Enter deposit amount (-1 to cancel): Rp");
  scanf("%lld", &amountTemp);
  if(amountTemp == -1)
  {
    printf("\n<<Deposit Canceled!>>\n");
    return;
  }
  else if(amountTemp < -1)
  {
    printf("\n<<Invalid Amount. Retrying...>>\n\n");
  }
  else{
  	//assigning values to the struct
    int index2 = accounts[index].totalDepo;
    if(accounts[index].totalDepo == 0)
      accounts[index].depoH = (depositWithdrawHistory*)malloc(sizeof(depositWithdrawHistory));
    else
      accounts[index].depoH = realloc(accounts[index].depoH, (accounts[index].totalDepo + 1) * sizeof(depositWithdrawHistory));
    accounts[index].depoH[index2].type = true;
    accounts[index].balance += amountTemp;
    accounts[index].depoH[index2].amount = amountTemp;
    printf("\n<<Deposit Complete>>\n");
    printf("<<Current Balance Now: Rp%lld>>\n", (accounts + index)->balance);
    time_t t = time(NULL);
    accounts[index].depoH[index2].tm = localtime(&t);
    strcpy(accounts[index].depoH[index2].recordedTime, asctime(accounts[index].depoH[index2].tm));
    accounts[index].totalDepo += 1;
    return;
    }
  }while(true);
}

void withdraw(account * accounts, int index){
  long long int amountTemp;
  do{
    printf("====Withdraw Menu====\n");
    printf("Enter withdraw amount (-1 to cancel): Rp");
    scanf("%lld", &amountTemp);
    if(amountTemp == -1)
    {
      printf("\n<<Withdraw Canceled!>>\n");
      return;
    }
    else if(amountTemp < -1)
    {
      printf("\n<<Invalid Amount. Retrying...>>\n\n");
    }
    else if(amountTemp > accounts[index].balance)
    {
      printf("\n<<Insufficient Funds in Your Account. Retrying...>>\n\n");
    }
    else{
    	//assigning values to the struct
      int index2 = accounts[index].totalDepo;
      if(accounts[index].totalDepo == 0)
        accounts[index].depoH = (depositWithdrawHistory*)malloc(sizeof(depositWithdrawHistory));
      else
        accounts[index].depoH = realloc(accounts[index].depoH, (accounts[index].totalDepo + 1) * sizeof(depositWithdrawHistory));
      accounts[index].depoH[index2].type = false;
      accounts[index].balance -= amountTemp;
      accounts[index].depoH[index2].amount = amountTemp;
      printf("\n<<Withdraw Complete>>\n");
      printf("<<Current Balance Now: Rp%lld>>\n", (accounts + index)->balance);
      time_t t = time(NULL);
      accounts[index].depoH[index2].tm = localtime(&t);
      strcpy(accounts[index].depoH[index2].recordedTime, asctime(accounts[index].depoH[index2].tm));
      accounts[index].totalDepo += 1;
      return;
    }
  }while(true);
}

void payment(account * accounts, int index)
{
  long long int amountTemp;
  int choice;
  char temp[50];
  do{
    printf("=====Payment Menu=====\n");
    printf("Payment for:\n");
    printf("(1) Electricity\n");
    printf("(2) BPJS\n");
    printf("(3) Tax\n");
    printf("(4) Credit Card\n");
    printf("(5) Insurance\n");
    printf("(6) Custom\n");
    printf("(-1) Cancel\n");
    printf("> ");
    scanf("%d", &choice);
    if(choice == 6)
    {
    	clrscr();
    	printf("==Custom Payment==\n");
      	printf("\nWhat's the payment for? ");
      	getchar();
      	fgets(temp, 50, stdin);
      	if ((strlen(temp) > 0) && (temp[strlen (temp) - 1] == '\n'))
        	temp[strlen (temp) - 1] = '\0';
    }
    else if(choice == -1)
    {
      	printf("\n<<Payment Canceled>>\n");
      	return;
    }
    do{
    	printf("\nEnter payment amount (-1 to cancel): Rp");
    	scanf("%lld", &amountTemp);
    	if(amountTemp == -1)
    	{
      		printf("\n<<Payment Canceled!>>\n");
      		return;
    	}
    	else if(amountTemp < -1)
    	{
      		printf("<<Invalid Amount. Retrying...>>\n");
    	}
    	else if(amountTemp > accounts[index].balance)
    	{
      		printf("<<Insufficient Funds in Your Account. Retrying...>>\n");
    	}
    	else{
    		//assigning values to the struct
      		int index2 = accounts[index].totalPay;
      		if(accounts[index].totalPay == 0)
        		accounts[index].payH = (paymentHistory*)malloc(sizeof(paymentHistory));
      		else
        		accounts[index].payH = realloc(accounts[index].payH, (accounts[index].totalPay + 1) * sizeof(paymentHistory));
      		accounts[index].balance -= amountTemp;
      		accounts[index].payH[index2].amount = amountTemp;
      		printf("\n<<Payment Complete>>\n");
      		printf("<<Current Balance Now: Rp%lld>>\n", (accounts + index)->balance);
     		time_t t = time(NULL);
      		accounts[index].payH[index2].tm = localtime(&t);
      		strcpy(accounts[index].payH[index2].recordedTime, asctime(accounts[index].payH[index2].tm));
      		accounts[index].totalPay += 1;
      		//Different type of payment would mean different strcpy
      		if(choice == 1)
      		{
        		strcpy(accounts[index].payH[index2].paymentType, "Electricity");
     		}
      		else if(choice == 2)
     		{
        		strcpy(accounts[index].payH[index2].paymentType, "BPJS");
      		}
      		else if(choice == 3)
      		{
        		strcpy(accounts[index].payH[index2].paymentType, "Tax");
      		}
      		else if(choice == 4)
      		{
        		strcpy(accounts[index].payH[index2].paymentType, "Credit Card");
      		}
      		else if(choice == 5)
      		{
        		strcpy(accounts[index].payH[index2].paymentType, "Insurance");
      		}
      		else if(choice == 6)
      		{
        		strcpy(accounts[index].payH[index2].paymentType, temp);
      		}
      		return;
    	}
	}while(true);
  }while(true);
}
//finding account index using account number
int findAccountViaNum(account * accounts, char Id[6], int totalRegist)
{
  int i;
  for(i = 0; i < totalRegist; i++){
    	if(strcmp(Id, (accounts + i)->accNum) == 0 && strlen((accounts + i)->name) > 0){
      		if((accounts + i)->deleted == false){
        		return i;
      		}
      		else{
        		return -2;
      		}
    	}
	}
    return -1;
}

void transfer(account * accounts, int index, int totalRegist)
{
  long long int amountTemp;
  int choice, indexDest;
  char temp[50];
  char temp2[20];
  do{
    printf("=====Transfer Menu=====\n");
    printf("Transfer To?\n");
    printf("(1) Mendiri Account\n");
    printf("(2) Non-Mendiri Account\n");
    printf("(-1) Cancel\n");
    printf("> ");
    scanf("%d", &choice);
    if(choice == 2)
    {
    	//non mendiri account, assume account number is always valid
    	clrscr();
    	printf("===Transfer To Non-Mendiri Account===\n");
      	printf("\nAccount Number: ");
     	scanf("%s", temp2);
      	printf("Name of The Account Owner: ");
      	getchar();
      	fgets(temp, 50, stdin);
      	if ((strlen(temp) > 0) && (temp[strlen (temp) - 1] == '\n'))
        	temp[strlen (temp) - 1] = '\0';
    }
    else if(choice == -1)
    {
      	printf("\n<<Transfer Canceled>>\n");
      	return;
    }
    else if(choice == 1)
    {
    	//mendiri account, needs to make sure accnum is correct
      do{
      	printf("===Transfer to Mendiri Account===\n");
      	printf("\nAccount Number (type \"exit\" to cancel): ");
      	scanf("%s", temp2);
      	if(strcmp(temp2, "exit\0") == 0)
      	{
        	printf("\n<<Transfer Canceled>>\n");
        	return;
      	}
      	else if(strlen(temp2) != 5)
      	{
        	printf("\n<<Invalid Account Number. Retrying...>>\n\n");
      	}
      	else
      	{
        	indexDest = findAccountViaNum(accounts, temp2, totalRegist);
        	if(indexDest == -1)
        	{
          		printf("\n<<Account Number Not Found. Retrying...>>\n");
          		continue;
        	}
        	else if(indexDest == -2)
        	{
          		printf("\n<<This Account Is Currently Deactivated>>\n");
          		printf("<<Transfer Attempt Terminated>>\n");
          		return;
        	}
        	else
        	{
          		int choice2;
          		clrscr();
          		printf("Account Name: %s\n", accounts[indexDest].name);
          		printf("Confirm?\n(1) Yes\n(2) No\n> ");
          		scanf("%d", &choice2);
          		if(choice2 == 1)
            		break;
          		else if(choice2 == 2)
          		{
            		printf("<<Retrying...>>\n");
            		continue;
          		}
        	}
      	}
      }while(true);
    }
    clrscr();
    do{
    	printf("Enter transfer amount (-1 to cancel): Rp");
    	scanf("%lld", &amountTemp);
    	if(amountTemp == -1)
    	{
      		printf("\n<<Transfer Canceled!>>\n");
      		return;
    	}
    	else if(amountTemp < -1)
    	{
      		printf("\n<<Invalid Amount. Retrying...>>\n");
    	}
    	else if(amountTemp > accounts[index].balance)
    	{
      		printf("\n<<Insufficient Funds in Your Account. Retrying...>>\n");
    	}
    	else{
      		int index2 = accounts[index].totalTrans;
      		if(accounts[index].totalTrans == 0)
        		accounts[index].transH = (transferHistory*)malloc(sizeof(transferHistory));
      		else
        		accounts[index].transH = realloc(accounts[index].transH, (accounts[index].totalTrans + 1) * sizeof(transferHistory));
      		accounts[index].balance -= amountTemp;
      		accounts[index].transH[index2].amount = amountTemp;
      		printf("\n<<Transfer Complete>>\n");
      		printf("<<Current Balance Now: Rp%lld>>\n", (accounts + index)->balance);
      		time_t t = time(NULL);
      		accounts[index].transH[index2].tm = localtime(&t);
      		strcpy(accounts[index].transH[index2].recordedTime, asctime(accounts[index].transH[index2].tm));
      		accounts[index].transH[index2].give = true;
      		accounts[index].totalTrans += 1;
      		if(choice == 2)
      		{
        		accounts[index].transH[index2].type = false;
        		strcpy(accounts[index].transH[index2].name, temp);
        		strcpy(accounts[index].transH[index2].accNum, temp2);
      		}
     		else if(choice == 1)
      		{
        		accounts[index].transH[index2].type = true;
        		strcpy(accounts[index].transH[index2].name, accounts[indexDest].name);
        		strcpy(accounts[index].transH[index2].accNum, accounts[indexDest].accNum);
        		//Inputting Transfer Data for Account Destination
        		int index3 = accounts[indexDest].totalTrans;
        		if(accounts[indexDest].totalTrans == 0)
          			accounts[indexDest].transH = (transferHistory*)malloc(sizeof(transferHistory));
        		else
          			accounts[indexDest].transH = realloc(accounts[indexDest].transH, (accounts[indexDest].totalTrans + 1) * sizeof(transferHistory));
        		accounts[indexDest].balance += amountTemp;
        		accounts[indexDest].transH[index3].amount = amountTemp;
        		strcpy(accounts[indexDest].transH[index3].name, accounts[index].name);
        		strcpy(accounts[indexDest].transH[index3].accNum, accounts[index].accNum);
        		accounts[indexDest].transH[index3].tm = localtime(&t);
        		strcpy(accounts[indexDest].transH[index3].recordedTime, asctime(accounts[indexDest].transH[index3].tm));
        		accounts[indexDest].transH[index3].give = false;
        		accounts[indexDest].transH[index3].type = true;
        		accounts[indexDest].totalTrans += 1;
      		}
      		return;
    	}
	}while(true);
  }while(true);
}
//account deposit/withdraw, payment, transfer history
void printAccountHistory(account * accounts, int index)
{
  int i;
  printf("====Account History=====\n\n");
  printf("<<Deposit/Withdraw History>>\n");
  for(i = 0 ; i < accounts[index].totalDepo ; i++)
    {
      printf("Time: %s", accounts[index].depoH[i].recordedTime);
      if(accounts[index].depoH[i].type)
      {
        printf("Amount: +Rp%lld\n", accounts[index].depoH[i].amount);
      }
      else
      {
        printf("Amount: -Rp%lld\n", accounts[index].depoH[i].amount);
      }
      printf("\n");
    }
  printf("<<Payment History>>\n");
  for(i = 0 ; i < accounts[index].totalPay ; i++)
    {
      printf("Time: %s", accounts[index].payH[i].recordedTime);
      printf("Transfer for: %s\n", accounts[index].payH[i].paymentType);
      printf("Amount: -Rp%lld\n", accounts[index].payH[i].amount);
      printf("\n");
    }
  printf("<<Transfer History>>\n");
  for(i = 0 ; i < accounts[index].totalTrans ; i++)
    {
      printf("Time: %s", accounts[index].transH[i].recordedTime);
      if(accounts[index].transH[i].type)
      {
        printf("%s Mendiri Account Number: %s\n", accounts[index].transH[i].give ? "To" : "From", accounts[index].transH[i].accNum);
        printf("Name: %s\n", accounts[index].transH[i].name);
        printf("Amount: %cRp%lld\n", accounts[index].transH[i].give ? '-' : '+', accounts[index].transH[i].amount);
        printf("\n");
      }
      else
      {
        printf("To Non-Mendiri Account Number: %s\n", accounts[index].transH[i].accNum);
        printf("Name: %s\n", accounts[index].transH[i].name);
        printf("Amount: -Rp%lld\n", accounts[index].transH[i].amount);
        printf("\n");
      }
      printf("\n");
    }
}
//outputtin account info (Full Data)
void printAccInfo(account * accounts, int index)
{
  printf("=====Account Info=====\n\n");
  printf("Name: %s\n", accounts[index].name);
  printf("Birth Date: %s\n", accounts[index].birth);
  printf("Phone Number: %s\n", accounts[index].phoneNum);
  printf("Address: %s\n", accounts[index].address);
  printf("Occupation: %s\n", accounts[index].occupation);
  printf("Current Balance: %lld\n", accounts[index].balance);
  printf("Account Number: %s\n", accounts[index].accNum);
  printf("User ID: %s\n", accounts[index].userID);
  printf("Account Status: %s\n", accounts[index].deleted ? "Deactivated" : "Active");
  printf("\n");
}
//Changing Password
void changePass(account * accounts, int index)
{
  int i;
  char newPassTemp[50];
  char oldPass[50];
  for(i = 2 ; i > -1 ; i--)
  {
  	//have 3 attempts to input old password
    printf("Old Password: ");
    scanf("%s", oldPass);
    if(strcmp(oldPass, (accounts + index)->password) == 0)
    {
      printf("New Password: ");
      scanf("%s", accounts[index].password);
      printf("\n<<Password Changed Successfully>>\n");
      return;
    }
    else
    {
      printf("\n<<Incorrect Old Password. Try Again! (%d attempt(s) left)>>\n", i);
    }
  }
}

void editInfo(account * accounts, int index)
{
	//edit private info for the account
  char temp[50];
  printf("=====Change Account Info=====\n");
  printf("Phone Number : ");
  fgets(temp, 50, stdin);
  if ((strlen(temp) > 0) && (temp[strlen (temp) - 1] == '\n'))
    temp[strlen (temp) - 1] = '\0';
  strcpy(accounts[index].phoneNum, temp);
  printf("Current Address : ");
  fgets(temp, 50, stdin);
  if ((strlen(temp) > 0) && (temp[strlen (temp) - 1] == '\n'))
     temp[strlen (temp) - 1] = '\0';
  strcpy(accounts[index].phoneNum, temp);
  printf("Occupation : ");
  fgets(temp, 50, stdin);
  if ((strlen(temp) > 0) && (temp[strlen (temp) - 1] == '\n'))
    temp[strlen (temp) - 1] = '\0';
  strcpy(accounts[index].occupation, temp);
  printf("\n<<Account Info Changed Successfully>>\n");
  return;
}

bool deactivate(account * accounts, int index, int *inactive)
{
	//deactivating account
  int choice;
  printf("=====ACCOUNT DEACTIVATION=====\n");
  printf("Are you sure?\n");
  printf("(1) Yes\n(2) No\n");
  printf("> ");
  scanf("%d", &choice);
  if(choice == 1)
  {
    accounts[index].deleted = true;
    *inactive += 1;
    printf("\n<<Account has been deactivated>>\n");
    return true;
  }
  else if(choice == 2)
  {
    printf("\n<<Deactivation Canceled>>\n");
    return false;
  }
  return false;
}

void menuTransition()
{
	//For enhanced user-friendliness
  printf("\n\nPress any key to continue...");
  getch();
  clrscr();
}

void clrscr()
{
    system("@cls||clear");
}