// 프로그래머스 코딩테스트 연습 - 다리를 지나는 트럭
package stack_queue;
import java.util.*;

class Truck {
    int weight;
    int position;

    Truck(int weight, int position) {
        this.weight = weight;
        this.position = position;
    }
}

public class BridgeTruck {
    public static void main(String[] args) {
        // int bridge_length = 2;
        // int weight = 10;
        // int[] truck_weights = {7, 4, 5, 6};

        // int bridge_length = 100;
        // int weight = 100;
        // int[] truck_weights = {10};

        int bridge_length = 100;
        int weight = 100;
        int[] truck_weights = {10, 10, 10, 10, 10, 10, 10, 10, 10, 10};     

        System.out.println(solution(bridge_length, weight, truck_weights));
    }
    public static int solution(int bridge_length, int weight, int[] truck_weights) {
        int time = 0;
        Queue<Truck> beforeBridge = new LinkedList<>(); // 다리 오르기 전
        Queue<Truck> onBridge = new LinkedList<>(); // 다리 위

        for (int i = 0 ; i < truck_weights.length; i++) {
            Truck truck = new Truck(truck_weights[i], 0);
            beforeBridge.add(truck);
        }
        
        while (!(beforeBridge.isEmpty() && onBridge.isEmpty())) {
            int totalWeight = 0;
            for (Truck truck:onBridge) {
                totalWeight += truck.weight;
                truck.position++;

            }
            if (!onBridge.isEmpty() && onBridge.peek().position > bridge_length) {
                totalWeight -= onBridge.peek().weight;
                onBridge.poll();
            }

            if (!beforeBridge.isEmpty() && onBridge.size() <= bridge_length && beforeBridge.peek().weight + totalWeight <= weight) {
                beforeBridge.peek().position = 1;
                onBridge.offer(beforeBridge.poll());
            }
            time++;
        }
        return time;
    }
}