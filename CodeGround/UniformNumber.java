// 문제 제목 : 균일수
import java.io.FileInputStream;
import java.util.Scanner;

class UniformNumber {
    static int Answer;

    public static void main(String args[]) throws Exception {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new FileInputStream("../input.txt"));

        int T = sc.nextInt();
        for (int test_case = 0; test_case < T; test_case++) {
            int answer = 1000000000; // 제수는 2부터 시작
            int number = sc.nextInt();

            if (number <= 2)
                answer = number + 1;
            else {
                for (int i = 2; i * i <= number; i++) {
                    boolean flag = true;
                    int dividend = number; // 피제수
                    int remainder = dividend % i;
                    while (dividend > 0) {
                        if (dividend % i != remainder) {
                            flag = false;
                            break;
                        } else {
                            dividend /= i;
                        }
                    }
                    if (flag) {
                        answer = answer > i ? i : answer;
                    }

                    if (number % i != 0)
                        continue;
                    int temp = number / i - 1;
                    if (temp > i) {
                        answer = answer > temp ? temp : answer;
                    }
                }
                if (answer == 1000000000)
                    answer = number - 1;
            }

            System.out.println("Case #" + (test_case + 1));
            System.out.println(answer);
        }
    }
}