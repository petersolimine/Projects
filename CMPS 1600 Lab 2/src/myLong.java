/**
 * Author: Peter Solimine
 * Class: CMPS 1600
 * Project: Lab 2
 * Date: 09/17/2018
 * Professor: Parisa Kordjamshidi
 * Lab Section: Tuesday 5 P.M.
 * Description: create a data structure that can hold up to 100 digits
 * create 5 methods: getLong, setLong, add, subtract, & multiply.
 */
public class myLong {
    private int[] number;
    public int maxIndex = 99;


    public myLong() {
        this.number = new int[maxIndex+1];
    }

    public void setLong(String input) {
        /**
         * parameters: input - String
         * takes a string as input and converts it to type myLong
         * sets this.number == input    (in the form of an array)
         * no return value
         */
        int len = input.length();
        int addStart = (maxIndex+1) - len;
        int digit;
        int counter = 0;
        for (int i = addStart; i < maxIndex+1; i++) {
            digit = Integer.parseInt(String.valueOf((input.charAt(counter))));
            this.number[i] = digit;
            counter++;
        }
    }

    public String getLong() {
        /**
         * no parameters
         * convert a myLong to a string for printing purposes
         * return: String
         */
        int zeros = countZeros(this);

        String val = "";
        for (int i = zeros; i < maxIndex+1; i++) {
            val = val + Integer.toString((this.number[i]));
        }
        return val;
    }

    public void add(myLong valToAdd) {
        /**
         * input: myLong
         * adds two myLong.number values
         * updates this.number to equal this.number+valToAdd.number
         * no return value
         */
        int carry = 0;
        int placement, added;
        for (int i = maxIndex; i > 0; i--) {
            added = this.number[i] + valToAdd.number[i] + carry;
            if (added > 9) {
                placement = added % 10;
                carry = added / 10;
            } else {
                placement = added;
                carry = 0;
            }
            this.number[i] = placement;
        }
    }

    public void subtract(myLong valToSub) {
        /**
         * input: myLong
         * subtracts valToSub.number from this.number
         * updates this.number to equal difference
         * no return value
         */
        int sub, num1, num2;
        for (int i = maxIndex; i > 0; i--) {
            num1 = this.number[i];
            num2 = valToSub.number[i];
            sub = num1-num2;
            if (sub < 0) {
                sub = (10 + num1) - num2;
                this.number[i - 1] -= 1;
            }
            this.number[i] = sub;
        }
    }

    public void multiply(myLong other){
        /**
         * input: myLong
         * multiplies two myLong.number values
         * updates this.number to equal this.number*valToAdd.number
         * no return value
         */
        int[][] matrix = new int[maxIndex+1][maxIndex+1]; //new 2d array of size (maxIndex+1)^2
        int zeros1 = countZeros(this); //This provides the # of zeros before the number actually begins
        int zeros2 = countZeros(other);

        int counter1 = maxIndex-zeros1; // maxIndex minus this above number provides the length of the number
        int counter2 = maxIndex-zeros2;
        System.out.println(zeros1+" "+zeros2);
        System.out.println(counter1+" "+counter2);
        int start1 = maxIndex-counter1;
        int start2 = maxIndex-counter2;

        for(int i = start1; i<=maxIndex; i++){
            for(int j = start2; j<=maxIndex; j++){
                if((this.number[i] * other.number[j]) > 9) {
                    matrix[i][(maxIndex-1) - (counter1+counter2)] += (this.number[i] * other.number[j])/10;
                }
                matrix[i][(maxIndex) - (counter1+counter2)] += (this.number[i] * other.number[j])%10;
                System.out.println("frst = "+(this.number[i] * other.number[j])%10);
                counter2--;
            }
            counter2 = maxIndex-zeros2;
            counter1--;
        }

        //Make all 2 digit numbers back into 1 digit numbers;
        myLong ans = new myLong();
        myLong matrixColumnAdd = new myLong();

        //go one by one through the rows of the matrix adding downward into
        for(int col = 0; col<=maxIndex; col++){
            matrixColumnAdd.number = matrix[col];
            ans.add(matrixColumnAdd);
        }
        this.number = ans.number;
    }
    private int countZeros(myLong x) {
        /**
         * input: myLong
         * finds the true length of a myLong.number by counting the number of leading zeros
         * returns int //number of 0's before actual number begins (max 100 -> if myLong.number = 0)
         */
        int countZeros = 0; //serves as a counter for the number of zeroes to remove and also as an incrementer
        int digit = x.number[0]; //first digit
        while (digit == 0 && countZeros < maxIndex) {
            countZeros++;
            digit = x.number[countZeros];
        }
        return countZeros;
    }
}
