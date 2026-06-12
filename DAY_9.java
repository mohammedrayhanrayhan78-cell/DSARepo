import java.util.Scanner;


public class DAY_9 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter your AGE: ");
        int Age = scan.nextInt();
        if(Age>=18){
            System.out.println("You are MAJOR and you can now VOTE");
        }
        else if(Age<18&&Age>0){
            System.out.println("You are still a CHILD come back later when you grow up ");
        }
        else{
            System.out.println("NOT a VALID age");
        }
        scan.close();
    }
}