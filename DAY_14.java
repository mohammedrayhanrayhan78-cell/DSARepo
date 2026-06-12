import java.util.Scanner;

public class DAY_14 {
   public static void main(String[] args) {
       Scanner scan = new Scanner(System.in);
       System.out.println("----- MENU -----");
       System.out.println("1. Pizza");
       System.out.println("2. Burger");
       System.out.println("3. Sandwich");
       System.out.println("4. Pasta");
       System.out.println("5. Salad");
       System.out.print("Enter your menu number: ");
       int choice = scan.nextInt();
       switch (choice) {
           case 1:
               System.out.println("You selected Pizza ");
               break;
           case 2:
               System.out.println("You selected Burger ");
               break;
           case 3:
               System.out.println("You selected Sandwich ");
               break;
           case 4:
               System.out.println("You selected Pasta ");
               break;
           case 5:
               System.out.println("You selected Salad ");
               break;
           default:
               System.out.println("Invalid choice! Please enter a number between 1 and 5.");
       }
       scan.close();
   }
}