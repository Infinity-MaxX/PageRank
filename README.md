# PageRank

PageRank is the fundamental algorithm behind Google's Search Engine. It operates on the assumption that web pages will link to each other, with the most important websites receiving the most links, allowing them to rank among the first for a specific search. Specifically, PageRank works by counting the number and quality of links to a page. Through that, a rough estimation of the page's importance is determined.

This program was written during my course in Linear Algebra and Optimisation back in 2019. It implements two functions: 1) Random Surfer, which will jump to a random node in the graph or follow a random edge and increment the score total for that page, and 2) PageRank itself, represented as a matrix and its eigenvectors, which hold the importance scores for a page.

## Prequisites
The code relies on `NetworkX` and `numpy` to run. `numpy` is important as it increases the speed of the PageRank algorithm by about an order of magnitude. `NetworkX` is for reading in the edges between nodes and creating a graph from it.

You can install each necessary package through `pip install <networkx/numpy>`.

## Disclaimer
The code defaults to 100 iterations for Random Surfer and PageRank each. This can result in disagreements between the two sets of results as 100 iterations mean different things for each function. This means that the result may vary each time you run the code, even on the same file. This can be adjusted if needed, but as is, the code works best on graphs of appropriate sizes.

100 iterations works well for PageRank of any sized graph, but for Random Surfer, you may want to adjust the number of iterations by about 10k to make the scores between the functions more likely to align.

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
python PageRank_Algorithm.py <data-file>
```
**Note**: No random data file will do. The data _must_ be in the form of integer edge pairs, one pair per line. The integer pairs can be duplicates of earlier pairs to represent multiple edges between nodes, but additional edges between nodes are ignored and do not count towards the total importance. Reflexive edges are likewise allowed but ignored. Comments may be included in the data file.

See sample data in the `PageRankExampleData` directory.

## Example Input
Data file: `wikipedia.txt`
```
# 11 nodes
1 2
2 1
3 0 
3 1
4 3 
4 1 
4 5
5 1 
5 4
6 1 
6 4
7 1 
7 4
8 1 
8 4
9 1 
9 4
10 1 
10 4
```

## Example Output
```
Top 10 visited nodes are:  [('1', 34), ('2', 27), ('4', 13), ('3', 6), ('0', 5), ('5', 4), ('6', 3), ('9', 3), ('8', 2), ('10', 2)]

Node: 1
Score: 0.40014745686695474

Node: 2
Score: 0.3561242552742236

Node: 4
Score: 0.06457156444888226

Node: 3
Score: 0.03429417008582068

Node: 5
Score: 0.03429417008582068

Node: 0
Score: 0.030573915778444496

Node: 10
Score: 0.01599889349197071

Node: 6
Score: 0.01599889349197071

Node: 7
Score: 0.01599889349197071

Node: 8
Score: 0.01599889349197071
```
