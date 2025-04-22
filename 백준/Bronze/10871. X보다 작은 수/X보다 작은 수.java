import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n,x;
        n = scan.nextInt();
        x = scan.nextInt();
        
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextInt();
        }
        
        int[] res = new int[10000];
        int idx = 0;
        for (int num:arr) {
            if (num < x) {
                res[idx++] = num;
            }
        }
        
        for (int i = 0; i < idx; i++) {
            System.out.print(res[i] + (i==idx-1?" ":"\n"));
        }
    }
}