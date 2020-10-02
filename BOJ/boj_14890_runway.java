import java.util.Scanner;
import java.io.FileInputStream;

public class boj_14890_runway {
    static int N;
    static int L;
    static int[][] ground;
    static int[][] rotateGround;
    static boolean[][] isSlope;
    static int totalRoadNum;
    public static void main(String[] args) throws Exception {
        // Scanner sc = new Scanner(System.in);
        Scanner sc = new Scanner(new FileInputStream("../input.txt"));
        N = sc.nextInt();
        L = sc.nextInt();
        ground = new int[100][100];
        rotateGround = new int[100][100];
        isSlope = new boolean[100][100];
        totalRoadNum = 0;

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                ground[r][c] = sc.nextInt();
                rotateGround[c][r] = ground[r][c];
                isSlope[r][c] = false;
            }
        }
        totalRoadNum += findRoad(ground);
        initiateSlope();
        totalRoadNum += findRoad(rotateGround);

        System.out.println(totalRoadNum);
    }

    public static boolean isField(int r, int c) {
        boolean flag = false;
        if (r >= 0 && r < N && c >= 0 && c < N) {
            flag = true;
        }
        return flag;
    }
    
    public static int findRoad(int[][] ground) {
        int roadNum = 0;
        
        for (int r = 0; r < N; r++) {
            boolean isRoad = true;
            for (int c = 0; c < N-1; c++) {
                int nowRoad = ground[r][c];
                int nextRoad = ground[r][c+1];

                if (nextRoad == nowRoad) {
                    continue;
                } else if (nextRoad == nowRoad - 1) {
                    for (int l = 1; l < L+1; l++) {
                        if (!isField(r, c+l)) {
                            isRoad = false;
                            break;
                        }
                        if (ground[r][c+l] != nextRoad) {
                            isRoad = false;
                            break;
                        }
                        isSlope[r][c+l] = true;
                    }
                } else if (nextRoad == nowRoad + 1) {
                    for (int l = 0; l < L; l++) {
                        if (!isField(r, c-l)) {
                            isRoad = false;
                            break;
                        }
                        if (ground[r][c-l] != nowRoad) {
                            isRoad = false;
                            break;
                        }
                        if (isSlope[r][c-l]) {
                            isRoad = false;
                            break;
                        }
                        isSlope[r][c-l] = true;
                    }
                } else {
                    isRoad = false;
                    break;
                }
            }
            if (isRoad) {
                roadNum++;
            }
        }
        return roadNum;
    }

    public static void initiateSlope() {
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                isSlope[r][c] = false;
            }
        }
    }
}