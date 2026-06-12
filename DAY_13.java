import java.util.Scanner;

public class DAY_13 {
   public static void main(String[] args) {
       Scanner scan = new Scanner(System.in);
       System.out.print("Enter your MARKS : ");
       int Marks = scan.nextInt();
       if (Marks>=35&&Marks<=100) {
           System.out.println("You have successfully PASSED");
       } else if (Marks<35&&Marks>0) {
           System.out.println("You have FAILED try again");
       } else if(Marks<=0||Marks>100){
           System.out.println("INVALID CHOICE!");
       }
       scan.close();
   }
}