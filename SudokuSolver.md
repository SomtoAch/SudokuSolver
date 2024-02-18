Backtracking - Make schoices within the given constraints. If a choice stops our program from any choice later on (ie no number is within constraints), we unwind and change the choice

It is key to note that a valid choice is valid within the set constraints (ie the sudoku rules of no duplicates per row, column or subgrid)

A correct choice is one that doesnt stop us from making a valid choice everywhere else
If we can fill up the board with valid choices, we have solved it.

# Sudoku Thought Process
- Focus on the first choice to be made
- Starting from 1 loop through numbers 1 to 9, check whether number is in subgrid, row, or column. If all those conditions are false choose the number. By iterating in increasing order we make sure to choose the smallest number for which these conditions are false.
- If we finish iterating from 1 to 9 and no number can be chosen (ie there is no valid choice) then go back to the previous choice. repeat step 2 but start iterating from the previous choice. LOOP
<!-- this part could be handled by calling func again when choice made, if NVC return from call to continue iterating through previous options -->
- do this until all choices have been made. our goal is to make all our choices - when there are no more choices to make

-----------------------------------------------------------------------------

# Program completed!

BREAKDOWN

- The program is recursive and has a default input of f=0.
- The program is called when a choice has been made and we want to move onto the next space. It is returned with True when all choices ahead are valid and the board has been completed. 
- Essentially it first points to the first space of the board. If this space is filled it enters an if statement, with the condition being SudokuSolver(f+1) which points to the next space. If this space is empty, we enter loop through 1 --> 9 calling an external validator function to check if each number is a valid choice. 
- Once a valid choice for that space is found, the board is updated. we enter an if clause, with SudokuSolver(f+1) as the condition. If on the next runthrough we loop through 1 to 9 with no valid choice for that space, the program returns false. remember the function was called in an if statement. this means we go through the else clause instead of the if clause. the else clause simply says remove the value assigned to that space and continue the loop. we look for a valid choice greater than the previous choice. if nvc again, we return the false and the previous space needs to be reassigned.
- if when we are unwinding/backtracking we go over a position that didnt need to be updated, we just return the value returned to it. We can discern between filled choices and spaces that were filled to begin with by the way the next function iteration is called - they are called in different areas, and so when we backtrack the returned values can be handled differently

this program took me <8 hours and was a great experience. I didnt understand the backtracking algorithm at first, and ran into quite a few issues when programming the code, but taking some time off and debugging using print statements and tracing helped me finally solve my issues.