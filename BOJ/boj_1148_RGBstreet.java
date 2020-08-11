import java.io.*;

public class boj_1148_RGBstreet {
    static int n;
    static int answer;
    static int[][] colorPrice;
    static int[][] totalPrice;

    public static void main(final String[] args) throws NumberFormatException, IOException {
        String txtPath = "../input.txt";
        BufferedReader br = new BufferedReader(new FileReader(txtPath));
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        colorPrice = new int[n][n];
        totalPrice = new int[n][n];

        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                colorPrice[i][j] = Integer.parseInt(line[j]);
            }
        }

        for (int i = 0; i < n; i++) {
            totalPrice[0][i] = colorPrice[0][i];
        }

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < 3; j++) {
                int cand = 9999999;
                for (int k = 0; k < 3; k++) {
                    if (j != k) { 
                        if (totalPrice[i-1][k] < cand) {
                            cand = totalPrice[i-1][k];
                        }
                    }
                }
                totalPrice[i][j] = colorPrice[i][j] + cand;
            }
        }

        answer = 9999999;
        for (int i = 0; i < n; i++) {
            if (totalPrice[n-1][i] < answer) {
                answer = totalPrice[n-1][i];
            }
        }

        System.out.println(answer);

        br.close();
    }
}