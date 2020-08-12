// 문제 제목 : 프로그래밍 경진대회
import java.io.FileInputStream;
import java.util.Arrays;
import java.util.Scanner;

class ProgrammingComp {
    public static void main(String[] args) throws Exception {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new FileInputStream("../input.txt"));

        int T = sc.nextInt();

        for (int testCase = 0; testCase < T; testCase++) {
            int answer = 0;
            int N = sc.nextInt();
            int[] nowScore = new int[N];
            int[] finalRoundMaxScore = new int[N];

            for (int i = 0; i < N; i++) {
                nowScore[i] = sc.nextInt();
            }

            Arrays.sort(nowScore);

            for (int i = 0; i < N; i++) {
                finalRoundMaxScore[i] = nowScore[N-1-i] + (i+1);
            }

            Arrays.sort(finalRoundMaxScore);

            for (int i = 0; i < N ; i++) {
                if (nowScore[i] + N >= finalRoundMaxScore[N-1]) {
                    answer++;
                }
            }
            
			System.out.println("Case #"+(testCase+1));
			System.out.println(answer);
        }

    }
}