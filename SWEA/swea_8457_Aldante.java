import java.util.Scanner;

public class swea_8457_Aldante {
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args){
        int T = sc.nextInt();
        for (int tc = 1; tc <= T; tc++){
            int n = sc.nextInt();
            int b = sc.nextInt();
            int e = sc.nextInt();
            int sandtimer[] = new int[n];
            
            for (int i=0; i<n ; i++) sandtimer[i] = sc.nextInt();
            
            int res = 0;
            for (int i=0; i<n ; i++){
                int t = 1;
                while(true){
                    if (sandtimer[i] * t <= b-e){
                        t++;
                    }
                    else if (sandtimer[i] * t <= b+e){
                        res++; 
                        break;
                    }
                    else{
                        break;
                    }
                }
            }
            System.out.printf("#%d %d", tc, res);
        }

    }
}