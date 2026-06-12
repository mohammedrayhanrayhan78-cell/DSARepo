import java.util.Scanner;

public class DAY_10 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter two number to find out largest amongst them : ");
        int x = scan.nextInt();
        int y = scan.nextInt();
        if(x>y){
            System.out.println("X is greatest");
        }
        else if(x<y){
            System.out.println("Y is greatest");
        }
        else if(x==y){
            System.out.println("X and Y are equal");
        }
        else{
            System.out.println("NOT a VALID number");
        }
        scan.close();
    }
}