import java.util.Scanner;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.PriorityQueue;

class FloweryTrails {
	private HashMap<Integer, ArrayList<long[]>> graph; // Adjacency list for Dijkstra's Algorithm
	private PriorityQueue<long[]> priorityQueue; // Priority queue for Dijkstra's Algorithm
	private long[] distances; // Distance table for Dijkstra's Algorithm 
	private HashMap<Integer, ArrayList<Integer>> parents; // Parent subgraph for modified Dijkstra's Algorithm 

	private HashMap<Integer, HashMap<Integer, Long>> shortestEdges; // Maps the shortest edges at each point to ignore inefficient edges
	private boolean[] visited; // Tracks the fully visited nodes for modified Dijkstra's Algorithm

	private int numberOfNodes, numberOfTrails; // Number of point and trails

	public static void main(String[] args) {
		Scanner scnr = new Scanner(System.in);

		FloweryTrails flowerTrails = new FloweryTrails();
		flowerTrails.readInput(scnr);
		flowerTrails.findShortestPath();
		flowerTrails.getTotalDistance();
	}

	public void readInput(Scanner scnr) {
		String[] input = scnr.nextLine().trim().split(" "); // Read first line
		numberOfNodes = Integer.parseInt(input[0]); // Parse number of nodes
		numberOfTrails = Integer.parseInt(input[1]); // Parse number of trails

		graph = new HashMap<Integer, ArrayList<long[]>>(); // Initialize graph
		distances = new long[numberOfNodes]; // Initialize distances array		
		parents = new HashMap<Integer, ArrayList<Integer>>(); // Initialize parents table
		shortestEdges = new HashMap<Integer, HashMap<Integer, Long>>(); // Initialize shortest edge table
		visited = new boolean[numberOfNodes]; // Initialize visited array

		for (int i = 0; i < numberOfNodes; i++) {
			graph.put(i, new ArrayList<long[]>());
			distances[i] = Long.MAX_VALUE; // Fill distances array with infinite constants
			shortestEdges.put(i, new HashMap<Integer, Long>()); // Initialize shortestEdge table for each polong
			parents.put(i, new ArrayList<Integer>()); // Initialize parents subgraph
		}
		distances[0] = 0; // Set distances from 0 (first node) to 0

		int node1, node2;
		long distance;
		for (int i = 0; i < numberOfTrails; i++) {
			input = scnr.nextLine().trim().split(" "); // Read each connection line
			node1 = Integer.parseInt(input[0]); // Parse node 1 
			node2 = Integer.parseInt(input[1]); // Parse node 2
			distance = Integer.parseInt(input[2]); // Parse distance

			if (node1 == node2) continue; // We don't care if a node connects to itself
			
			graph.get(node1).add(new long[] { node2, distance }); // Connections are pairs in adj. list: (<node>, <distance>)
			graph.get(node2).add(new long[] { node1, distance }); // Connections are two-way		
			if (shortestEdges.get(node1).get(node2) == null) { // No value is set
				shortestEdges.get(node1).put(node2, distance); // Set distance
				shortestEdges.get(node2).put(node1, distance); 
			} else {
				long newDistance = Math.min(shortestEdges.get(node1).get(node2), distance); // Set distance to whichever is smaller  
				shortestEdges.get(node1).put(node2, newDistance); // Update distance
				shortestEdges.get(node2).put(node1, newDistance);
			}
		}
		scnr.close();
	}

	public void findShortestPath() { // Modified Djikstra's Algorithm to build a subgraph of only the shortest paths
		priorityQueue = new PriorityQueue<long[]>(numberOfTrails, (v1, v2) -> (int) (v1[1] - v2[1])); // Initialize priority queue
		priorityQueue.add(new long[] { 0, 0 }); // Enqueue starting node

		while (!priorityQueue.isEmpty()) {
			long[] current = priorityQueue.poll(); // Remove first element from priority queue			
			int node = (int) current[0];
			if (visited[node]) continue; // If the element was visited, ignore it
			visited[node] = true; // Visit node

			for (long[] adjacent : graph.get(node)) {
				int next = (int) adjacent[0];
				long oldDist = distances[next];
				long newDist = distances[node] + adjacent[1]; 
				if (newDist < oldDist) { // New distance is shorter
					distances[next] = newDist; // Update the distance

					parents.get(next).clear(); // Remove any previously found connections because this one is shorter
					parents.get(next).add(node); // Add this connection to the parent table

					priorityQueue.add(adjacent); // Add the node to the priority queue
					continue;
				}
				if (newDist == oldDist) { // Distances are the same
					parents.get(next).add(node); // Add this connection to the parent table
					continue;
				}
			}
		}
	}

	public void getTotalDistance() { // Used to traverse the parents and sum the distances
		long totalDistance = 0;
		Arrays.fill(visited, false); // Reset visited array
		ArrayDeque<Integer> queue = new ArrayDeque<Integer>(numberOfNodes);

		queue.add(numberOfNodes - 1); // Start with the maximum value node
		while (!queue.isEmpty()) { // BFS
			int current = queue.poll(); // Remove first element from queue
			
			if (visited[current]) continue; // If the element was visited, ignore it
			visited[current] = true; // Visit node

			for (int next : parents.get(current)) {
				totalDistance += shortestEdges.get(current).get(next); // Get the minimum distance between the two nodes, add it to total

				queue.add(next); // Enqueue the node
			}
		}
		System.out.println(totalDistance * 2); // Output
	}
}