import java.util.Scanner;
import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayList;

class RunningMom {
    private HashMap<String, ArrayList<String>> graph = new HashMap<String, ArrayList<String>>(); // Graph
    private HashMap<String, Boolean> visited = new HashMap<String, Boolean>(); // Visited cities
    private HashMap<String, Boolean> safeCityMap = new HashMap<String, Boolean>(); // Maps cities to whether or not they are safe
    private HashSet<String> checking = new HashSet<String>(); // Set, will track valid (safe) cities along the recursion 

    private ArrayList<String> startingCities = new ArrayList<String>(); // Stores the origin cities

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in); 
        RunningMom rMom = new RunningMom();

        rMom.readInput(scnr);
        scnr.close();

        rMom.runningMom();
    }

    public void readInput(Scanner scnr) {
        int count = Integer.parseInt(scnr.nextLine().strip());
        for (int i = 0; i < count; i++) {
            String[] input = scnr.nextLine().trim().split(" ");
            String city = input[0];
            String destination = input[1]; 

            if (!graph.containsKey(city)) {
                graph.put(city, new ArrayList<String>()); 
            }
            if (!graph.containsKey(destination)) {
                graph.put(destination, new ArrayList<String>()); 
            }
            graph.get(city).add(destination);
            if (!visited.containsKey(city)) {
                visited.put(city, false);
            }
            if (!visited.containsKey(destination)) {
                visited.put(destination, false);
            }
        }  
        while (scnr.hasNextLine()) {
            startingCities.add(scnr.nextLine().trim());
        }
        System.out.println(graph);
        System.out.println(startingCities);
        System.out.println(visited);
    }

    public boolean findSafeCity(String city) { // Modified DFS
        visited.put(city, true);
        checking.add(city);

        ArrayList<String> destinations = graph.get(city);
        boolean cityIsSafe;
        for (String destination : destinations) {
            if (visited.get(destination)) {
                cityIsSafe = checking.contains(destination);
            } else {
                cityIsSafe = findSafeCity(destination);
            }
            if (!cityIsSafe) continue;
            safeCityMap.put(destination, true);
            return true;
        }
        checking.remove(city);
        return false;
    }

    public void runningMom() {
        for (String city : startingCities) {
            safeCityMap.put(city, findSafeCity(city));
        }
        for (String city : startingCities) {
            System.out.printf("%s %s%n", city, safeCityMap.get(city) ? "safe" : "trapped");
        }
    }
}
