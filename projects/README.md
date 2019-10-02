# Dataset and project ideas for NTDS'19

## A word on preparing the data

For all projects, some degree of pre-processing is needed before obtaining usable data.
That is inherent to the work of a data scientist, and will mostly involve the following steps.

1. **Data acquisition.**
   Raw data may need to be (i) collected via a web API, (ii) collected by scraping a website, or (iii) already collected and packaged (for example in a CSV file).
2. **Data importation.**
   Raw data needs to be imported in a pandas DataFrame, where rows will be nodes of the network, and columns will be features (or characteristics or attributes) of those nodes.
3. **Data cleaning.**
   This step varies a lot from projects to projects.
   In the context of the course, it will mostly consist in reducing the size of the network so that it can be processed in a reasonable amount of time.
   The less packaged the raw data, the more cleaning will be necessary.
4. **Network creation.**
   The network structure may either be (i) given to you as an adjacency matrix, (ii) given to you as an edge list, or (iii) inferred from raw data.

While those steps are necessary for every project, the amount of pre-processing will however vary.
If the project requires raw data to be collected or the network to be created, that will be indicated in the project description.
So if you're a beginner and don't feel confident, choose a project that requires little pre-processing.
If you feel confident, be adventurous!
Keep in mind that the amount of work generally trades with flexibility: well packaged data usually serves a single task and may restrict your creativity.

## Proposed datasets

* [Free Music Archive](#free-music-archive)
* [US Senators](#us-senators)
* [Wikipedia](#wikipedia)
* [Researchers on Twitter](#researchers-on-twitter)
* [Scientific co-Authorship](#scientific-co-authorship)
* [Spammers on Social Networks](#spammers-on-social-networks)
* [Terrorist Attacks and Relations](#terrorist-attacks-and-relations)
* [IMDb Films and Crew](#imdb-films-and-crew)
* [Flight Routes](#flight-routes)
* [Recipes 1M](#recipes-1m)
* [Genetics](#genetics)
* [Movielens 100k](#movielens-100k)

In addition to the above list, look at [past NTDS projects](#past-projects).
We also encourage teams to work on their own data and ideas.
That is especially relevant to PhD students who want to apply the knowledge acquired in this course to their own problems.
The network can either exist in the data, either be constructed from features.
Look at the below descriptions for examples and discuss with the TAs for guidance.

## Free Music Archive
By Michaël

The [Free Music Archive](http://freemusicarchive.org/) (FMA) is a free and open library directed by [WFMU](https://wfmu.org/), the longest-running freeform radio station in the United States.
Inspired by [Creative Commons](https://creativecommons.org/) and the open-source software movement, the FMA provides a platform for curators, artists, and listeners to harness the potential of music sharing.
The website provides a large catalog of artists and tracks, hand-picked by established audio curators. Each track is legally free to download as artists decided to release their works under permissive licenses.

The goal of this project is to analyze the content created by an open community.
Through the light of networks, it is possible to examine how music tracks relate to each other.
Does genre structure the music?
Do we observe groups of similar artists?
Can we build a playlist that links two tracks through a smooth transition?
To answer those questions, we will build a similarity graph between music tracks.

The packaged data consists of music tracks with associated metadata.
Metadata exists at the level of tracks (e.g., title, creation date), albums (e.g., track number), and artists (e.g, artist name).
A full-length audio recording is available for each track.
Additionally, a fixed length feature vector (audio descriptors computed from the waveform) describes the track.
Relations between tracks can be studied by constructing a similarity graph.
The similarity graph should at first be computed from audio features only.
Later, motivated students will explore and merge other sources of information, at the level of tracks, albums, or artists.
For the first part of the project (milestones 1 to 4), we recommend students to work with tracks that belong to the Hip-Hop and Rock genres of the dataset "FMA small".
That will create a subset of 2,000 tracks.

It is also feasible to work with other graphs, such as relations between artists or listeners.
The latter requires to scrap the website.
We don't recommend exploring those options before having completed the milestones.

Resources:
* Paper: <https://arxiv.org/abs/1612.01840>
* Code and data: <https://github.com/mdeff/fma>

Projects from NTDS'18:
* [[report][r11], [slides][s11], [code][c11]] Music Genre Recognition
* [[report][r14], [slides][s14], [code][c14]] Smooth Radio: Automatic playlist generation using signal graph processing
* [[report][r30], [slides][s30], [code][c30]] Free Music Alternative Playlists
* [[report][r32], [slides][s32], [code][c32]] Genre Classification: A Transductive, Inductive and Deep Approach
* [[report][r33], [slides][s33], [code][c33]] Friends Will Be Friends: A Network Tour of Musical Friendship
* [[report][r36], [slides][s36], [code][c36]] Transitional playlists for new musical discoveries
* [[report][r52], [slides][s52], [code][c52]] Mood Changing Playlist Generator

|          | Description                                | Amount |
| -------- | ------------------------------------------ | ------:|
| nodes    | audio tracks                               | 25,000 |
| edges    | similarity between tracks                  |    N/A |
| features | audio features pre-extracted from waveform |    518 |
| labels   | musical genre (e.g., Rock, Pop)            |     16 |

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: up to the students
* **Network creation**: needs to be built from features

## US Senators
By Michaël

The goal of this project is to understand the [community structure](https://en.wikipedia.org/wiki/Community_structure) and voting pattern of US senators.
Will we observe a divide between democrats and republicans?
Are there sub-communities or moderate members?
Can we predict what a senator will vote knowing what some senators voted?
To answer those questions, we will build a similarity graph between senators.

For each senator, we know (i) their political party (i.e., republican, democrat, independent), (ii) their voting activity (i.e., what they voted on a list of issues), and (iii) the groups they belong to (e.g., the bills they sponsored, the committees they are member of).
We propose to first build the similarity graph from the votes, i.e., measure the distance between voting vectors.
Going further, similarity might be measured from the other features, such as bill sponsoring or committee membership.

Resources:
* [ProPublica Congress API](https://projects.propublica.org/api-docs/congress-api/)
* [Blog post on using the API](http://www.storybench.org/use-propublicas-congress-api-see-senators-stand-issues/)

Projects from NTDS'18:
* [[report][r02], [slides][s02], [code][c02]] Learning US Senate voting behavior from bill sponsorship profiles
* [[report][r07], [slides][s07], [code][c07]] Vote prediction of US Senators from graph properties
* [[report][r18], [slides][s18], [code][c18]] U.S. Senators: A Voting Pattern Study

|          | Description                                              | Amount |
| -------- | -------------------------------------------------------- | ------:|
| nodes    | US senators                                              |   ~100 |
| edges    | similarity between senators                              |    N/A |
| features | votes, bill sponsoring, committee membership, statements |    N/A |
| labels   | political party: democrat, republican, independent       |      3 |

* **Data acquisition**: need to be collected from a web API
* **Requires down-sampling**: no
* **Network creation**: needs to be built from features

## Wikipedia
By Benjamin

Wikipedia is an enormous source of information visited dayly by millions on users. We can understand more about the human behavior by looking at how it is build and how it is accessed. In this project you will investigate the Wikipedia structure and learn more about our use, as human, of the largest encyclopedia ever.
Pages, with their hyperlinks, can be seen as a network, connecting related or similar pages. We will use graph algorithms taught in the course to analyze the graph and gather relevant pages together. Label propagation and community detection will help to group and categorize pages.
In a second step, the number of visits per page (for one month) will be added to analyze the popularity of the articles and check if it influences the popularity of the neighbor pages. The project is open and students can also have access to the evolution in time of the number of visits (visits per hour or per day). Depending on the students progress and motivation, the time series could be analyzed to get interesting information on Wikipedia.

There will be two steps in the project. In the first part, the teams will investigate a small dataset in order to focus on the graph techniques and not spend too much time on the preprocessing and handling of the data. we will use the dataset available here:
[SNAP repository](https://snap.stanford.edu/data/wikispeedia.html)
The file of interest is the path and graph file: wikispeedia_paths-and-graph.tar.gz
The archive provides the articles titles (articles.tsv), their categories (categories.tsv) and the hyperlinks connecting the pages (links.tsv).
The first goal will be to create the graph of articles from the data and study it (apply the techniques learned during the course).

In the second step, to allow more freedom and creativity, the students will have access to a graph database where the full wikipedia graph has been stored, along with categories (work in progress within the LTS2 lab, do not look for it on the internet). In addition, the number visits per hour will be available (for one month). Since the graph is enormous (14 millions articles for the english Wikipedia), the goal for the teams will be to focus on a few categories (that they choose freely) and investigate this smaller subgraph. They will have the possibility to answer questions such as how the categories are connected, what are the central articles within categories, what are the articles that bridge categories... Looking at the number of visits, can we detect particular events that triggered an increase in the number of visits? Which pages are involved? It should also be possible to study the graph of articles for different languages and compare the differences.

Dataset:

Wikipedia dump + Wikipedia data on the number of visits per pages

Resources:
* <https://en.wikipedia.org/wiki/Wikipedia:Database_download>
* <https://dumps.wikimedia.org/other/pagecounts-ez>

Projects from NTDS'18:
* [[report][r09], [slides][s09], [code][c09]] A Network Analysis of the 2018 FIFA World Cup
* [[report][r13], [slides][s13], [code][c13]] Conversation starter using Wikipedia
* [[report][r23], [slides][s23], [code][c23]] Minipedia
* [[report][r24], [slides][s24], [code][c24]] Wikipedia Analysis Using Keyword Based Graphs
* [[report][r37], [slides][s37], [code][c37]] A Wikipedia Tour of Death — or how University College Boat Club became popular

A reduced dataset, extracted from the links above, will be provided to the students.

|          | Description                                |  Amount |
| -------- | ------------------------------------------ | -------:|
| nodes    | Wikipedia pages                            | ~10,000 |
| edges    | hyperlinks                                 |     N/A |
| features | number of visits for one month             |       1 |
| labels   | category                                   |     3-5 |

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: no
* **Network creation**: given

## Researchers on Twitter
by Ersi

The goal of this project is to analyze the interactions of a sub-network of Twitter. The Twitter accounts in this project are Computer Science reasearchers or other accounts "related" to Computer Science.
The [dataset](https://github.com/l3s/twitter-researcher) used consists of the activity of 52678 Twitter users. Of those 170 are Twitter screen names of 98 Computer Science Conferences. These 170 Twitter accounts are set as seeds and more Twitter nodes have been collected if they are i) following a seed or ii) being followed by a seed or iii) have re-tweeted a seed's tweet. Out of the 52678 Twitter users the 9191 are verified to be researchers (they have been matched to a DBLP author profile). 22 features are given for each Twitter user, including for instance a boolean feature demonstrating if the bio description includes words that are usually being used to describe researchers. You can find a detailed description of the data in [this paper](https://dl.acm.org/citation.cfm?doid=2615569.2615676)

|          | Description                                                | Amount |
| -------- | ---------------------------------------------------------- | ------:|
| nodes    | Twitter accounts                                           | 52,678 |
| edges    | similarity (or connection) between Twitter accounts        |    N/A |
| features | numerical and boolean features describing Twitter accounts |     22 |
| labels   | researcher or non-researcher (noisy label)                 |      2 |

* **Data acquisition**: already collected and packaged (load tsv files). Some data cleaning will be needed.
* **Requires down-sampling**: up to the students
* **Network creation**: If you chose to create a similarity graph between the Twitter users, it needs to be built from features. If you chose to build a graph with the connections between users, you must collect information using the Twitter API (Tweepy). As this can be time consuming, we recommend to build a feature graph for the milestones and to explore the connections graph at the last part of the course. Keep in mind that you might need to build different feature graphs for the different milestones. Also, keep in mind that the labels for this project are noisy. They are the results of the classification of [the paper](https://dl.acm.org/citation.cfm?doid=2615569.2615676) mentioned before.

## Scientific co-Authorship
by Ersi

This project aims to explore the co-authorship behaviour of scientific authors.
The [dataset](https://perso.liris.cnrs.fr/marc.plantevit/doku/doku.php?id=data_sets) is a co-authorship graph built from the DBLP digital library. Each vertex represents an author that has published at least one paper in one of the major conferences and journals of the Data Mining and Database communities between January 1990 and February 2011. Each edge links two authors who co-authored at least one paper (no matter the conference or journal). The vertex properties are the number of publications in each of the 29 selected conferences or journals and 9 topological properties (Degree Cent., Closeness Cent., Betweenness Cent., EigenVector Cent., PageRank, Clustering Coeff., Size of Max. Quasi-Clique, Number of Quasi-Cliques, Size of Community).

|          | Description                                                    |  Amount |
| -------- | -------------------------------------------------------------- | -------:|
| nodes    | scientific authors                                             |  42,252 |
| edges    | authors are linked if they wrote a paper together              | 210,320 |
| features | number of publications in conferences and topological features |      38 |
| labels   | N/A                                                            |     N/A |

* **Data acquisition**: already collected and packaged (load txt files)
* **Requires down-sampling**: up to the students
* **Network creation**: The connections between the nodes are already provided.

Remark 1: There are no labels given for the nodes in this dataset. You can chose as your labels two subsets of the conferences (e.g., KDD and AAAI).

Remark 2: The creator of this dataset has agreed to provide the data for this project. However, they will be given to you through a private channel and you should not re-distribute it.

## Spammers on Social Networks
by Eda

The dataset contains 5.6 million users, which are described by 4 features; "user id", "gender", "age group", "spammer label". There are 7 different type of relations between the users indicating the action between them such as profile view, message, poke, etc., which may lead to 7 different directed graph. In total, there are 858 million link between the users. The original task associated with this dataset is to identify the spammers based on their features and links in the network.

Since this dataset is very big, it requires subsampling even during the loading of the data and cleaning the network accordingly. We warn the students that the size of the dataset add more difficulties (for example you can't create a 5.6x5.6 million adjacency matrix). So be sure you can make a smaller, meaningful subset for the project if you choose it.

Resources:
* <https://linqs.soe.ucsc.edu/node/236>
* <https://linqs-data.soe.ucsc.edu/public/social_spammer>
* Paper: <http://www.cs.umd.edu/~shobeir/papers/fakhraei_kdd_2015.pdf>
* Code: <https://github.com/shobeir/fakhraei_kdd2015>
* Data: <https://linqs-data.soe.ucsc.edu/public/social_spammer/usersdata.csv.gz>, <https://linqs-data.soe.ucsc.edu/public/social_spammer/relations.csv.gz>

Projects from NTDS'18:
* [[report][r20], [slides][s20], [code][c20]] Spammer… Catch me if you can
* [[report][r50], [slides][s50], [code][c50]] Identifying Spammers on Social Networks

|          | Description                                                   |      Amount |
| -------- | ------------------------------------------------------------- | -----------:|
| nodes    | users of tagged.com                                           |   5,607,447 |
| edges    | action between users: includes a timestamp and one of 7 types | 858,247,099 |
| features | sex, timePassedValidation, ageGroup                           |           3 |
| labels   | spammer or not spammer                                        |           2 |

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: yes
* **Network creation**: network is given as a list of edges

## Terrorist Attacks and Relations
by Eda

The first dataset consists of 1293 terrorist attacks (nodes), each of which is assigned to one of 6 labels indicating the type of the attack. Each attack is described by a 0/1-valued vector of attributes whose entries indicate the absence/presence of a feature. There are a total of 106 distinct features. The files in the dataset can be used to create two distinct graphs. In one of them edges of the graph connect the colocated attacks. On the other one, edges connect co-located terrorist attacks performed by the same terrorist organization.

The second dataset is designed for the classification of the relationships between the terrorists. The dataset contains 851 relations (aka; nodes of the graph). Each node is assigned to least one label (multiple labeling is also possible) among 4 labels; "Colleague", "Congregate", "Contact", "Family", and is described with 0/1 valued feature vector indicating absence/presence of the attributes, which are 1224 in total. There are 8592 edges on the graph, which connects the nodes involving the same terrorist group.
As the goal is the classification of links, we will here build the [line graph](https://en.wikipedia.org/wiki/Line_graph) of the social network between terrorists.
That is, instead of having terrorists as nodes and relationships between them as edges, relationships will be nodes and terrorists will be edges.

We warn the students that the 106 features given in this dataset are undocumented so that it can not be used for interpreting the data or doing anything meaningful. The students who choose this project will have to increase the dataset by collecting data from other source of information about terrorism.

Resources:
* <https://linqs.soe.ucsc.edu/node/236>
* <http://www.cs.umd.edu/~sen/lbc-proj/LBC.html>
* Paper: <https://pdfs.semanticscholar.org/c047/f91ece3e9ec74bf42b8f69f375e27498a54a.pdf>
* Data: <https://linqs-data.soe.ucsc.edu/public/lbc/TerrorAttack.tgz>
* Data: <https://linqs-data.soe.ucsc.edu/public/lbc/TerroristRel.tgz>

Projects from NTDS'18:
* [[report][r19], [slides][s19], [code][c19]] A Data Study of Terrorism and its Tendencies
* [[report][r21], [slides][s21], [code][c21]] Exposing the True Terrorist Network
* [[report][r25], [slides][s25], [code][c25]] Finding the Authors of a Terrorist Attack
* [[report][r27], [slides][s27], [code][c27]] How to beat terrorism efficiently: identification of set of key players in terrorist networks
* [[report][r29], [slides][s29], [code][c29]] Predicting Terror Attacks — A Data Story
* [[report][r34], [slides][s34], [code][c34]] Predicting the nature of terrorist attacks
* [[report][r54], [slides][s54], [code][c54]] Fight Against Terrorism

|          | Description                                                                  | Amount |
| -------- | ---------------------------------------------------------------------------- | ------:|
| nodes    | relationships                                                                |    851 |
| edges    | terrorists                                                                   |  8,592 |
| features | 0-1 vector of attribute values                                               |  1,224 |
| labels   | type of relationship (non exclusive): colleague, congregate, contact, family |      4 |

|          | Description                                                     | Amount |
| -------- | --------------------------------------------------------------- | ------:|
| nodes    | terrorist attacks                                               |  1,293 |
| edges    | connect co-located attacks                                      |  3,172 |
| features | 0-1 vector of attribute values                                  |    106 |
| labels   | kind of attack: arson, bombing, kidnapping, weapon, nbcr, other |      6 |

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: no
* **Network creation**: network is given as a list of edges

## IMDb Films and Crew
By Rodrigo

Resources:
* <https://www.imdb.com/interfaces>
* <https://www.kaggle.com/tmdb/tmdb-movie-metadata/home>

Projects from NTDS'18:
* [[report][r01], [slides][s01], [code][c01]] A Network Analysis of Movie Popularity
* [[report][r04], [slides][s04], [code][c04]] Evolution of the movie industry
* [[report][r10], [slides][s10], [code][c10]] History of Movie Success through GSP
* [[report][r15], [slides][s15], [code][c15]] Movie Grossing Success Prediction with Convolutional Neural Networks on Graphs
* [[report][r16], [slides][s16], [code][c16]] How to invest in movies?
* [[report][r17], [slides][s17], [code][c17]] A Netflix Tour of Data Science — Film suggestion by diffusion on graphs
* [[report][r31], [slides][s31], [code][c31], [proposal][p31]] Feminism in Hollywood
* [[report][r40], [slides][s40], [code][c40]] Can we estimate the earnings of a movie?
* [[report][r49], [slides][s49], [code][c49]] A Network Tour of Millenial Movies

The IMDb datasets contain information such as crew, rating, and genre for every entertainment product in its database. The Kaggle dataset linked above is a smaller, but similar dataset, and could be used instead of the IMDb one, which is much larger. The goal of this project is to analyze this database in graph form, and attempt to recover missing information from data on cast/crew co-appearance in movies. The graphical analysis requires network creation, for which two possible paths are possible, according to which instances one wishes to consider as the nodes of the network.

The first approach could be to construct a social network of cast/crew members, where the edges are weighted according to co-appearance For example, actor_1 becomes strongly connected to actor_2 if they have appeared in a lot of movies together. The edges of the graph could be weighted according to a count on the number of entertainment products in which the two corresponding people participated together. We can take as a signal on this constructed graph the aggregate ratings of movies each person has participated in.

|          | Description                            |                          Amount |
| -------- | -------------------------------------- | ------------------------------: |
| nodes    | cast/crew                              | millions (IMDb), ~8500 (Kaggle) |
| edges    | co-apearance in movies/TV/etc.         |                  O(10) per node |
| features | ratings of movies taken part in        |                  O(10) per node |
| labels   | movie genre                            |       unknown (IMDb), 3 (Kaggle)|

A second approach could be to create a movie-network, in which movies are strongly connected if they share a lot of crew/cast members (or some other similarity measure combining this and genres, running times, release years, etc.). There are more options for the signal the students could consider on this graph, as they could use either the movie ratings, or the genre labels.

|          | Description                                           |                          Amount |
| -------- | ----------------------------------------------------- | ------------------------------: |
| nodes    | movies                                                | millions (IMDb), ~5000 (Kaggle) |
| edges    | count of common cast/crew + other feature similarity. |                  O(10) per node |
| features | average rating                                        |                               1 |
| labels   | movie genre                                           |      unknown (IMDb), 3 (Kaggle) |

For the extra work, there is plenty of extra information. For instance, the students could try to predict the revenue of movies by potentially including extra metadata. Note however that the number of instances in the original dataset is of the order of **millions**, so a smaller subset of those should be used.

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: yes if using the original datasets from IMDb, no if using the subsampled dataset from Kaggle
* **Network creation**: needs to be built from features

## Flight Routes
By Rodrigo

Resources:
* <https://openflights.org/data.html#route>
* <https://openflights.org/data.html>

Projects from NTDS'18:
* [[report][r03], [slides][s03], [code][c03]] Retrieving the continent labels from the air routes structure
* [[report][r05], [slides][s05], [code][c05]] A network tour to flight delay in the US
* [[report][r06], [slides][s06], [code][c06]] Flight network and airline alliances
* [[report][r08], [slides][s08], [code][c08]] Spreading disease through the air
* [[report][r12], [slides][s12], [code][c12]] Finding Continents from a Flight Routes Network
* [[report][r22], [slides][s22], [code][c22]] Small Components' Analysis and Flight Delay Prediction
* [[report][r28], [slides][s28], [code][c28]] A Network Topology Analysis of the Airline Industry
* [[report][r38], [slides][s38], [code][c38]] Tempering the Spread of Epidemics on Aerial Networks
* [[report][r42], [slides][s42], [code][c42]] Re-balancing flight routes inequalities
* [[report][r47], [slides][s47], [code][c47]] An overviews of intercontinental flight route connections

This OpenFlights/Airline Route Mapper Route Database contains 67,663 routes (EDGES) between 3,321 airports (NODES) on 548 airlines spanning the globe.

The construction of the graph is facilitated by the source and destination airports of each flight, which gives essentially an edge list for the airport graph. Students could complement the graph construction by providing weigths to the edges, proportional to the number of flights connecting the corresponding pair of airports. The visualization of the graph embedded on the globe can be achieved by using the supplemented data in https://openflights.org/data.html, which contains, among others, information on latitute/longitude of each airport. A potential goal of the extra work could then be comparing the embedding produced by the Laplacian eigenmaps algorithm seen in the course and the "natural" embedding given by the terrestrial coordinates. The most sensitive part of the project (which could be examined in the extra work) would be to find a label signal on the graph that could be recovered via a label propagation algorithm on the graph. In principle, the average number of stops of flights leaving each airport could fulfill this purpose, but it remains a metter of study whether a subsampled version of this information can be recovered from the topological information of the graph alone or not.

|          | Description                                 | Amount |
| -------- | ------------------------------------------- | -----: |
| nodes    | airports                                    |  3,321 |
| edges    | count of flights connecting airports        | 67,663 |
| features | average number of stops of outbound flights |      1 |
| labels   | N/A                                         |    N/A |

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: no
* **Network creation**: network is essentially given (list of edges)

## Recipes 1M
By Nicolas

Resources:
* <http://pic2recipe.csail.mit.edu/>
* <http://im2recipe.csail.mit.edu/dataset/download/> (requires free registration prior download)

This database contains ca. 1 million cooking recipes retrieved from several websites, along with one or more images for each recipe (13 million images available).
Its original use is to train models to perform a "im2recipe" (i.e. get a recipe instructins from an image).
For every recipe in this dataset, you can retrieve the full-text of instructions, ingredients contained in the file available under the "layers" link (and after you unpack the file, in the "layer1.json" file).
For each ingredient line inside a recipe, the name of the ingredient has been extracted ("ingredient detection" link).
Ingredient name detection from text is a non-trivial task, expect the results to be noisy.
Quantity detection has not been performed, but might be an interesting feature to study (requires extra work).
If you intend to work with images, they require more than 100 GB of download and a matching storage space, be careful !

You can, for instance, construct an ingredient graph (linking ingredients when they appear simultaneously in a recipe).

|          | Description                                 |          Amount |
| -------- | ------------------------------------------- | --------------: |
| nodes    | ingredients                                 |           18253 |
| edges    | connect co-appearing ingredients            |  O(10) per node |
| features | recipes                                     |               1 |
| labels   | N/A                                         |             N/A |

Another approach could be to create a graph from recipes having several ingredients in common.
Given the size of the dataset, it might be a good idea to try out a smaller subset of the dataset, for instance by filtering recipes that contain a particular ingredient (e.g. 'beef', 'vanilla', etc.).
In order for the students to get started more easily, [two smaller subsets](https://drive.switch.ch/index.php/s/fjjqqaRznah6PKp) (with ca. 10k and 23k recipes) are supplied.

|          | Description                                 |                         Amount |
| -------- | ------------------------------------------- | -----------------------------: |
| nodes    | recipes                                     |                             1M |
| edges    | connect recipes with common ingredients     | depends how the graph is built |
| features | images / ingredient quantities              |                           1-10 |
| labels   | N/A                                         |                            N/A |

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: yes
* **Network creation**: to be created from co-appearing ingredients or from recipes

## Genetics
By Benjamin

This dataset contains genes, protein expressions and phenotypes of a "family" of mice. It is a subset of the open dataset available at [genenetwork.org](http://www.genenetwork.org/). The goal is to explore the data using graphs and discover connections between genes, protein expression and / or phenotypes. This data has been collected by different labs all over the world during several decades. The LISP from EPFL is part of the group. More details about the project and dataset can be found on this [EPFL mediacom article](https://actu.epfl.ch/news/a-big-data-tool-begins-new-era-for-biology-and-per/).

This dataset is a collection of matrices. Each column is a single BXD strain (a mouse) whose genome is a unique combination of the C57BL/6J and DBA/2J parental strains. They have been saved as csv files (with extention 'txt').
The `genotype_BXD.txt` file is a binary matrix that describes the contribution of each of the parental strains for a list of selected genes (rows). Each row of the genotype data indicates whether a certain position in the genome is inherited from the C57BL/6J or DBA/2J parent.
Phenotype data contained in `Phenotype.txt` are also matrices indicating the values of each phenotype for each strain.
In addition, multiomic molecular phenotypes from different mouse organs are represented as one matrix per organ (e.g. brain, bone, muscle, liver...), in the folder `expression_data`.

It is important to note that protein or phenotype information is not available for all the mice. Depending on the research team gathering the data or the protocols, only subset of mice have been tested for each phenotype, or different organs have been analyzed. Hence, the combination of several matrices will result in missing entries.
These missing entries, along with the variety of the data, are a real challenge for a data science approach, but mimic the real life situation encountered with human medical records.

The dataset for the NTDS project can be found [here](https://drive.switch.ch/index.php/s/mtQ2F0dYc7dHOtQ). The students are expected to:
* use the different matrices of data to build one or more graphs (for example a graph of mice),
* explore these graphs,
* associate values to the nodes of the graphs using the other matrices,
* apply graph signal processing approaches,
* discover new relations between the genome, protein expressions in tissues and phenotypes (optional but that would be great!)

Resources:
* [EPFL mediacom article](https://actu.epfl.ch/news/a-big-data-tool-begins-new-era-for-biology-and-per/)
* [Info on the BXD mice](https://www.biorxiv.org/content/10.1101/672097v3.full)
* [dataset official Website](http://www.genenetwork.org/)
* [Dataset link](https://drive.switch.ch/index.php/s/mtQ2F0dYc7dHOtQ)

|          | Description                                                  |         Amount |
| -------- | ------------------------------------------------------------ | -------------: |
| nodes    | mice                                                         |      100 - 200 |
| edges    | similar genes, protein expressions, or phenotypes            | O(10) per node |
| features | genes, protein expressions in tissues, or phenotypes         |          1000s |
| labels   | depends: a particular gene, phenotype, or protein expression |            N/A |

## Movielens 100k
By Clément

Movielens is a personalized movie recommendation system. Several datasets have been built using this database, the smallest being Movielens 100k. It contains 100,000 ratings from 1000 users on 1700 movies. Various information is available about the users (Age, Gender, Occupation, Zip code) and the movies (Release date, genre). Given that the movie title are available, additional features can be added as well. Two graphs can be built out of this dataset, and they can be connected using the ratings.

The main purpose of this data is to build a recommender system, which can be formulated as a semi-supervised learning problem: given a user, can you predict the ratings that he/she will give to a new movie? Graph neural networks can be used for this purpose, but other graph based approaches can be explored as well.

Resources:
* [Data](<https://grouplens.org/datasets/movielens/>)
* Papers using graph neural networks:
  * [Geometric Matrix Completion with Recurrent Multi-Graph Neural Networks](https://arxiv.org/abs/1704.06803)
  * [Graph Convolutional Matrix Completion](https://arxiv.org/abs/1706.02263)

| Users graph | Description                       |                         Amount |
| ----------- | --------------------------------- | -----------------------------: |
| nodes       | users                             |                           1000 |
| edges       | similar features                  | depends how the graph is built |
| features    | age, gender, occupation, zip code |                              4 |
| labels      | ratings of the movies             |                           100k |

| Movies graph | Description               |                         Amount |
| ------------ | ------------------------- | -----------------------------: |
| nodes        | movies                    |                           1700 |
| edges        | similar features          | depends how the graph is built |
| features     | name, release date, genre |                  2 + 19 genres |
| labels       | ratings given by users    |                           100k |

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: no
* **Network creation**: needs to be built from features

## Past projects

Projects from NTDS'18:
* [[report][r01], [slides][s01], [code][c01]] A Network Analysis of Movie Popularity
* [[report][r02], [slides][s02], [code][c02]] Learning US Senate voting behavior from bill sponsorship profiles
* [[report][r03], [slides][s03], [code][c03]] Retrieving the continent labels from the air routes structure
* [[report][r04], [slides][s04], [code][c04]] Evolution of the movie industry
* [[report][r05], [slides][s05], [code][c05]] A network tour to flight delay in the US
* [[report][r06], [slides][s06], [code][c06]] Flight network and airline alliances
* [[report][r07], [slides][s07], [code][c07]] Vote prediction of US Senators from graph properties
* [[report][r08], [slides][s08], [code][c08]] Spreading disease through the air
* [[report][r09], [slides][s09], [code][c09]] A Network Analysis of the 2018 FIFA World Cup
* [[report][r10], [slides][s10], [code][c10]] History of Movie Success through GSP
* [[report][r11], [slides][s11], [code][c11]] Music Genre Recognition
* [[report][r12], [slides][s12], [code][c12]] Finding Continents from a Flight Routes Network
* [[report][r13], [slides][s13], [code][c13]] Conversation starter using Wikipedia
* [[report][r14], [slides][s14], [code][c14]] Smooth Radio: Automatic playlist generation using signal graph processing
* [[report][r15], [slides][s15], [code][c15]] Movie Grossing Success Prediction with Convolutional Neural Networks on Graphs
* [[report][r16], [slides][s16], [code][c16]] How to invest in movies?
* [[report][r17], [slides][s17], [code][c17]] A Netflix Tour of Data Science — Film suggestion by diffusion on graphs
* [[report][r18], [slides][s18], [code][c18]] U.S. Senators: A Voting Pattern Study
* [[report][r19], [slides][s19], [code][c19]] A Data Study of Terrorism and its Tendencies
* [[report][r20], [slides][s20], [code][c20]] Spammer… Catch me if you can
* [[report][r21], [slides][s21], [code][c21]] Exposing the True Terrorist Network
* [[report][r22], [slides][s22], [code][c22]] Small Components' Analysis and Flight Delay Prediction
* [[report][r23], [slides][s23], [code][c23]] Minipedia
* [[report][r24], [slides][s24], [code][c24]] Wikipedia Analysis Using Keyword Based Graphs
* [[report][r25], [slides][s25], [code][c25]] Finding the Authors of a Terrorist Attack
* [[report][r27], [slides][s27], [code][c27]] How to beat terrorism efficiently: identification of set of key players in terrorist networks
* [[report][r28], [slides][s28], [code][c28]] A Network Topology Analysis of the Airline Industry
* [[report][r29], [slides][s29], [code][c29]] Predicting Terror Attacks — A Data Story
* [[report][r30], [slides][s30], [code][c30]] Free Music Alternative Playlists
* [[report][r31], [slides][s31], [code][c31], [proposal][p31]] Feminism in Hollywood
* [[report][r32], [slides][s32], [code][c32]] Genre Classification: A Transductive, Inductive and Deep Approach
* [[report][r33], [slides][s33], [code][c33]] Friends Will Be Friends: A Network Tour of Musical Friendship
* [[report][r34], [slides][s34], [code][c34]] Predicting the nature of terrorist attacks
* [[report][r36], [slides][s36], [code][c36]] Transitional playlists for new musical discoveries
* [[report][r37], [slides][s37], [code][c37]] A Wikipedia Tour of Death — or how University College Boat Club became popular
* [[report][r38], [slides][s38], [code][c38]] Tempering the Spread of Epidemics on Aerial Networks
* [[report][r40], [slides][s40], [code][c40]] Can we estimate the earnings of a movie?
* [[report][r42], [slides][s42], [code][c42]] Re-balancing flight routes inequalities
* [[report][r44], [slides][s44], [code][c44], [proposal][p44]] Voting patterns in the Swiss National Council
* [[report][r47], [slides][s47], [code][c47]] An overviews of intercontinental flight route connections
* [[report][r49], [slides][s49], [code][c49]] A Network Tour of Millenial Movies
* [[report][r50], [slides][s50], [code][c50]] Identifying Spammers on Social Networks
* [[report][r51], [slides][s51], [code][c51], [proposal][p51]] An exploratory study on the brain dysconnectome
* [[report][r52], [slides][s52], [code][c52]] Mood Changing Playlist Generator
* [[report][r54], [slides][s54], [code][c54]] Fight Against Terrorism

Projects from NTDS'17:
* [[proposal][01p], [analysis][01r], [slides][01s]] American Basketball Players
* [[proposal][02p], [analysis][02r], [slides][02s]] Graph-based Nutrition Guide
* [[proposal][03p], [analysis][03r], [slides][03s]] What Impacts the Success of a Movie?
* [[proposal][04p], [analysis][04r], [slides][04s]] Exploring the Crunchbase Dataset to Detect High Potential Startups
* [[proposal][05p], [analysis][05r], [slides][05s]] Beer Suggester
* [[proposal][06p], [analysis][06r], [slides][06s]] Swiss Political Survey
* [[proposal][07p], [analysis][07r], [slides][07s]] A StackOverflow Recommender System
* [[proposal][08p], [analysis][08r], [slides][08s]] Analysis of World Development Indicators as Predictors
* [[proposal][09p], [analysis][09r], [slides][09s]] Satellites Characterization – Clustering using Orbital Characteristics
* [[proposal][10p], [analysis][10r], [slides][10s]] Amazon Electronic Products – Network Analysis
* [[proposal][11p], [analysis][11r], [slides][11s]] GSP on the Digital Reconstruction of the Brain
* [[proposal][12p], [analysis][12r], [slides][12s]] Movie Recommendation
* [[proposal][13p], [analysis][13r], [slides][13s]] GraphLang
* [[proposal][14p], [analysis][14r], [slides][14s]] Buda + Pest = Budapest
* [[proposal][15p], [analysis][15r], [slides][15s]] Manifold Learning of Face Data
* [[proposal][16p], [analysis][16r], [slides][16s]] A Network Tour of the Tunisian and Egyptian Springs
* [[proposal][17p], [analysis][17r], [slides][17s]] StackOverflow Survey
* [[proposal][18p], [analysis][18r], [slides][18s]] Speech Recognition Challenge
* [[proposal][19p], [analysis][19r], [slides][19s]] Analysis of the Elite Football Transfer Market
* [[proposal][20p], [analysis][20r], [slides][20s]] Titanic
* [[proposal][21p], [analysis][21r], [slides][21s]] This is My Jam
* [[proposal][22p], [analysis][22r], [slides][22s]] A Network Tour of StackOverflow
* [[proposal][23p], [analysis][23r], [slides][23s]] Course Suggester
* [[proposal][24p], [analysis][24r], [slides][24s]] Spectral Analysis of 5000 Movies Network
* [[proposal][25p], [analysis][25r], [slides][25s]] Community Detection on the Wikipedia Hyperlink Graph
* [[proposal][26p], [analysis][26r], [slides][26s]] 3D Meshes of Facial Expression
* [[proposal][27p], [analysis][27r], [slides][27s]] Terrorist Attacks
* [[proposal][28p], [analysis][28r], [slides][28s]] Community Detection and Labelling in an Instagram Network
* [[proposal][29p], [analysis][29r], [slides][29s]] Graph-based Recommendation for lastFM

[p31]: https://github.com/mdeff/ntds_2018/blob/master/projects/proposals/team_31.pdf
[p44]: https://github.com/mdeff/ntds_2018/blob/master/projects/proposals/team_44.pdf
[p51]: https://github.com/mdeff/ntds_2018/blob/master/projects/proposals/team_51.pdf

[r01]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_01.pdf
[r02]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_02.pdf
[r03]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_03.pdf
[r04]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_04.pdf
[r05]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_05.pdf
[r06]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_06.pdf
[r07]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_07.pdf
[r08]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_08.pdf
[r09]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_09.pdf
[r10]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_10.pdf
[r11]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_11.pdf
[r12]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_12.pdf
[r13]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_13.pdf
[r14]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_14.pdf
[r15]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_15.pdf
[r16]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_16.pdf
[r17]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_17.pdf
[r18]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_18.pdf
[r19]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_19.pdf
[r20]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_20.pdf
[r21]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_21.pdf
[r22]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_22.pdf
[r23]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_23.pdf
[r24]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_24.pdf
[r25]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_25.pdf
[r27]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_27.pdf
[r28]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_28.pdf
[r29]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_29.pdf
[r30]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_30.pdf
[r31]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_31.pdf
[r32]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_32.pdf
[r33]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_33.pdf
[r34]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_34.pdf
[r36]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_36.pdf
[r37]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_37.pdf
[r38]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_38.pdf
[r40]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_40.pdf
[r42]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_42.pdf
[r44]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_44.pdf
[r47]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_47.pdf
[r49]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_49.pdf
[r50]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_50.pdf
[r51]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_51.pdf
[r52]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_52.pdf
[r54]: https://github.com/mdeff/ntds_2018/blob/master/projects/reports/team_54.pdf

[s01]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_01.pdf
[s02]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_02.pdf
[s03]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_03.pdf
[s04]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_04.pdf
[s05]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_05.pdf
[s06]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_06.pdf
[s07]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_07.pdf
[s08]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_08.pdf
[s09]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_09.pdf
[s10]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_10.pdf
[s11]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_11.pdf
[s12]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_12.pdf
[s13]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_13.pdf
[s14]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_14.pdf
[s15]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_15.pdf
[s16]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_16.pdf
[s17]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_17.pdf
[s18]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_18.pdf
[s19]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_19.pdf
[s20]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_20.pdf
[s21]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_21.pdf
[s22]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_22.pdf
[s23]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_23.pdf
[s24]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_24.pdf
[s25]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_25.pdf
[s27]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_27.pdf
[s28]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_28.pdf
[s29]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_29.pdf
[s30]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_30.pdf
[s31]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_31.pdf
[s32]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_32.pdf
[s33]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_33.pdf
[s34]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_34.pdf
[s36]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_36.pdf
[s37]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_37.pdf
[s38]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_38.pdf
[s40]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_40.pdf
[s42]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_42.pdf
[s44]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_44.pdf
[s47]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_47.pdf
[s49]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_49.pdf
[s50]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_50.pdf
[s51]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_51.pdf
[s52]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_52.pdf
[s54]: https://github.com/mdeff/ntds_2018/blob/master/projects/slides/team_54.pdf

[c01]: https://github.com/illorens/Project_NTDS
[c02]: https://github.com/roman-bachmann/US-Senators
[c03]: https://github.com/AmauV/NTDS
[c04]: https://github.com/swouf/ntds_IMDb_team4
[c05]: https://github.com/yf0726/ntds_project
[c06]: https://github.com/nicolasFontbonne/Project_ntds
[c07]: https://github.com/magoncal/NTDS_Project
[c08]: https://github.com/dsalathe/group_ntds
[c09]: https://github.com/ProjectNTDS/Network_World_Cup_Analysis
[c10]: https://github.com/hugofluhr/Team10_ntds_2018
[c11]: https://github.com/angomez/ntds
[c12]: https://github.com/franckdess/NTDS_Project
[c13]: https://github.com/okhofsk/NTDS_Wikipedia
[c14]: https://github.com/padesplaces/ntds_project
[c15]: https://github.com/mcherep/ntds-epfl
[c16]: https://github.com/GentleDell/IMDb_movie_analysis
[c17]: https://github.com/PierreFourcade/A-Netflix-Tour-of-Data-Science---Film-suggestion-by-diffusion-on-graphs
[c18]: https://github.com/lkieliger/US-Senators
[c19]: https://github.com/AminMekacher/NTDS_Team19
[c20]: https://github.com/mfendri2/NTDS_Project_Team20
[c21]: https://github.com/sinyil/ntds_2018_Final_Project
[c22]: https://github.com/sami2310/NTDS_Project_team22
[c23]: https://github.com/Ivo-A/Team23_Wikipedia
[c24]: https://github.com/mattminder/wikilinks
[c25]: https://github.com/yusiZou/NTDS_project
[c27]: https://github.com/natbolon/terrorist_network_weaknesses
[c28]: https://github.com/rusucosmin/ntp
[c29]: https://github.com/Axeln78/TerrorAttacksNtds
[c30]: https://github.com/TTimTT/FMAP
[c31]: https://github.com/othmanbck/ntds_project_2018
[c32]: https://github.com/senakicir/ntds_project
[c33]: https://github.com/JCrobe/NTDS19_FWBF
[c34]: https://github.com/coencharles/NTDS_team34
[c36]: https://github.com/Team36-ntds2018/Project_free_music_archives_2018
[c37]: https://github.com/isabelaconstantin/wikinet
[c38]: https://github.com/montalex/NTDS_2018_Final_Project
[c40]: https://github.com/rocari96/NTDS-project
[c42]: https://github.com/VincentCoriou/Re-balancing-flight-routes-inequalities
[c44]: https://github.com/nikolaiorgland/conseil_national
[c47]: https://github.com/FrankSchmutz/NTDS2019FinalProject
[c49]: https://github.com/MilenaFilipovic/NTDS_Project_Team_49
[c50]: https://github.com/ilijagjorgjiev/project_ntds
[c51]: https://github.com/emullier/NTDS_team51_BrainNetworks
[c52]: https://github.com/rezaho/NetworkTour-of-DataScience
[c54]: https://github.com/mouadhhamdi/NTDS_Project

[01p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/basketball_players.pdf
[02p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/nutrition_guide.pdf
[03p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/movie_success.pdf
[04p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/crunchbase_startups.pdf
[05p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/beer_suggester.pdf
[06p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/swiss_politics.pdf
[07p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/stackoverflow_recommendation.pdf
[08p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/countries_development.pdf
[09p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/satellites.pdf
[10p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/amazon_products.pdf
[11p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/brain_network.pdf
[12p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/movie_recommendation.pdf
[13p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/graphlang.pdf
[14p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/road_network.pdf
[15p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/face_manifold.pdf
[16p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/arab_springs.pdf
[17p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/stackoverflow_survey.pdf
[18p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/speech_recognition.pdf
[19p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/football_transfers.pdf
[20p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/titanic.pdf
[21p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/jam.pdf
[22p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/stackoverflow_network.pdf
[23p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/course_suggester.pdf
[24p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/movie_network.pdf
[25p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/wikipedia_hyperlink.pdf
[26p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/facial_expression.pdf
[27p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/terrorist_attacks.pdf
[28p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/instagram_community.pdf
[29p]: https://github.com/mdeff/ntds_2017/blob/master/projects/proposals/lastfm_recommendation.pdf

[01s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/basketball_players.pdf
[02s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/nutrition_guide.pdf
[03s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/movie_success.pdf
[04s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/crunchbase_startups.pdf
[05s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/beer_suggester.pdf
[06s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/swiss_politics.pdf
[07s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/stackoverflow_recommendation.pdf
[08s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/countries_development.pdf
[09s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/satellites.pdf
[10s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/amazon_products.pdf
[11s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/brain_network.pdf
[12s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/movie_recommendation.pdf
[13s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/graphlang.pdf
[14s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/road_network.pdf
[15s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/face_manifold.pdf
[16s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/arab_springs.pdf
[17s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/stackoverflow_survey.pdf
[18s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/speech_recognition.pdf
[19s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/football_transfers.pdf
[20s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/titanic.pdf
[21s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/jam.pdf
[22s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/stackoverflow_network.pdf
[23s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/course_suggester.pdf
[24s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/movie_network.pdf
[25s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/wikipedia_hyperlink.pdf
[26s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/facial_expression.pdf
[27s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/terrorist_attacks.pdf
[28s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/instagram_community.pdf
[29s]: https://github.com/mdeff/ntds_2017/blob/master/projects/slides/lastfm_recommendation.pdf

[01r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/basketball_players
[02r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/nutrition_guide
[03r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/movie_success
[04r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/crunchbase_startups
[05r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/beer_suggester
[06r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/swiss_politics
[07r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/stackoverflow_recommendation
[08r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/countries_development
[09r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/satellites
[10r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/amazon_products
[11r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/brain_network
[12r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/movie_recommendation
[13r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/graphlang
[14r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/road_network
[15r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/face_manifold
[16r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/arab_springs
[17r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/stackoverflow_survey
[18r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/speech_recognition
[19r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/football_transfers
[20r]: https://github.com/zifeo/Titanic
[21r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/jam
[22r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/stackoverflow_network
[23r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/course_suggester
[24r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/movie_network
[25r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/wikipedia_hyperlink
[26r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/facial_expression
[27r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/terrorist_attacks
[28r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/instagram_community
[29r]: https://github.com/mdeff/ntds_2017/blob/master/projects/reports/lastfm_recommendation
