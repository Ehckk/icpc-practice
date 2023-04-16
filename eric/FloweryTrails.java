import java.util.Scanner;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.PriorityQueue;

public class FloweryTrails {
	private HashMap<Integer, ArrayList<int[]>> graph; // HashMap for constructing adjacency list for graph
	private PriorityQueue<int[]> priorityQueue; // Priority queue for Dijkstra's Algorithm implementation
	private int[] distances; // Distance table for Dijkstra's Algorithm implementation 

	private int[][] trails; // Trails lookup table for modified Dijkstra's Algorithm implementation
	private HashMap<Integer, int[]> parents; // Parents lookup table for modified Dijkstra's Algorithm implementation
	// Key: pathId, Value: [<previous node>, <next node>, <trail id>, <previous path id>]

	private int numberOfNodes;
	private int numberOfTrails;
	private int totalDistance; // Value to keep track of the total path length of all shortest paths

	public static void main(String[] args) {
		Scanner scnr = new Scanner(System.in);

		FloweryTrails flowerTrails = new FloweryTrails();
		flowerTrails.readInput(scnr);
		flowerTrails.findShortestPath();
	}

	public void readInput(Scanner scnr) {
		graph = new HashMap<Integer, ArrayList<int[]>>(); // Initialize graph

		String[] input = scnr.nextLine().trim().split(" "); // Read first line
		numberOfNodes = Integer.parseInt(input[0]); // Parse number of nodes
		numberOfTrails = Integer.parseInt(input[1]); // Parse number of trails
		distances = new int[numberOfNodes]; // Initialize array to keep track of distances 
		
		trails = new int[numberOfTrails][2]; // Initialize lookup table to keep track of trails and whether or not they have been walked 
		parents = new HashMap<Integer, int[]>(); // Initialize lookup to keep track of the different paths walked (DP) 
		totalDistance = 0; // Initialize total distance

		for (int i = 0; i < numberOfNodes; i++) {
			graph.put(i, new ArrayList<int[]>()); // Initialize adjacency list keys
			if (i == 0) {
				distances[i] = i == 0 ? 0 : Integer.MAX_VALUE; // Set distance value as 0 for node 0
			} else {
				distances[i] = i == 0 ? 0 : Integer.MAX_VALUE; // Initialize distance value as infinity for all other nodes
			}
		}

		int node1, node2, distance;
		for (int i = 0; i < numberOfTrails; i++) {
			input = scnr.nextLine().trim().split(" "); // Read each connection line
			
			node1 = Integer.parseInt(input[0]); // Parse node 1 
			node2 = Integer.parseInt(input[1]); // Parse node 2

			if (node1 == node2) continue; // We don't care if a node connects to itself
			distance = Integer.parseInt(input[2]); // Parse distance 

			trails[i][0] = distance; // First value is length of the trail
			trails[i][1] = 0; // Second value is 1 if trail has been accounted for in total length of all shortest paths, else 0

			graph.get(node1).add(new int[] { node2, distance, i }); // Connections are triplets in adj. list: (<node>, <distance>, <trail id>)
			graph.get(node2).add(new int[] { node1, distance, i }); // Connections are two-way
		}
		scnr.close();
	}

	public void findShortestPath() {
		priorityQueue = new PriorityQueue<int[]>(numberOfTrails, (v1, v2) -> v1[1] - v2[1]); // Initialize priority queue
		priorityQueue.add(new int[] { 0, 0, -1 }); // Enqueue starting node

		int[] current;
		int[] shortestPath = {  Integer.MAX_VALUE, 0 }; // (<distance>, <number of shortest paths>) 
		while (!priorityQueue.isEmpty()) { // Modified BFS for Dijkstra's Algorithm
			current = priorityQueue.poll(); // Removes head of priority queue
			int index = current[0];
			int dist = current[1];
			int pathId = current[2];
			int nextPathId = parents.size();
			
            for (int[] connection : graph.get(index)) { // Loop over connected vertices
				int nextIndex = connection[0];
				int nextDist = connection[1];
				int nextTrailId = connection[2];
				
				int oldDist = distances[nextIndex]; // Old distance
				int newDist = dist + nextDist; // New distance

				boolean newPathIsLonger = newDist > oldDist; // Compare new distance with stored path distance
				if (newPathIsLonger) continue; // New path is longer, so who cares
				distances[nextIndex] = newDist; // Update distance of node connection
				parents.put(nextPathId, new int[] { nextTrailId, pathId });
				if (nextIndex == numberOfNodes - 1) { // We have made it to node 9
					if (newDist < shortestPath[0]) { // We have found a shorter path than the current shortest path
						totalDistance -= shortestPath[0] * shortestPath[1]; // Subtract the previously stored total area  
						shortestPath[0] = newDist; // Accounts for finding a path shorter than a path previously thought to be the shortest
						shortestPath[1] = 0;
					}
					shortestPath[1]++;
					updateTotalDistance(nextPathId);
					continue;
				}
				priorityQueue.add(new int[] { nextIndex, newDist, nextPathId }); // Add this path to the priority queue
				nextPathId++; 
			}
		}
		System.out.println(totalDistance * 2);
	}

	public void updateTotalDistance(int pathId) {
		int[] path = parents.get(pathId); 
		int trail = path[0]; // Get trail ID
		int prevPathId = path[1]; // Get previous path ID
		
		if (prevPathId != -1) updateTotalDistance(prevPathId); // We not made it to node 0, recurse on parent node

		int length = trails[trail][0]; // Get length of trail
		boolean hasBeenWalked = trails[trail][1] == 1; // Has the trail been accounted for?
		if (!hasBeenWalked) { // Trail has not been accounted for in total distance
			totalDistance += length; // Add trail length to total distance
			trails[trail][1] = 1; // Mark trail as accounted for
		}
	}
}
