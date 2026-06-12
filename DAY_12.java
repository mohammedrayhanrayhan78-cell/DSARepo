import java.util.Scanner;

public class DAY_12 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter your ROOM TEMP : ");
        int Temp = scan.nextInt();
        if (Temp < 18) {
            System.out.println("The temperature is TOO COLD");
        } else if (Temp > 30) {
            System.out.println("The temperature is TOO HOT");
       } else {
           System.out.println("The temperature is COMFORTABLE");
        }
        scan.close();
   } 
}
