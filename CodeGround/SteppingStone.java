import java.io.FileInputStream;
import java.util.Scanner;

class SteppingStone {
    static int MOD = 1000000009;
    public static void main(String[] args) throws Exception {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new FileInputStream("../input.txt"));

        int T = sc.nextInt();
        for (int testCase = 0; testCase < T; testCase++) {
            int N = sc.nextInt();
            int K = sc.nextInt();
            int L = sc.nextInt();
            boolean[] bomb = new boolean[N+1];
            int[][] dp = new int[N+1][K+1]; // i번째 돌에 k번째 칸만큼으로 뛰어 오는 경우
            int [] totalNum = new int[N+1];


            // 폭탄이 있는 경우
            for (int i = 1; i < L + 1; i++) {
                int num = sc.nextInt();
                bomb[num] = true;
            }

            if (!bomb[1]) {
                dp[1][1] = 1;
                totalNum[1] = 1;
            }


            for (int i = 2; i < N+1; i++) {
                if (bomb[i]) continue;
                for (int k = 1; k < K+1; k++) {
                    if (i < k) continue;
                    else if (i == k) dp[i][k] = 1;
                    else {
                        dp[i][k] = (totalNum[i-k] + MOD - dp[i-k][k]) % MOD;
                    }
                    totalNum[i] = (totalNum[i] + dp[i][k]) % MOD;
                }
            }

            System.out.println("Case #" + (testCase+1) + "\n" + totalNum[N] % MOD);
        }
    }
}