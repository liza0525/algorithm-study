class Solution {
    public static void main(String[] args) {
        int[] citations = {3, 0, 6, 1, 5};
        System.out.println(solution(citations));
    }

    public static int solution(int[] citations) {
        int answer = 0;
        for (int h = citations.length ; h > -1 ; h--) {
            int highH = 0;
            for (int c = 0 ; c < citations.length ; c++) {
                if (citations[c] >= h) {
                    highH += 1;
                }
            }
            if (highH >= h) {
                answer = h;
                break;
            }
        }
        return answer;
    }
}