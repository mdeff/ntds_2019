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
* [Citation Network](#citation-network)
* [Terrorist Attacks and Relations](#terrorist-attacks-and-relations)
* [IMDb Films and Crew](#imdb-films-and-crew)
* [Flight Routes](#flight-routes)

In addition to the above list, we allow teams to work on their own data and ideas.
That is especially relevant to PhD students who want to apply the knowledge acquired in this course to their own problems.
Teams that choose this option must submit a project proposal.
The proposal must explain what is the data, where is the network, and what the team wants to do with it.
The network can either exist in the data, either be constructed from features.
Look at the below descriptions and discuss with the TAs for guidance.

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

|          | Description                                                    | Amount  |
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

Since this dataset is very big, it requires subsampling even during the loading the data and cleaning the network accordingly.

Resources:
* <https://linqs.soe.ucsc.edu/node/236>
* <https://linqs-data.soe.ucsc.edu/public/social_spammer>
* Paper: <http://www.cs.umd.edu/~shobeir/papers/fakhraei_kdd_2015.pdf>
* Code: <https://github.com/shobeir/fakhraei_kdd2015>
* Data: <https://linqs-data.soe.ucsc.edu/public/social_spammer/usersdata.csv.gz>, <https://linqs-data.soe.ucsc.edu/public/social_spammer/relations.csv.gz>

|          | Description                                                   |      Amount |
| -------- | ------------------------------------------------------------- | -----------:|
| nodes    | users of tagged.com                                           |   5,607,447 |
| edges    | action between users: includes a timestamp and one of 7 types | 858,247,099 |
| features | sex, timePassedValidation, ageGroup                           |           3 |
| labels   | spammer or not spammer                                        |           2 |

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: yes
* **Network creation**: network is given as a list of edges

## Citation Network
by Eda

CORA citation network is a graph containing 2708 vertices representing papers and 5429 edges representing citations. Each paper is described by a 1433-dimensional bag-of-words feature vector and belongs to seven classes (the field of the study). The feature vectors contain 0/1 values indicating the absence/presence of the corresponding word from the dictionary consisting of 1433 unique words. The asscoiated task with this dataset is usually label prediction.

Resources:
* <https://linqs.soe.ucsc.edu/node/236>
* <https://relational.fit.cvut.cz/dataset/CORA>
* Paper: <http://www.aaai.org/Papers/ICML/2003/ICML03-066.pdf>
* Data: <https://linqs-data.soe.ucsc.edu/public/lbc/cora.tgz>

|          | Description                                     | Amount |
| -------- | ------------------------------------------------| ------:|
| nodes    | scientific publications                         |  2,708 |
| edges    | a paper cites another paper                     |  5,429 |
| features | vector indicating the absence/presence of words |  1,433 |
| labels   | scientific field                                |      7 |

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: no
* **Network creation**: network is given as a list of edges

## Terrorist Attacks and Relations
by Eda

The first dataset consists of 1293 terrorist attacks (nodes), each of which is assigned to one of 6 labels indicating the type of the attack. Each attack is described by a 0/1-valued vector of attributes whose entries indicate the absence/presence of a feature. There are a total of 106 distinct features. The files in the dataset can be used to create two distinct graphs. In one of them edges of the graph connect the colocated attacks. On the other one, edges connect co-located terrorist attacks performed by the same terrorist organization.

The second dataset is designed for the classification of the relationships between the terrorists. The dataset contains 851 relations (aka; nodes of the graph). Each node is assigned to least one label (multiple labeling is also possible) among 4 labels; "Colleague", "Congregate", "Contact", "Family", and is described with 0/1 valued feature vector indicating absence/presence of the attributes, which are 1224 in total. There are 8592 edges on the graph, which connects the nodes involving the same terrorist group.
As the goal is the classification of links, we will here build the [line graph](https://en.wikipedia.org/wiki/Line_graph) of the social network between terrorists.
That is, instead of having terrorists as nodes and relationships between them as edges, relationships will be nodes and terrorists will be edges.

Resources:
* <https://linqs.soe.ucsc.edu/node/236>
* <http://www.cs.umd.edu/~sen/lbc-proj/LBC.html>
* Paper: <https://pdfs.semanticscholar.org/c047/f91ece3e9ec74bf42b8f69f375e27498a54a.pdf>
* Data: <https://linqs-data.soe.ucsc.edu/public/lbc/TerrorAttack.tgz>
* Data: <https://linqs-data.soe.ucsc.edu/public/lbc/TerroristRel.tgz>

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

The IMDb datasets contain information such as crew, rating, and genre for every entertainment product in its database. The Kaggle dataset linked above is a smaller, but similar dataset, and could be used instead of the IMDb one, which is much larger. The goal of this project is to analyze this database in graph form, and attempt to recover missing information from data on cast/crew co-appearance in movies. The graphical analysis requires network creation, for which two possible paths are possible, according to which instances one wishes to consider as the nodes of the network.

The first approach could be to construct a social network of cast/crew members, where the edges are weighted according to co-appearance For example, actor_1 becomes strongly connected to actor_2 if they have appeared in a lot of movies together. The edges of the graph could be weighted according to a count on the number of entertainment products in which the two corresponding people participated together. We can take as a signal on this constructed graph the aggregate ratings of movies each person has participated in. 

|          | Description                            |                               Amount |
| -------- | -------------------------------------- | -----------------------------------: |
| nodes    | cast/crew                              |       millions (IMDb) ~8500 (Kaggle) |
| edges    | co-apearance in movies/TV/etc.         |                       O(10) per node |
| features | ratings of movies taken part in        |                       O(10) per node |
| labels   | movie genre                            |             unknown (IMDb) 3 (Kaggle)|

A second approach could be to create a movie-network, in which movies are strongly connected if they share a lot of crew/cast members (or some other similarity measure combining this and genres, running times, release years, etc.). There are more options for the signal the students could consider on this graph, as they could use either the movie ratings, or the genre labels.

|          | Description                                           |         Amount |
| -------- | ----------------------------------------------------- | -------------: |
| nodes    | movies                                                |       millions (IMDb) ~5000 (Kaggle) |
| edges    | count of common cast/crew + other feature similarity. |                       O(10) per node |
| features | average rating                                        |                                    1 |
| labels   | movie genre                                           |            unknown (IMDb) 3 (Kaggle) |

For the extra work, there is plenty of extra information. For instance, the students could try to predict the revenue of movies by potentially including extra metadata. Note however that the number of instances in the original dataset is of the order of **millions**, so a smaller subset of those should be used.

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: yes if using the original datasets from IMDb, no if using the subsampled dataset from Kaggle
* **Network creation**: needs to be built from features

## Flight Routes
By Rodrigo

Resources:
* <https://openflights.org/data.html#route>
* <https://openflights.org/data.html>

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
