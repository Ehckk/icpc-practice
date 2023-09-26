import java.util.*;

class Promotions {
    int minPromotions;
    int maxPromotions;
    int numEmployees;
    int numRules;

    HashMap<Integer, ArrayList<Integer>> graph;
    boolean[] visited = new int[numEmployees];
    int[] minSteps;
    int[] maxSteps;

    public static void main(String[] args) {
        Promotions promotions = new Promotions();
        Scanner scnr = new Scanner(System.in);
        promotions.readInput(scnr);
        promotions.findPromotions();
    }

    public void readInput(Scanner scnr) {
        String[] line = scnr.nextLine().trim().split(" ");
        minPromotions = Integer.parseInt(line[0]);
        maxPromotions = Integer.parseInt(line[1]);
        numEmployees = Integer.parseInt(line[2]);
        numRules = Integer.parseInt(line[3]);

        graph = new HashMap<Integer, ArrayList<Integer>>();
        minSteps = new int[numEmployees];
        Arrays.fill(minSteps, Integer.MAX_VALUE);
        maxSteps = new int[numEmployees];

        visited = new boolean[numEmployees];


        for (int i = 0; i < numEmployees; i++) {
            graph.put(i, new ArrayList<Integer>());
        }

        for (int i = 0; i < numRules; i++) {
            line = scnr.nextLine().trim().split(" ");
            int x = Integer.parseInt(line[0]);
            int y = Integer.parseInt(line[1]);

            // Directed edges represented as "dependencies for" not "dependent on"
            // graph.get(y).add(x);
             graph.get(x).add(y);
        }
    }

    public void findPromotions() {
        // Get max number of steps required to reach node
        for (int node :  graph.keySet()) {
            if (visited[node]) continue;
            depthFirstSearch(node, 1);
        }

        // For each i of minPromotions
        // Count the nodes removed
        //
        // For each i of maxPromotions
        // Count the nodes removed
        //
        int aCount = 0;
        int bCount = 0;
        // for (int i = 0; i < )
        System.out.println(Arrays.toString(minSteps));
        System.out.println(Arrays.toString(maxSteps));
    }

    public void depthFirstSearch(int node, int depth) {
        if (visited[node]) {
            minSteps[node] = Math.min(depth, minSteps[node]);
            maxSteps[node] = Math.max(depth, maxSteps[node]);
            return;
        }
        visited[node] = true;
        minSteps[node] = depth;
        maxSteps[node] = depth; 
        for (int adj : graph.get(node)) {
            depthFirstSearch(adj, depth + 1);
        }
    }
}