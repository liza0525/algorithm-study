// 문제 제목 : 숫자 골라내기
import java.io.FileInputStream;
import java.util.Scanner;
import java.util.*;

class SelectNum {
	public static void main(String args[]) throws Exception	{
        // Scanner sc = new Scanner(System.in);
		Scanner sc = new Scanner(new FileInputStream("../input.txt"));
		int T = sc.nextInt();
		for(int test_case = 0; test_case < T; test_case++) {
            int answer = 0;
            int N = sc.nextInt();
            Map<Integer, Integer> numMap = new HashMap<>();
            for (int i = 0; i < N; i++) {
                int num = sc.nextInt();
                if (numMap.containsKey(num) == false) {
                    numMap.put(num, 1);
                } else {
                    numMap.put(num, numMap.get(num) + 1);
                }
            }
            for (int key: numMap.keySet()) {
                if (numMap.get(key) % 2 == 1) {
                    answer ^= key;
                }
            }

			System.out.println("Case #"+(test_case+1));
			System.out.println(answer);
		}
	}
}