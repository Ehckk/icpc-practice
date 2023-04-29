import java.util.Stack;
import java.util.Scanner;

class SpidermanWorkout {
    int numDist;
    int bestHeight = (int) 1e9;
    String bestPath;
    Stack<Integer> path;
    int[] dist;

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);

        SpidermanWorkout spidermanWorkout = new SpidermanWorkout();
        int numCases = Integer.parseInt(scnr.nextLine());
        while (numCases > 0) {
            spidermanWorkout.readInput(scnr);
            numCases--;
        }
        scnr.close();
    }   
    
    public void readInput(Scanner scnr) {
        numDist = Integer.parseInt(scnr.nextLine());
        bestPath = "IMPOSSIBLE";
        dist = new int[numDist];
        for (int i = 0; i < numDist; i++) {
            dist[i] = scnr.nextInt();
        }
        scnr.nextLine();
        path = new Stack<Integer>();
        path.push(1);
        spiderman(dist[0], 1, dist[0]);
        System.out.println(bestPath);
    }

    public void spiderman(int current, int size, int maxHeight) {
        if (size == numDist) {
            if (maxHeight < bestHeight) {
                updateBestPath();
                bestHeight = maxHeight;
            }
            return;
        }
        if (current - dist[size] >= 0) { // Then we can go down
            path.push(-1);
            spiderman(current - dist[size], size + 1, maxHeight);
            path.pop();
        }
        if (current + dist[size] < bestHeight) { // Then we can go up
            path.push(1);
            spiderman(current + dist[size], size + 1, Math.max(maxHeight, current + dist[size])); // And (potentially) find something better
            path.pop();
        }
    }

    public void updateBestPath() {
        StringBuilder sb = new StringBuilder(numDist);
        for(int i = 0; i < path.size(); i++) {
            sb.append(path.get(i) == 1 ? 'U' : 'D');
        }
        bestPath = sb.toString();
    }
}
