import java.io.FileInputStream;
import java.util.Scanner;
import java.math.BigInteger;

class ThreeTimesOne {
    public static void main(String[] args) throws Exception {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new FileInputStream("../input.txt"));

        int T = sc.nextInt();
        for (int testCase = 0; testCase < T; testCase++) {
            int N = sc.nextInt();
            BigInteger maxAns = new BigInteger("1");
            for (int i = 0; i < N; i++) {
                maxAns = maxAns.multiply(BigInteger.valueOf(2));
            }

            long minAns = 1;
            while (true)  {
                if (getCount(minAns) == N) break;
                else minAns++;
            }
            
            System.out.println("Case #" + (testCase+1));
            System.out.println(minAns + " " + maxAns);
        }
    }

    public static int getCount(long number) {
        int res = 0;

        while (number != 1) {
            if (number % 2 == 0) number /= 2;
            else number = number * 3 + 1;
            res++;
        }


        return res;
    }
}