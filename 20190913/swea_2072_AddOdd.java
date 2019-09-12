import java.util.Scanner;

class swea_2072_AddOdd {
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args){
        int T = sc.nextInt();
        for (int tc=1; tc<=T; tc++){
            int sum = 0;
            for (int i=0; i<10; i++){
                int n = sc.nextInt();
                if (n%2 == 1) sum += n;
            }
        System.out.printf("#%d %d", tc, sum);
        }
    }
}