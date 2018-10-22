

---
id=0 
title=gStore: Answering SPARQL queries via subgraph matching
author=Lei Zou, Jinghui Mo, Lei Chen, M. Tamer Ozsu, Dongyan Zhao
journal=Proceedings of the Vldb Endowment
year=2011
tags=RDF, SPARQL Queries, Subgraph Matching, S-Tree, VS*-tree
star=****
problem=store and query RDF data via subgraph matching
interest=RDF has been used in various applications. For example, Yago, DBPedia & Bio2RDF
hardness=query processing & wildcard queries & scalability & Subgraph matching is a NP-hard problem & storage problem
idea=graph-based approach,translate a SPARQL query to a query graph. VS*-tree(like B+ tree, good for disk storage), searching strategy like DFS 
future=not mentioned
comment=A detailed paper. VS*-tree is its main contribution.
other= NULL


---
id=1
title=Natural language question answering over RDF: a graph data driven approach
author=Lei Zou，Ruizhe Huang，Haixun Wang，Jeffrey Xu Yu，Wenqiang He，Dongyan Zhao
journal=ACM SIGMOD International Conference on Management of Data
year=2014
tags=NLP, RDP Q/A, Graph
star=****
problem=Answer a natural language problem via RDF Q/A system
interest= We need a easy interface for users to use Q/A system
hardness= Natural language has ambiguation
idea= rudece NPL to subgraph matching query Q^s and then evaluate Q^s. If passed, search Q^s in the database 
future=NULL
comment=Subgraph matching is a NP-hard question, time complexity may become a challenge. Use subgraph matching to understand natural language is a new point
other=NULL

---
id=2 
title=Subgraph matching: on compression and computation.
author=Miao Qiao, Hao Zhang and Hong Cheng
journal= Proceedings of the Vldb Endowment
year=2017
tags=VCBC(vertex-cover based compression), CBF, helve, Crystal and clique , C(x,y)
star=****
problem=Find the set of all the subgraphs that are iosmorphic to the pattern graph.
interest=various appliactions such as biology ,social science ,et al.
hardness=It is NP hard & target graph may not fit into the memory & output crisis
idea=using output compression（vector-cover based）, Crystal-based Computation Framework to reduce the cost of subgraph matching. Combine both to 'Core-Crysstal Decomposition'& introduce CBF to external momory and parallel platforms
future=explore the compression technique on directed or labeled grapgs
comment=a minimun vertex cover is still preferred & the definition of 'helve' cannot be found outside
other= NULL

---
id=3
title=An analytical study of large SPARQL query logs.
author=Angela Bonifati, Wim Martens, and Thomas Timm
journal=Proceedings of the Vldb Endowment
year=2017
tags= Analytical study, topology of queries, CQ( conjuctive queries)
star=****
problem=some features among SPARQL query logs
interest= Query logs can indicate the actual usage of data
hardness= projection makes the evalutaion hard(so ignore it)
idea=mine the projection in Queries, analyse the shape/structure of queries(chain faster than cycle), Sort the graph into two classes: graph and hyper-graph & the introduction of streak
future= more refined analysis on the encountered streaks& evaluation of streaks of larger scale
comment= It's a statistics analyzing essay. Simple queries (one triple) are the majority. Some kinds of queries (CQ , CQ^F, CQ^OF,etc) have some advantages which can reduce computation and they also take a large percentage.
other= NULL


Haven't read through
---
id=4 
title=Turbo iso : towards ultrafast and robust subgraph isomorphism search in large graph databases
author=Wook-Shin Han,Jinsoo Lee and Jeong-Hoon Lee
journal=International Conference on Management of Data (ACM SIGMOD)
year=2013
tags=neighborhood equivalence class
star=****
problem=
interest=
hardness=
idea=
future=
comment=
other= NULL

---
id=0 
title=
author=
journal=
year=
tags=
star=
problem=
interest=
hardness=
idea=
future=
comment=
other= NULL

---
id=0 
title=
author=
journal=
year=
tags=
star=
problem=
interest=
hardness=
idea=
future=
comment=
other= NULL

---
id=0 
title=
author=
journal=
year=
tags=
star=
problem=
interest=
hardness=
idea=
future=
comment=
other= NULL
---