import java.io.FileInputStream;
import java.util.Scanner;

class ArithmeticSequence {
    public static void main(String[] args) throws Exception {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new FileInputStream("../input.txt"));
        
        int T = sc.nextInt();

        for (int test_case = 0; test_case < T; test_case++) {
            int answer = 0;
            int N = sc.nextInt();
            long[] numbers = new long[N];

            for (int i = 0; i < N; i++) {
                numbers[i] = sc.nextLong();
            }


            long minDiff = 987654321; 
            for (int i = 0; i < N - 1; i++) {
                long tempDiff = numbers[i+1] - numbers[i];
                if (tempDiff < minDiff) {
                    minDiff = tempDiff;
                }
            }

            boolean flag = false;
            for (int d = 1; d <= Math.sqrt(minDiff); d++) {
                if (minDiff % d == 0) {
                    answer += 1;
                    if (d == Math.sqrt(minDiff)) flag = true;
                }
            }

            if (flag) answer = 2 * answer - 1;
            else answer *= 2;
            if (answer == 0) answer = 1; 


            System.out.println("Case #" + (test_case+1) + "\n" + answer);
        }

    }

}