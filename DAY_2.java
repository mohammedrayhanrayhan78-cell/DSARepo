//import java.util.Scanner;
//
//public class DAY_2 {
//    public static void main(String[]args){
//        Scanner scan = new Scanner(System.in);
//        System.out.print("Enter your AGE to get a discount on MOVIE TICKETS : ");
//        int Age = scan.nextInt();
//        if (Age < 12) {
//            System.out.println("You get a 50% DISCOUNT on your ticket");
//        } else if (Age > 60) {
//            System.out.println("You get a 30% DISCOUNT on your ticket");
//        } else {
//            System.out.println("You Don't get a discount you have to pay the FULL TICKET");
//        }
//        scan.close();
//    }
//}



import java.util.Scanner;

public class DAY_2 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int accountBalance = 5000;
        System.out.println("Welcome to the ATM!");
        System.out.println("Your current balance: ₹" + accountBalance);
        System.out.print("Enter withdrawal amount: ₹");
        int amount = scan.nextInt();
        if (amount % 100 != 0) {
            System.out.println("Error: Withdrawal amount must be in multiples of ₹100.");
        }
        else if (amount > accountBalance) {
            System.out.println("Error: Insufficient balance.");
        }
        else if (amount > 0) {
            accountBalance -= amount;
            System.out.println("Withdrawal successful! You withdrew ₹" + amount);
            System.out.println("Remaining balance: ₹" + accountBalance);
        }
        else {
            System.out.println("Error: Invalid withdrawal amount.");
        }

        scan.close();
    }
}

