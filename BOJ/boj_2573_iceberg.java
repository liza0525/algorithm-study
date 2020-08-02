import java.util.*;
import java.io.*;

class Area {
    int i;
    int j;
    int cntZero;

    Area(int i, int j) {
        this.i = i;
        this.j = j;
    }

    Area(int i, int j, int cntZero) {
        this.i = i;
        this.j = j;
        this.cntZero = cntZero;
    }
}

public class boj_2573_iceberg {
    static int row;
    static int column;
    static int year;
    static int[][] ground;
    static boolean[][] visited;
    static int[] di = {-1, 1, 0, 0};
    static int[] dj = {0, 0, -1, 1};
    public static void main(String[] args) throws IOException {
        // String txtPath = "../input.txt";
        // BufferedReader br = new BufferedReader(new FileReader(txtPath));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] index = br.readLine().split(" ");
        row = Integer.parseInt(index[0]);
        column = Integer.parseInt(index[1]);
        ground = new int[row][column];
        visited = new boolean[row][column];
        year = 0;

        for (int i = 0; i < row; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = 0 ; j < column; j++) {
                ground[i][j] = Integer.parseInt(line[j]);
            }
        }

        while (true) {
            int islandNum = 0;
            resetVistied();
            melting();
            year += 1;            
            for (int i = 0 ; i < row ; i++) {
                for (int j = 0 ; j < column; j++) {
                    if (ground[i][j] != 0 && visited[i][j] == false) {
                        dfs(i, j);
                        islandNum += 1;
                    }
                }
            }
            if (islandNum > 1) {
                break;
            } else if (islandNum == 0) {
                year = 0;
                break;
            }
        }
        System.out.println(year);
        br.close();
    }

    public static boolean isField(int i, int j) {
        boolean res = false;
        if (i >= 0 && i < row && j >= 0 && j < column) {
            res = true;
        }
        return res;
    }

    public static void dfs(int i, int j) {
        Stack<Area> stack = new Stack<>();
        stack.add(new Area(i, j));

        while (!stack.isEmpty()) {
            Area area = stack.pop();
            int si = area.i;
            int sj = area.j;
            for (int k = 0; k < 4; k++) {
                int ni = si + di[k];
                int nj = sj + dj[k];
                if (!isField(ni, nj)) {
                    continue;
                }
                if (ground[ni][nj] != 0 && visited[ni][nj] == false) {
                    stack.add(new Area(ni, nj));
                    visited[ni][nj] = true;
                }
            }
        }
    }

    public static void resetVistied() {
        for (int i = 0 ; i < row ; i++) {
            for (int j = 0 ; j < column; j++) {
                visited[i][j] = false;
            }
        }
    }

    public static void melting() {
        ArrayList<Area> info = new ArrayList<>();
        for (int i = 0 ; i < row ; i++) {
            for (int j = 0 ; j < column; j++) {
                int cntZero = 0;
                if (ground[i][j] == 0) {
                    continue;
                }
                for (int k = 0; k < 4; k++) {
                    int ni = i + di[k];
                    int nj = j + dj[k];
                    if (!isField(ni, nj)) {
                        continue;
                    }
                    if (ground[ni][nj] == 0) {
                        cntZero += 1;
                    }
                }
                info.add(new Area(i, j, cntZero));
            }
        }

        for (int i=0; i < info.size(); i++) {
            Area area = info.get(i);
            if (area.cntZero >= ground[area.i][area.j]) {
                ground[area.i][area.j] = 0;
            } else {
                ground[area.i][area.j] -= area.cntZero;
            }
        }
    }
}