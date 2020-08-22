import java.util.Scanner;
import java.io.FileInputStream;


class swea_9997_minimulism_clock {
	public static void main(String args[]) throws Exception {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new FileInputStream("../input.txt"));

		int T;
		T=sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++) {
            int degree = sc.nextInt();

            int hour = degree / 30;
            int minute = (int)((degree - (hour * 30)) / 0.5);

            System.out.printf("#%d %d %d", test_case, hour, minute);
            System.out.println();
		}
	}
}