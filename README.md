Albert-Ludwigs-Universität Freiburg

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*

Course ILIAS: [web page link](https://ilias.uni-freiburg.de/ilias.php?ref_id=2339316&cmdClass=ilobjcoursegui&cmd=view&cmdNode=zf:ns&baseClass=ilRepositoryGUI)

---
## Bioinformatics 1
###### WS 2021/2022
##### Exercise sheet 10: UPGMA
---

The following introduction is mainly taken from en.wikipedia.org.
A phylogenetic tree or evolutionary tree is a branching diagram or ”tree” showing the inferred
evolutionary relationships among various biological species or other entities based upon similarities
and differences in their physical and/or genetic characteristics. The taxa joined together in the tree
are implied to have descended from a common ancestor. In a rooted phylogenetic tree, each node
with descendants represents the inferred most recent common ancestor of the descendants, and the
edge lengths in some trees may be interpreted as time estimates. Each node is called a taxonomic
unit. Internal nodes are generally called hypothetical taxonomic units (HTUs) as they cannot be
directly observed.

**UPGMA** (Unweighted Pair Group Method with Arithmetic Mean) is a simple agglomerative or
hierarchical clustering method used in bioinformatics for the creation of phylogenetic trees. UP-
GMA assumes a constant rate of evolution (molecular clock hypothesis), and is not a well-regarded
method for inferring phylogenetic trees unless this assumption has been tested and justified for the
data set being used.

Distances for a merged cluster e, where e = c ∪ d:

<p align="center">
<img src="./figures/upgma.svg" alt="WPGMA and UPGMA" width="70%"/>
</p>


### _Exercise 1 -  UPGMA and WPGMA

Calculate the according evolutionary tree using WPGMA and the pairwise distances in the following distance matrix.

| D<sub>ij</sub>| a  | b  | c  | d  | e  |
|---------------|----|----|----|----|----|
| **a**         |  0 |  3 | 12 | 12 |  9 |
| **b**         |    |  0 | 13 | 13 | 10 |
| **c**         |    |    |  0 |  6 |  7 |
| **d**         |    |    |    |  0 |  7 |
| **e**         |    |    |    |    |  0 |

**a)** Which leaves should be selected first?

- [ ] c and d
- [ ] a and b
- [ ] d and e

**b)** Calculate the corresponding distance for the set of leaves from **a**.

**c)** Given your answers from **a** and **b**, which of the following distance matrices corresponds
to the correct distances from the set of leaves (or internal node) in **a** to all other leaves.

**1.**

| D<sub>ij</sub>| {a,b}  | c    | d    | e   | 
|---------------|--------|------|------|-----|
| **{a,b}**     |  0     | 12.5 | 12.5 | 9.5 |
| **c**         |        |  0   | 13   | 7   |
| **d**         |        |      |  0   |  7  |
| **e**         |        |      |      |  0  |

**2.** 

| D<sub>ij</sub>| {a,b}  | c    | d    | e   | 
|---------------|--------|------|------|-----|
| **{a,b}**     |  0     | 10.5 | 10.5 | 9.5 |
| **c**         |        |  0   | 13   | 7   |
| **d**         |        |      |  0   |  7  |
| **e**         |        |      |      |  0  |

**3.** 

| D<sub>ij</sub>| {c,d}  | a    | b    | e   | 
|---------------|--------|------|------|-----|
| **{c,d}**     |  0     |  12  | 13   |  7  |
| **a**         |        |  0   | 13   |  7  |
| **b**         |        |      |  0   |  7  |
| **e**         |        |      |      |  0  |

**d)** Which nodes are joined next given the correct distance matrix from **c**?

- [ ] c and d
- [ ] {a,b} and e
- [ ] {c,d} and e
- [ ] e and a

**e)** Following the approach from the previous exercises, which of the following 
representations of the tree is correct? (Trees are given in [Newick format](https://en.wikipedia.org/wiki/Newick_format))
Feel free to inspect them using an [online tool](http://www.trex.uqam.ca/index.php?action=newick&project=trex)

- [ ] ((a : 1.5, b : 1.5) : 4, ((c : 3, d : 3) : 0.5, e : 3.5) : 2);
- [ ] ((a : 1.5, b : 1.5) : 4.25, ((c : 3, d : 3) : 0.5, e : 3.5) : 2.25);
- [ ] (((c : 3, d : 3) : 3.5, e : 3.5): 4, (a : 1.5, b : 1.5) : 2);