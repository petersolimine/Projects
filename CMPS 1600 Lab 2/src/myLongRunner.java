/**
 * Author: Peter Solimine
 * Class: CMPS 1600
 * Project: Lab 2
 * Date: 09/17/2018
 * Professor: Parisa Kordjamshidi
 * Lab Section: Tuesday 5 P.M.
 * Description: create a data structure that can hold up to 100 digits
 * create 3 methods, add, subtract, and multiply, to use on these data structures.
 */
import java.util.*;
public class myLongRunner {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);

        //get first line of input which will be converted into type myLong
        System.out.println("Enter a number between 1 and 100 digits: ");
        String temp = console.next();
        myLong curLong = new myLong();
        String choice = "";

        //create a menu and loop until user elects to quit
        while (!choice.equals("Q")) {
            curLong.setLong(temp);
            System.out.println("Your number is "+temp+
                    "\nWhat would you like to do? \n" +
                    "A - add to another number\n" +
                    "S - subtract a smaller number from this number\n" +
                    "M - multiply this number by another number\n" +
                    "Q - quit the program");
            choice = console.next();
            if(choice.equals("Q"))
                break;
            while(!choice.equals("A") && !choice.equals("S") && !choice.equals("M")) {
                System.out.println("Invalid selection. Try again: ");
                choice = console.next();
            }
            System.out.println("Enter another number: ");
            temp = console.next();
            myLong num = new myLong();
            num.setLong(temp);

            if(choice.equals("A"))
                curLong.add(num);
            if(choice.equals("S"))
                curLong.subtract(num);
            if(choice.equals("M"))
                curLong.multiply(num);

            temp = curLong.getLong();
        }
        System.out.println("Peace out brotha man");
    }
}
