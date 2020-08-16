
// 문제 제목 : 마라톤 경로
import java.io.FileInputStream;
import java.util.Scanner;

public class MarathonRoute {
    final static int INF = 100000000;

    public static void main(String[] args) throws Exception {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new FileInputStream("../input.txt"));

        int T = sc.nextInt();
        for (int test_case = 0; test_case < T; test_case++) {
            int answer = INF;
            int M = sc.nextInt();
            int N = sc.nextInt();
            int K = sc.nextInt();
            int[][] ground = new int[N + 1][M + 1];
            boolean[][] isWater = new boolean[N + 1][M + 1];
            int[][][] dp = new int[N + 1][M + 1][11]; // i행 j열 k개 물통

            for (int i = 0; i <= N; i++) {
                for (int j = 0; j <= M; j++) {
                    int altitude = sc.nextInt();
                    if (altitude < 0) {
                        isWater[i][j] = true;
                    } else {
                        isWater[i][j] = false;
                    }
                    ground[i][j] = Math.abs(altitude);
                }
            }

            // dp 초기화
            for (int i = 0; i <= N; i++) {
                for (int j = 0; j <= M; j++) {
                    for (int k = 0; k <= 10; k++) {
                        dp[i][j][k] = INF;
                    }
                }
            }

            dp[0][0][0] = 0;

            // 0번 행 초기화
            int bottle = 0;
            for (int j = 1; j <= M; j++) {
                int preBottle = bottle;
                if (isWater[0][j] == true && bottle < 10) {
                    bottle++;
                }
                dp[0][j][bottle] = dp[0][j - 1][preBottle] + Math.abs(ground[0][j - 1] - ground[0][j]);
            }

            // 0번 열 초기화
            bottle = 0;
            for (int i = 1; i <= N; i++) {
                int preBottle = bottle;
                if (isWater[i][0] == true && bottle < 10) {
                    bottle++;
                }
                dp[i][0][bottle] = dp[i - 1][0][preBottle] + Math.abs(ground[i - 1][0] - ground[i][0]);
            }

            for (int i = 1; i <= N; i++) {
                for (int j = 1; j <= M; j++) {
                    for (int k = 0; k <= 10; k++) {
                        if (dp[i - 1][j][k] == INF && dp[i][j - 1][k] == INF)
                            continue;
                        int temp1 = dp[i - 1][j][k] + Math.abs(ground[i - 1][j] - ground[i][j]);
                        int temp2 = dp[i][j - 1][k] + Math.abs(ground[i][j - 1] - ground[i][j]);
                        int temp_res = Math.min(temp1, temp2);
                        if (isWater[i][j] == true && k != 10) {
                            dp[i][j][k+1] = temp_res;
                        } else if (k == 10) {
                            dp[i][j][k] = Math.min(dp[i][j][k], temp_res);
                        } else {
                            dp[i][j][k] = temp_res;
                        }

                    }
                }
            }

            for (int k = K; k <= 10; k++) {
                answer = Math.min(answer, Math.abs(dp[N][M][k]));
            }

            System.out.println("Case #" + (test_case + 1));
            System.out.println(answer);
        }
    }
}