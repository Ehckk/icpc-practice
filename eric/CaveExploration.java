import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

class CaveExploration {
    HashMap<Integer, HashSet<Integer>> graph; // Adjacency List for graph
    int time = 0; // Track the order of discovery (first visit) through DFS
    int[] discoveryTime; // Track the time each node is "discovered" in the DFS traversal 
    int[] minTime; // Shortest possible time the node can be discovered
    int numNodes, numEdges; // Number of nodes and edges
    ArrayList<int[]> bridges; // Keep track of the bridges we find

    public static void main(String[] args) {
        CaveExploration caveExploration = new CaveExploration();
        Scanner scnr = new Scanner(System.in);

        caveExploration.readInput(scnr);
        scnr.close();
        
        caveExploration.findBridges(0, -1); 
        
        // After the bridges have been found and removed, we can traverse the graph to find how many nodes remain connected
        System.out.println(caveExploration.exploreCave());
    }

    public void readInput(Scanner scnr) {
        String[] input = scnr.nextLine().trim().split(" ");
        numNodes = Integer.parseInt(input[0]);
        numEdges = Integer.parseInt(input[1]);

        discoveryTime = new int[numNodes]; // initialze discovery time array
        Arrays.fill(discoveryTime, -1); // set all values to -1 initially

        minTime = new int[numNodes]; // initialze minimum time array
        Arrays.fill(discoveryTime, -1); // set all values to -1 initially

        graph = new HashMap<Integer, HashSet<Integer>>(numNodes);
        bridges = new ArrayList<int[]>();

        for (int i = 0; i < numNodes; i++) {
            graph.put(i, new HashSet<Integer>());
        }

        int node1, node2;
        for (int i = 0; i < numEdges; i++) {
            input = scnr.nextLine().trim().split(" ");
            node1 = Integer.parseInt(input[0]);
            node2 = Integer.parseInt(input[1]);

            graph.get(node1).add(node2); // Add node1-node2 connection
            graph.get(node2).add(node1); // Add node2-node1 connection
        }
        // System.out.println(graph);
    }

    public void findBridges(int current, int parent) { // Recursive solution
        discoveryTime[current] = time; // Set discovery time
        minTime[current] = time; // Assume the minimum possible discovery time is the current discovery time 

        for (int next : graph.get(current)) { // Loop over adjacent nodes
            if (next == parent) continue; // Avoid child-parent connection
            
            if (discoveryTime[next] == -1) { // Node has not yet been discovered
                time++; // Increment time 
                findBridges(next, current); // Recurse on the child node
                // After DFS from next node, discovery times for relevant nodes should be set
                if (discoveryTime[current] < minTime[next]) { // Next node cannot possibly be discovered before current node
                    bridges.add(new int[] { current, next }); // We have found a bridge 
                }
                minTime[current] = Math.min(minTime[current], minTime[next]); // Next node 
            } else { // Next node already discovered, so next node has anscestor that is NOT current node 
                minTime[current] = Math.min(minTime[current], discoveryTime[next]); // Update min time accordingly
            }
        }
    }

    public int exploreCave() {
        int node1, node2;
        for (int[] bridge : bridges) {
            node1 = bridge[0];
            node2 = bridge[1];
            graph.get(node1).remove(node2);
            graph.get(node2).remove(node1); // Remove the bridge from the graph
        }

        boolean[] visited = new boolean[numNodes];
        int safeNodeCount = 0;
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(0);

        while (!stack.isEmpty()) {
            int current = stack.pop();
            
            if (visited[current]) continue;
            visited[current] = true;

            safeNodeCount++;
            for (int next : graph.get(current)) {
                stack.push(next);
            }
        }
        return safeNodeCount;
    }
}