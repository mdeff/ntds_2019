# Layouts tutorial

In this tutorial, we will try the most popular tools for graph exploration in Gephi. We will learn how to get visual insights by spatializing and highlighting important attributes of graphs. As an example, we will use a subnetwork of Wikipedia pages that had anomalous visitor activity over the period 15-31 October 2018. You can find the corresponding `.gexf` file in this folder.

Before starting this tutorial, install the following plugins (unless they are already installed):
* Multigravity Force Atlas 2
* Circle Pack layout
* Leiden algorithm
* Bridging centrality
* Clustering coefficient

Watch a short walk-through screencast to get an idea of what we are going to do in this tutorial. Attention: the video has sound.

[![YouTube link](https://img.youtube.com/vi/aRZIeTroUog/0.jpg)](https://www.youtube.com/watch?v=aRZIeTroUog)

### 1. Spatialize your graph with force-directed layouts.

To start with, let's spatialize our graph. To do that, we can use force-directed layouts. They don't require any attributes and quite easy to setup. We will try four layouts: **Multigravity Force Atlas 2**, **Yuifan Hu**, **Fruchterman-Reingold**, **Open Ord**. You can find all these layouts in the "Layout" pane. Here are some tips related to the parameters of each algorithm:

* Parameters
	* Multigravity Force Atlas 2
		* *Scaling*. Control scale of the expansion of the graph. 
		* *Dissuade hubs*. Apply stronger repulsive forces to hubs.
		* *Prevent overlap*. Prevent nodes from overlapping.
	* Yifan Hu
		* *Step ratio*. High ratio improves quality (at the expense of speed)
		* *Optimal distance*. Controls distance between nodes
		* *Theta*. Smaller Theta gives leads to more accurate results (slower)
	* Fruchterman-Reingold (expensive)
		* *Gravity*. Attraction strength.
		* *Speed*. A tradeoff between speed and accuracy. Higher values lead to faster but less accurate results
	* Open Ord
		* *Edge Cut (0 to 1)*. Higher values lead to more clustered results.
		* *Num Iterations*. Higher values lead to larger expansion.

In the following examples, colors correspond to *modularity*.

Multigravity Force Atlas 2 |  Yifan Hu | Fruchterman-Reingold | Open Ord
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
![Multigravity Force Atlas 2](https://raw.githubusercontent.com/mizvol/gephi-tutorials/master/Layouts/images/force-atlas.gif)  |  ![Yifan-hu](https://raw.githubusercontent.com/mizvol/gephi-tutorials/master/Layouts/images/yifan-hu.gif) | ![Fruchterman-Reingold](https://raw.githubusercontent.com/mizvol/gephi-tutorials/master/Layouts/images/f-r.gif) | ![Open Ord](https://raw.githubusercontent.com/mizvol/gephi-tutorials/master/Layouts/images/openord.gif)

### 2. Highlight attributes

With Gephi, we can highlight attributes of the nodes using different colors and sizes, reflecting the scale of the attributes. You can do it using "Appearance" pane. Before using the attributes, we should compute them using "Statistics" pane.

Some examples of attributes that can be used of sizing and coloring are listed below.

#### Node and label size

We can use the size to highlight local attributes of nodes.

   1. [Degree](https://en.wikipedia.org/wiki/Degree_(graph_theory)). Connectivity of a node
   2. Centrality
   		* [Betweenness](https://en.wikipedia.org/wiki/Betweenness_centrality). Number of random walks passing through the node
   		* [Bridging](http://www.cbmc.it/fastcent/doc/Bridging.htm). A measure of bi-partisanship of a node. Nodes that connect multiple communities (serve as bridges) have high bridging centrality
   3. [Page rank](https://en.wikipedia.org/wiki/PageRank). Importance of a node
   4. [Local clustering coefficient](https://en.wikipedia.org/wiki/Clustering_coefficient). Determines how close are neighbors of a node to a complete graph

#### Color

Coloring different communities of the graph is a allows to explore the structure of your graph and make it more visually appealing. To do that, we need to run a community detection algorithm. Once you compute communities, you can color the graph using "Appearance" pane.

   1. Community detection algorithms
   		* [Louvain modularity](https://en.wikipedia.org/wiki/Louvain_modularity) (*Modularity* in Gephi)
   		* [Leiden algorithm](https://www.nature.com/articles/s41598-019-41695-z)
    
### 3. Use attributed layouts

Gephi also provides a set of attributed layouts. You can use them to spatialize nodes according to their attributes. Here are a few examples of attributed layouts:

1. *Circular*. We can use it to show the distribution of nodes and their links and order nodes by an attribute and draw them on a circle.
2. *Radial Axis*. This layout allows studying homophily by showing distributions of nodes inside groups. Axes radiate from the central circle. The layout groups nodes by an attribute and draw them in axes.
3. *Network splitter 3D*. Use this if you want to unfold the graph in layers based on attributes. However, there is a trick. To use it, you need to copy a column with an attribute of interest and add *[Z]* in the end of the name of the column. *Z-maximum level* parameter should be equal to the number of layers you want to get, e.g. number of communities if you use communities as a splitting attribute.
4. *Circle pack*. This layout allows to group nodes by attribute(s) and plotting them in circles.

In the examples below, we use *modularity* as an attribute.

Circular |  Radial Axis | Network splitter 3D | Circle pack
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
![Circular](https://raw.githubusercontent.com/mizvol/gephi-tutorials/master/Layouts/images/circular.png)  |  ![Radial Axis](https://raw.githubusercontent.com/mizvol/gephi-tutorials/master/Layouts/images/radial-axis.png) | ![Network splitter 3D](https://raw.githubusercontent.com/mizvol/gephi-tutorials/master/Layouts/images/net-splitter.png) | ![Circle pack](https://raw.githubusercontent.com/mizvol/gephi-tutorials/master/Layouts/images/circle-pack.png)

### 4. Enhance readability with spatial transformation layouts

Normally, after all the transformations we have performed, it's hard to read labels. To enhance readability and interpretability of your graph, use the following layouts.

1. *Expansion/Contraction*. This layout simply changes the scale of the graph.
2. *Noverlap*. Use it to prevent overlap of nodes.
3. *Label adjust*. This layout spatializes labels so that they are easier to read. Before running it, you should display labels.

#### 5. Additional resources

If you want to learn how to publish Gephi graphs online, take a look at [this](https://github.com/mizvol/gephi-tutorials/blob/master/SigmaJS%20exporter/README.md) tutorial.

For more information, check out official Gephi tutorials:

1. [Gephi tutorial](https://gephi.org/users/tutorial-layouts/) on layouts. 
2. Other [Gephi tutorials](https://gephi.org/users/).
