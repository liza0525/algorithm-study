// SWEA 6900 주혁이의 복권 당첨
import java.io.FileInputStream;
import java.util.Scanner;
import java.util.Set;
import java.util.HashMap;
import java.util.Iterator;

class swea_6900_winner_of_lotto {
    public static void main(String[] args) throws Exception {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new FileInputStream("../input.txt"));

        int T = sc.nextInt();
        for (int testCase = 0; testCase < T; testCase++) {
            int answer = 0;
            int N = sc.nextInt();
            int M = sc.nextInt();
            HashMap<String, Integer> info = new HashMap<>();

            for (int i = 0; i < N; i++) {
                String a = sc.next();
                int b = sc.nextInt();
                info.put(a, b);
            }

            for (int i = 0; i < M; i++) {
                String lotto = sc.next();
                Set keySet = info.keySet();
                Iterator iter = keySet.iterator();
                while(iter.hasNext()) {
                    boolean flag = true;
                    String infoKey = (String)iter.next();
                    for (int j = 0; j < 8; j++) {
                        char ch1 = infoKey.charAt(j);
                        char ch2 = lotto.charAt(j);
                        if (ch1 == '*') {
                            continue;
                        } else if (ch1 != ch2) {
                            flag = false;
                            break;
                        }
                    }

                    if (flag) {
                        answer += info.get(infoKey);
                    }
                }
            }

            System.out.printf("#%d %d", testCase+1, answer);
            System.out.println();
        }
    }
}