**Esteban Quintana**<br>
**Javier Rodríguez**

### Lab 3
### (Un)Informed Search


  *  Which heuristics did you use for the A* algorithm?
      <br>  It compares all the values of the states with the goal state. It adds one to te heuristic for each stack that differs.

```
  example:
      Goal state: [ [B], [A], [C] ]
      State [[A], [C], [B]]

      herustic_value = 0
      for index, element in state:
        if (element == X): cotinue
        else if (element != goal_state[index]): herustic_value++
      return herustic_value

      In this case the result is 3          
      ```
  * Test your program with a couple of different problems. Increase the size of the problem to test the limits of your program. Make a table comparing how many nodes are searched to find the answer for each problem. For this table, you should compare a number of different problems (at least 3) to avoid a statistical bias. Which of the three algorithms (UCS, A with consistent and and A with an inconsistent heuristic) searches the least nodes and * which one take the most?
  * Why does this happen?
  * Which algorithms are optimal? Why?
  *  In your opinion, what are the benefits of simpler algorithms versus more complex ones?
