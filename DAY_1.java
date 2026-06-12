import java.util.Scanner;

public class DAY_1 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the number you want to know +ve or -ve: ");
        int x = scan.nextInt();
        if(x>0){
            System.out.println("The number is POSITIVE");
        }
        else if(x<0){
            System.out.println("The number is NEGATIVE");
        }
        else{
            System.out.println("The number is ZERO");
        }
        scan.close();
    }
}