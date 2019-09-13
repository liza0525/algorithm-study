import java.util.Scanner;

public class boj_9095_add123{
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args){
        int T = sc.nextInt();

        for (int i=1; i<=T; i++){
            int res;
            int num = sc.nextInt();
            res = dp(num);
            System.out.println(res);
        }
    }

    public static int dp(int num){
        if (num == 0)
            return 0;
        else if (num == 1)
            return 1;
        else if (num == 2)
            return 2;
        else if (num == 3)
            return 4;
        else
            return dp(num-1)+dp(num-2)+dp(num-3);
    }
}