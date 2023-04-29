#include <bits/stdc++.h>
#include<iostream>
using namespace std;
#define size 6
int minimumDistance(int distance[], bool visited[]) {
  int min = INT_MAX;
  int min_index = INT_MAX;
  for (int i = 0; i < size; i++) {
    if (!visited[i] && distance[i] <= min) {
      min = distance[i];
      min_index = i;
    }
  }
  return min_index;
}
void printParentPath(int parent[], int i) {
  if (parent[i] == -1) {
    return;
  }
  printParentPath(parent, parent[i]);
  cout << i + 1 << " ";
}
void dijkstra(int graph[size][size], int source) {
  int distance[size];
  bool visited[size];
  int parent[size];
  for (int i = 0; i < size; i++) {
    parent[0] = -1;
    distance[i] = INT_MAX;
    visited[i] = false;
  }
  distance[source] = 0;
  for (int i = 0; i < size - 1; i++) {
    int U = minimumDistance(distance, visited);
    visited[U] = true;
    for (int j = 0; j < size; j++) {
      int curr_distance = distance[U] + graph[U][j];
      if (!visited[j] && graph[U][j] &&
          curr_distance < distance[j]) {
        parent[j] = U;
        distance[j] = curr_distance;
      }
    }
  }
  cout << "Vertex\t\tDistance\tPath" << endl;
  for (int i = 1; i < size; i++) {
    cout << source + 1 << "->" << i + 1 << "\t\t" << distance[i] << "\t\t"
         << source + 1 << " ";
    printParentPath(parent, i);
    cout << endl;
  }
}
int main() {
  int graph[size][size] = {{0, 2, 4, 0, 0, 0},{0, 0, 1, 7, 0, 0},{0, 0, 0, 0, 3, 0},{0, 0, 0, 0, 0,1},{0, 0, 0, 2, 0, 5},{0, 0, 0, 0, 0, 0}};
  dijkstra(graph, 0);
}
