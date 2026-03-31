# PageRank

PageRank is the fundamental algorithm behind Google's Search Engine. It operates on the assumption that web pages will link to each other, with the most important websites receiving the most links, allowing them to rank among the first for a specific search. Specifically, PageRank works by counting the number and quality of links to a page. Through that, a rough estimation of the page's importance is determined.

This PageRank was written as part of a mandatory assignment for my course in Linear Algebra and Optimisation back in 2019. It implements two functions: 1) the Random Surfer, which will jump to a random node in the graph or follow a random edge, and increments each visitation to a page stored in a list, and 2) the PageRank itself, represented as a matrix and the eigenvectors holding the importance scores for a page.

EDIT: PageRank's patent expired in 2019. Furthermore, Google no longer relies solely on PageRank for its Search Engine.

## Disclaimer
The code relies on `NetworkX` and `numpy` to run. `numpy` is important as it increases the speed of the PageRank algorithm by an order of magnitude. `NetworkX` is important to read the adjacent list and create a graph from it.

Furthermore, the `bigRandom.txt` data file was excluded from this GitHub due to size issues.

## PageRank Formula
$x_{k+1} = (1 - m)Ax_k + (1 - m)Dx_k + mSx_k$

```
x: eigenvector
k: iteration counter
m: damping factor
A: stochastic matrix
D: dangling node matrix
S: "lowest score" matrix
```

## Usage
To run this file, download the files and navigate to their placement from the terminal. After, input the following:
```
python3 PageRank_Algorithm.py <data-file>
```
**Note**: No random data file will do. The data _must_ be in the form of integer edge pairs, one pair per line. The integer pairs can be duplicates of earlier pairs to represent multiple edges between nodes, but additional edges between nodes are ignored and do not count towards the total importance. Reflexive edges are likewise allowed but ignored. Comments may be included in the data file.

See sample data in the `PageRankExampleData` directory.

## Example Input
Data file: `three.txt`
```
# 4 nodes
0 1   
0 2
1 2   
2 0   
2 1
2 3
```

## Example Output
```
##########
```
