import java.util.Scanner;

public class DAY_11 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a number to identify whether it is ODD or EVEN : ");
        int x = scan.nextInt();
        if(x%2==0){
            System.out.println("The following number is EVEN");
        }
        else{
            System.out.println("The following number is ODD");
        }
        scan.close();
    }
}
