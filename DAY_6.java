// import java.util.Scanner;

// public class DAY_6 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);

//         // Array to store ratings for 7 days
//         int[] ratings = new int[7];

//         System.out.println("Enter food ratings for 7 days:");
//         for (int i = 0; i < ratings.length; i++) {
//             ratings[i] = sc.nextInt();
//         }

//         // Assume first rating is maximum initially
//         int max = ratings[0];

//         // Compare each rating to find the highest
//         for (int i = 1; i < ratings.length; i++) {
//             if (ratings[i] > max) {
//                 max = ratings[i];
//             }
//         }

//         System.out.println("Highest food rating = " + max);
//     }
// }
// import java.util.Scanner;

// public class DAY_6 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);

//         // Array to store rainfall data for 7 days
//         int[] rainfall = new int[7];

//         System.out.println("Enter rainfall data for 7 days:");
//         for (int i = 0; i < rainfall.length; i++) {
//             rainfall[i] = sc.nextInt();
//         }

//         // Assume first day's rainfall is minimum initially
//         int min = rainfall[0];

//         // Compare each value to find the least rainfall
//         for (int i = 1; i < rainfall.length; i++) {
//             if (rainfall[i] < min) {
//                 min = rainfall[i];
//             }
//         }

//         System.out.println("Least rainfall = " + min);
//     }
// }
// import java.util.Scanner;

// public class DAY_6 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);

//         // Array to store scores of 10 matches
//         int[] scores = new int[10];

//         System.out.println("Enter scores for 10 matches:");
//         for (int i = 0; i < scores.length; i++) {
//             scores[i] = sc.nextInt();
//         }

//         // Variable to hold the sum of all scores
//         int totalRuns = 0;

//         // Add each score to totalRuns
//         for (int i = 0; i < scores.length; i++) {
//             totalRuns += scores[i];
//         }

//         System.out.println("Total runs scored = " + totalRuns);
//     }
// }
// import java.util.Scanner;

// public class DAY_6 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);

//         // Array to store 5 customer ratings
//         int[] ratings = new int[5];

//         System.out.println("Enter 5 customer ratings:");
//         for (int i = 0; i < ratings.length; i++) {
//             ratings[i] = sc.nextInt();
//         }

//         // Variable to hold the sum of ratings
//         int sum = 0;

//         // Add each rating to sum
//         for (int i = 0; i < ratings.length; i++) {
//             sum += ratings[i];
//         }

//         // Calculate average (sum / number of ratings)
//         double average = (double) sum / ratings.length;

//         System.out.println("Average rating = " + average);
//     }
// }
// import java.util.Scanner;

// public class DAY_6 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);

//         // Array to store 8 sales values
//         int[] sales = new int[8];

//         System.out.println("Enter 8 sales values:");
//         for (int i = 0; i < sales.length; i++) {
//             sales[i] = sc.nextInt();
//         }

//         // Counters for even and odd values
//         int evenCount = 0;
//         int oddCount = 0;

//         // Check each value
//         for (int i = 0; i < sales.length; i++) {
//             if (sales[i] % 2 == 0) {
//                 evenCount++;
//             } else {
//                 oddCount++;
//             }
//         }

//         System.out.println("Count of even values = " + evenCount);
//         System.out.println("Count of odd values = " + oddCount);
//     }
// }
// import java.util.Scanner;

// public class DAY_6 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);

//         // Example: booked seat numbers stored in an array
//         int[] bookedSeats = {101, 102, 105, 110, 115};

//         System.out.print("Enter the seat number you want to check: ");
//         int requestedSeat = sc.nextInt();

//         boolean isBooked = false;

//         // Check if requested seat is already booked
//         for (int i = 0; i < bookedSeats.length; i++) {
//             if (bookedSeats[i] == requestedSeat) {
//                 isBooked = true;
//                 break;
//             }
//         }

//         if (isBooked) {
//             System.out.println("Seat number " + requestedSeat + " is NOT available (already booked).");
//         } else {
//             System.out.println("Seat number " + requestedSeat + " is available.");
//         }
//     }
// }
// import java.util.Scanner;

// public class DAY_6 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);

//         // Example: number of readings (you can change size if needed)
//         int[] temps = new int[7];

//         System.out.println("Enter temperature readings for 7 days:");
//         for (int i = 0; i < temps.length; i++) {
//             temps[i] = sc.nextInt();
//         }

//         // Reverse the array in-place
//         int start = 0;
//         int end = temps.length - 1;
//         while (start < end) {
//             int temp = temps[start];
//             temps[start] = temps[end];
//             temps[end] = temp;
//             start++;
//             end--;
//         }

//         // Print reversed array
//         System.out.println("Temperature readings in reverse order:");
//         for (int i = 0; i < temps.length; i++) {
//             System.out.print(temps[i] + " ");
//         }
//     }
// }
// import java.util.Scanner;

// public class DAY_6 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);

//         // Example: attendance data for 7 students
//         int[] attendance = new int[7];

//         System.out.println("Enter attendance data for 7 students:");
//         for (int i = 0; i < attendance.length; i++) {
//             attendance[i] = sc.nextInt();
//         }

//         // Create backup copy
//         int[] backup = new int[attendance.length];
//         for (int i = 0; i < attendance.length; i++) {
//             backup[i] = attendance[i];
//         }

//         // Print backup array
//         System.out.println("Backup attendance data:");
//         for (int i = 0; i < backup.length; i++) {
//             System.out.print(backup[i] + " ");
//         }
//     }
// }
// import java.util.Scanner;

// public class DAY_6 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);

//         // Example: product IDs sold (you can change size if needed)
//         int[] productIDs = new int[10];

//         System.out.println("Enter 10 product IDs sold:");
//         for (int i = 0; i < productIDs.length; i++) {
//             productIDs[i] = sc.nextInt();
//         }

//         System.out.print("Enter the Product ID to check frequency: ");
//         int targetID = sc.nextInt();

//         // Counter for frequency
//         int count = 0;

//         // Count how many times targetID appears
//         for (int i = 0; i < productIDs.length; i++) {
//             if (productIDs[i] == targetID) {
//                 count++;
//             }
//         }

//         System.out.println("Product ID " + targetID + " appears " + count + " time(s).");
//     }
// }
// import java.util.Scanner;

// public class DAY_6 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);

//         // Example: number of players (you can change size if needed)
//         int[] heights = new int[7];

//         System.out.println("Enter heights of 7 players:");
//         for (int i = 0; i < heights.length; i++) {
//             heights[i] = sc.nextInt();
//         }

//         boolean isSorted = true;

//         // Check if array is sorted in ascending order
//         for (int i = 0; i < heights.length - 1; i++) {
//             if (heights[i] > heights[i + 1]) {
//                 isSorted = false;
//                 break;
//             }
//         }

//         if (isSorted) {
//             System.out.println("The array is sorted in ascending order.");
//         } else {
//             System.out.println("The array is NOT sorted.");
//         }
//     }
// }
// import java.util.Scanner;

// public class DAY_6 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);

//         System.out.print("Enter the student name: ");
//         String name = sc.nextLine();

//         int vowelCount = 0;

//         // Convert to lowercase for easy comparison
//         name = name.toLowerCase();

//         for (int i = 0; i < name.length(); i++) {
//             char ch = name.charAt(i);
//             if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
//                 vowelCount++;
//             }
//         }

//         System.out.println("Number of vowels in the name = " + vowelCount);
//     }
// }
// import java.util.Scanner;

// public class DAY_6 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);

//         System.out.print("Enter the message: ");
//         String message = sc.nextLine();

//         String reversed = "";

//         // Reverse manually using a loop
//         for (int i = message.length() - 1; i >= 0; i--) {
//             reversed += message.charAt(i);
//         }

//         System.out.println("Reversed message = " + reversed);
//     }
// }
// import java.util.Scanner;

// public class DAY_6 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);

//         System.out.print("Enter the book title: ");
//         String title = sc.nextLine();

//         // Convert to uppercase
//         String upperTitle = title.toUpperCase();

//         System.out.println("Book title in uppercase = " + upperTitle);
//     }
// }
// import java.util.Scanner;

// public class DAY_6 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);

//         System.out.print("Enter the username: ");
//         String username = sc.nextLine();

//         // Remove all spaces
//         String cleaned = username.replace(" ", "");

//         System.out.println("Cleaned username = " + cleaned);
//     }
// }
// import java.util.Scanner;

// public class DAY_6 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);

//         System.out.print("Enter a word: ");
//         String word = sc.nextLine();

//         String reversed = "";

//         // Reverse the word manually
//         for (int i = word.length() - 1; i >= 0; i--) {
//             reversed += word.charAt(i);
//         }

//         // Compare original and reversed
//         if (word.equalsIgnoreCase(reversed)) {
//             System.out.println("Palindrome");
//         } else {
//             System.out.println("Not Palindrome");
//         }
//     }
// }