// 문제 제목 : MT게임
import java.io.FileInputStream;
import java.util.Scanner;

class MTGame {
    public static void main(String[] args) throws Exception {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new FileInputStream("../input.txt"));

        int T = sc.nextInt();
        
        for (int testCase = 0; testCase < T; testCase++) {
            int a = sc.nextInt(); // A학과 학생 수
            int b = sc.nextInt(); // B학과 학생 수
            int c = sc.nextInt(); // 게임 반복 횟수
            String answer = "";

            for (int game = 0; game < c; game++) {
                int N = sc.nextInt();
                int K = sc.nextInt();
                boolean isAWin = false;
                for (int finalNum = N - b ; finalNum < N; finalNum++) { // A팀 마지막 선수의 마지막 수
                    int firstNum = finalNum % (b * K + a); // A팀 마지막 선수의 첫 수
                    if (firstNum > ((a - 1) * K) && firstNum <= a*K) {
                        isAWin = true;
                        break;
                    }
                }
                if (isAWin) answer += "a";
                else answer += "b";
            }

            System.out.println("Case #" + (testCase+1) + "\n" + answer);
        }
    }
}