// 프로그래머스 코딩테스트 연습 - 네트워크
package BFS_DFS;

class Network {
    
    public static void main(String[] args) {
        int a = 3;
        int[][] b = {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};
        System.out.println(solution(a, b));
    }


    public static void dfs(int n, int i, boolean[] visited, int[][] computers) {
        visited[i] = true;
        for (int j = 0 ; j < n ; j++) {
            if (computers[j][i] == 1 && visited[j] == false) {
                dfs(n, j, visited, computers);
            }
        }
    }

    public static int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        for (int i = 0 ; i < n ; i++) {
            visited[i] = false;
        }

        for (int i = 0 ; i < n ; i++){
            for (int j = 0; j < n ; j++) {
                if (computers[i][j] == 1 && visited[i] == false) {
                    dfs(n, i, visited, computers);
                    answer += 1;
                }
            }
        }

        return answer;
    }
}