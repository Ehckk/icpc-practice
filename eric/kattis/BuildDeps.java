import java.util.Scanner;
import java.util.Stack;
import java.util.ArrayList;
import java.util.HashMap;

class BuildDeps {
    private HashMap<String, ArrayList<String>> graph = new HashMap<String, ArrayList<String>>();
    private HashMap<String, Boolean> visited = new HashMap<String, Boolean>();
    private Stack<String> stack = new Stack<String>();
    private String start;
    private int numberOfNodes;

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);   
        BuildDeps buildDeps = new BuildDeps();

        buildDeps.readInput(scnr);
        scnr.close();

        buildDeps.buildDepSearch();
    }

    public void readInput(Scanner scnr) {
        numberOfNodes = Integer.parseInt(scnr.nextLine().strip());
        
        for (int i = 0; i < numberOfNodes; i++) {
            String[] input = scnr.nextLine().trim().split(":");
            String file = input[0]; // File name - Key in adjacency list
            
            if (!graph.containsKey(file)) {
                graph.put(file, new ArrayList<String>()); // Initialize graph hashmap with empty list
            }
            visited.put(file, false); // Initialize visited hashmap with false  
            if (input.length == 1) continue; // No dependencies in line
            
            String[] deps = input[1].trim().split(" ");
            for (String dep : deps) {
                if (!graph.containsKey(dep)) {
                    graph.put(dep, new ArrayList<String>()); // Initialize graph hashmap with empty list
                }
                graph.get(dep).add(file);
            }
        }  
        System.out.println(graph);
        start = scnr.next();
    }

    public void findDeps(String file) { // Modified DFS to return TopSort of graph
        visited.put(file, true);

        ArrayList<String> deps = graph.get(file);
        for (String dep : deps) {
            if (visited.get(dep)) continue;
            findDeps(dep);
        }
        stack.push(file); 
    }

    public void buildDepSearch() {
        findDeps(start);

        while (!stack.isEmpty()) {
            System.out.println(stack.pop()); // The stack in the modified DFS allows the directed order to be maintained
        }
    }
}