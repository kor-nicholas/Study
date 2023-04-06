import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;

public class Fundamentals {
    public static void Theory() {
        // class System, object out, method println();
        // \t - Tab
        // sout + Enter - snippet to quick write
        System.out.println("\tHello \\ \"and welcome!");
        // [output]: 	Hello \ "and welcome!

        // -----------------------------------------------------------------
        // Comments: // or /* text */

        // -----------------------------------------------------------------
        // Variables:
        int age = 20;
        int age2; age2 = 20;
        age2 = 25;

        byte a; // -128 : 127 (1 byte)
        short b; // -32768 : 32767 (2 bytes)
        int c; // -2147483648 : 2147483647 (4 bytes)
        long d; // -9223372036854775808 : 9223372036854775807 (8 bytes)

        float e = 4.5f; // -3.4*10^38 : 3.4*10^38 (4 bytes)
        double f = 4.3; // ±4.9*10^-324 : ±1.7976931348623157*10^308 (8 bytes)

        char ch = 't';
        String str = "text";

        boolean isHappy = true; // or false

        System.out.println(str + " " + age2 + isHappy);
        // [output]: text 25true

        // -----------------------------------------------------------------
        // Get data from user + operations:

        // import java.util.Scanner
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = scan.nextLine();
        name = scan.nextLine(); // to delete hidden char from Java

        System.out.print("Enter your age: ");
        int age3 = scan.nextInt();

        System.out.println("Name: " + name + "\nAge: " + age3);

        // % - 50 / 33 = 1.51.. ; 33 * 1 = 33 ; 50 - 33 = 17(result)

        // -----------------------------------------------------------------
        // If-else:

        // ||(or), &&(and)
        if(str.equals("Text")) {
            System.out.println("Test if true");
        } else if(false) {
            System.out.println("Test if false");
        } else
            System.out.println("Test if");
        // [output]: Test if

        // break - to exit from switch-case
        // if break hasn't - next case like True
        switch(ch) {
            case 'w':
                System.out.println('w');
                break;
            case 't':
                System.out.println("You are winner");
            case 'q':
                System.out.println("Quit");
                break;
            case 'b':
                System.out.println("Bank");
                break;
            default:
                System.out.println("Error");
        }
        // [output]: You are winner\nQuit

        // -----------------------------------------------------------------
        // Loops:

        // break - exit from loop
        // continue - start next iteration
        for(int i = 0; i < 10; i++) {
            System.out.println(i);
        }

        int j = 0;
        while(j < 10) {
            System.out.println(j);
            j++;
        }

        do {
            j++;
            System.out.println(j);
        } while(j < 20);

        // -----------------------------------------------------------------
        // Arrays:

        int[] arr = new int[5];
        float[] arr2 = new float[] {1.6f, 2.8f, 9.4f};
        char[][] arr3 = new char[3][10];
        char[][] arr4 = new char[][] {
                {'H', 'e', 'l'},
                {'l', 'o', ' '},
                {'W', 'o', 'r'},
                {'l', 'd', '!'}
        };
        char[][][] arr5 = new char[2][3][5];

        for (int i = 0; i < arr2.length; i++) {
            System.out.println(arr2[i]);
        }

        // -----------------------------------------------------------------
        // Collections:
        // easier work, but need more memory

        // int -> Integer
        // float -> Float
        // byte -> Byte
        // ,,,
        ArrayList<Byte> nums = new ArrayList<>();
        nums.add((byte) 1);

        ArrayList<Integer> nums2 = new ArrayList<>();
        nums2.add(3);
        nums2.add(0, 8); // index, value
        nums2.size(); // length
        nums2.get(0); // index 0
        nums2.remove(0); // delete index 0
        nums2.clear(); // delete all elements

        nums2.add(13);
        nums2.add(100);

        for(Integer i : nums2) {
            System.out.println(i);
        }
        // [output]: 13
        // [output]: 100

        // like ArrayList, but add and delete elements faster
        LinkedList<Float> nums3 = new LinkedList<>();

        // -----------------------------------------------------------------
        // Functions(Methods):

        info("Dear Notebook, I can't say you my problems...");
        // [output]: Method info:\nDear Notebook, I can't say you my problems...

        info(String.valueOf(sum(3, 12)));
        // [output]: Method info:\n15

        byte[] nums1 = new byte[] {24, 76};
        info(String.valueOf(sumArray(nums1)));
        // [output]: Method info:\n100
    }

    public static void info(String letter) {
        System.out.println("Method info:\n" + letter);
    }

    public static int sum(int a, int b) {
        return a + b;
    }

    public static int sumArray(byte[] arr) {
        int summa = 0;
        for (int i = 0; i < arr.length; i++) {
            summa += arr[i];
        }
        return summa;
    }
}
