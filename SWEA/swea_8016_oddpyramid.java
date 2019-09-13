import java.util.Scanner;
public class swea_8016_oddpyramid{
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args){
        int T = sc.nextInt();
        for (int tc=1; tc<=T ; tc++){
            long N = sc.nextLong();
            long f_num = 2*N*N - 4*N + 3;
            long l_num = f_num + 2*(2*N - 2);

            System.out.println("#"+tc+" "+f_num+" "+l_num);
        }

    }
}