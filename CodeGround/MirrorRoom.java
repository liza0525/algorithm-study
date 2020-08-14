// 문제 제목 : 방 속의 거울
import java.util.Scanner;
import java.io.FileInputStream;

class MirrorRoom {
    static int[] dx = {-1, 1, 0, 0}; // 상하좌우
    static int[] dy = {0, 0, -1, 1};
	public static void main(String args[]) throws Exception	{
		
		// Scanner sc = new Scanner(System.in);
		Scanner sc = new Scanner(new FileInputStream("../input.txt"));

		int T = sc.nextInt();
		for(int test_case = 0; test_case < T; test_case++) {
            int answer = 0;
            int N = sc.nextInt();
            int[][] rooms = new int[N][N];
            boolean[][] visited = new boolean[N][N];

            for (int i = 0; i < N ; i++) {
                String line = sc.next();
                for (int j = 0; j < N; j++) {
                    rooms[i][j] = line.charAt(j) - '0'; // char형을 int로 변환
                    visited[i][j] = false;
                }
            }

            // 처음 시작 위치 및 방향
            int x = 0;
            int y = 0; 
            int d = 3; // 항상 왼->오 방향으로 시작

            while (x >= 0 && x < N && y >= 0 && y < N) {
                if (visited[x][y] == false) {
                    visited[x][y] = true;
                    if (rooms[x][y] == 1 || rooms[x][y] == 2) {
                        answer++;
                    }
                }
                if (rooms[x][y] == 1) { // 좌하 방향 거울
                    // 이전 방향이 0: 상, 1: 하, 2: 좌, 3:우 일 때
                    if (d == 0) {
                        d = 3;
                    } else if (d == 1) {
                        d = 2;
                    } else if (d == 2) {
                        d = 1;
                    } else if (d == 3) {
                        d = 0;
                    }
                } else if (rooms[x][y] == 2) { // 우하 방향 거울
                    // 이전 방향이 0: 상, 1: 하, 2: 좌, 3:우 일 때
                    if (d == 0) {
                        d = 2;
                    } else if (d == 1) {
                        d = 3;
                    } else if (d == 2) {
                        d = 0;
                    } else if (d == 3) {
                        d = 1;
                    }

                }
                x += dx[d];
                y += dy[d];
            }

            
			System.out.println("Case #"+(test_case+1));
			System.out.println(answer);
		}
    }
}