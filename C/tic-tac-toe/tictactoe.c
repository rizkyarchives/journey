
/*			TIC TAC TOE
			Disadvantages: Cannot be played more than once...
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <conio.h>

void clrscr();
void drawBoard();
int markBoard(int, int);
bool checkForWin();

char board[9] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};

int main()
{
	int i, input, validTest;//validTest is to to store the return value of markBoard
	bool win = false; //false by default
	drawBoard();
	for(i = 1 ; i <= 9 ; i++)//goes 9 times, because they can only be a total of 9 moves
	{
		if(i % 2 != 0)
		{
			printf("Player 1, enter a number: ");
			scanf("%d", &input);
		}
		else
		{
			printf("Player 2, enter a number: ");
			scanf("%d", &input);
		}
		validTest = markBoard(i, input);
		drawBoard();
		if(validTest == 0)//means invalid input, i-- is used so that it restart the current iteration
		{
			i--;
			continue;
		}
		win = checkForWin();
		if(win == true && i % 2 != 0)
		{
			printf("Player 1 wins\n");
			break;
		}
		else if(win == true && i % 2 == 0)
		{
			printf("Player 2 wins\n");
			break;
		}
	}
	if(win == false)
		printf("Draw!\n");//kalo ga menang yaa seri brarti yah
	return 0;
}

void clrscr()//to clear the screen, also why I need to include stdlib (from StackOverflow)
{
    system("@cls||clear");
}

void drawBoard()//To draw the board
{
	int i;
	clrscr();
	printf("\t    Tic Tac Toe\n\nPlayer 1 (X)\t-\tPlayer 2 (O)\n");
	for(i = 0 ; i <= 6 ; i += 3)
	{
		printf("\n   |   |   \n");
		printf(" %c | %c | %c \n", board[i], board[i + 1], board[i + 2]);
		printf("___|___|___");
	}
	for(i = 11 ; i > 0 ; i--)//because the third printf in the above for loop will create an invalid tictactoe board, I opted to just delete it (cont)
	{
		printf("\b");
	}
	printf("   |   |   \n\n");//and rewrite it with this so that it looks like an actual tictactoe board. Neat!
}

int markBoard(int player, int input)//Change the array according to player input, no error = 1, error = 0
{
	int result;
	if(board[input - 1] == 'X' || board[input - 1] == 'O' || input > 9 || input < 1)//error test, if it's already X or O then it is an error, if it isn't between 1 to 9 it is an error
	{
		printf("Invalid input...\nPress any key to retry...");
		result = 0;
		getch();//from conio.h, the press any key to retry functionality will work because of this function.
	}
	else//no error? then assign it
	{
		if(player % 2 != 0)
			board[input - 1] = 'X';
		else if(player % 2 == 0)
			board[input -1] = 'O';
		result = 1;
	}
	return result;//returned a result, because if there was an error, then the player can retry (see main function line 35 to see when this will be used)
}

bool checkForWin()//determine if a player wins or not. basically checking if there is a row or column or diagonal with all the same char
{
	int i1, i2;
	bool result = false;
	for(i1 = 0, i2 = 0 ; i1 <= 6 || i2 <= 2 ; i1 += 3, i2++)//make it simpler for checking each row or column with for loop
	{
		if(board[i1] == board[i1+1] && board[i1+1] == board[i1+2] && board[i1] == board[i1+2])
		{
			result = true;
			break;
		}
		else if(board[i2] == board[i2+3] && board[i2+3] == board[i2+6] && board[i2] == board[i2+6])
		{
			result = true;
			break;
		}
	}
	if(board[0] == board[4] && board[4] == board[8] && board[0] == board[8])//need to hard code this
		result = true;
	else if(board[2] == board[4] && board[4] == board[6] && board[2] == board[6])//this one as well needed hard code
		result = true;
	return result;//if any of the if function is true, will return value true, otherwise, will return value false
}