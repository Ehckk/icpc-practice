# include <bits/stdc++.h>
using namespace std;

void findBridges(int current, int parent);
int exploreCave();

vector<set<int>> graph; // Adjacency list for graph
vector<int> discoveryTime; // Track the time each node is "discovered" in the DFS traversal 
vector<int> minTime; // Shortest possible time the node can be discovered
vector<pair<int, int>> bridges;

int tim = 0; // Track the order of discovery (first visit) through DFS
int numNodes, numEdges; // Number of nodes and edges

int main() {
    scanf("%d %d", &numNodes, &numEdges);    
    graph.resize(numNodes);
    discoveryTime.resize(numNodes, -1);
    minTime.resize(numNodes, -1);

    for (int i = 0; i < numEdges; i++) {
        int node1, node2; scanf("%d %d", &node1, &node2);
        graph[node1].emplace(node2);
        graph[node2].emplace(node1);
    }

    findBridges(0, -1);
    cout << exploreCave() << endl;
}

void findBridges(int current, int parent) {
    discoveryTime[current] = tim; // Set discovery time
    minTime[current] = tim; // Assume the minimum possible discovery time is the current discovery time 

    for (auto const& next : graph[current]) { // Loop over adjacent nodes
        if (next == parent) continue; // Avoid child-parent connection
        
        if (discoveryTime[next] == -1) { // Node has not yet been discovered
            tim++; // Increment time 
            findBridges(next, current); // Recurse on the child node
            // After DFS from next node, discovery times for relevant nodes should be set
            if (discoveryTime[current] < minTime[next]) { // Next node cannot possibly be discovered before current node
                bridges.push_back({ current, next }); // We have found a bridge 
            }
            minTime[current] = min(minTime[current], minTime[next]); // Next node 
        } else { // Next node already discovered, so next node has anscestor that is NOT current node 
            minTime[current] = min(minTime[current], discoveryTime[next]); // Update min time accordingly
        }
    }
}

int exploreCave() {
    int node1, node2;
    for (auto const& bridge : bridges) {
        node1 = bridge.first;
        node2 = bridge.second;
        graph[node1].erase(node2);
        graph[node2].erase(node1); // Remove the bridge from the graph
    }

    vector<bool> visited;
    visited.resize(numNodes, false);

    int safeNodeCount = 0;

    stack<int> toVisit;
    toVisit.emplace(0);

    while (!toVisit.empty()) { // Normal DFS
        int current = toVisit.top(); 
        toVisit.pop();
        
        if (visited[current]) continue;
        visited[current] = true;

        safeNodeCount++;
        for (int next : graph[current]) {
            toVisit.push(next);
        }
    }
    return safeNodeCount;
}