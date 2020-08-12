import java.io.FileInputStream;
import java.util.Scanner;

class JumpingFrog {
    public static void main(String[] args) throws Exception {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new FileInputStream("../input.txt"));
        int T = sc.nextInt();
        for (int testCase = 0; testCase < T; testCase++) {
            int answer = 0;
            int N = sc.nextInt();
            int[] stone = new int[N+1];
            stone[0] = 0;
            for (int i = 1; i < N+1; i++) {
                stone[i] = sc.nextInt();
            }
            
            int jump = sc.nextInt();

            int nowIdx = 0;
            for (int nextIdx = 1; nextIdx < stone.length ; nextIdx++) {
                if (stone[nextIdx] - stone[nextIdx-1] > jump) {
                    answer = -1;
                    break;
                } else {
                    if (stone[nextIdx] - stone[nowIdx] > jump) {
                        nowIdx = --nextIdx;
                        answer++;
                    } else if (stone[nextIdx] - stone[nowIdx] == jump) {
                        nowIdx = nextIdx;
                        answer++;
                    } else if (nextIdx == N) {
                        answer++;
                    }
                }
            }
            System.out.println("Case #"+(testCase+1));
            System.out.println(answer);
        }

    }
}