---
title=Redesign of the gStore system
author=Li Zeng,Lei Zou
journal=Frontiers Comput. Sci.(FCS)
year=2018
tags=Database System,Graph Algorithm,Subgraph Matching,RDF Management,SPARQL Query
star=**
problem=optimize the graph database system - gStore
interest=to answer SPARQL queries as quickly as possible
hardness=the complexity of subgraph matching enumeration is NP-hard
idea=consider the shape of queries and new join algorithm based on filtering-and-verification framework
future=accelerate the system using new hardware like GPU, SSD, and FPGA
other=FCS is not in the CCF list
---
title=Scalable Breadth-First Search on a GPU Cluster
author=Yuechao Pan,Roger Pearce,John D. Owens
journal=International Parallel & Distributed Processing Symposium(IPDPS)
year=2018
tags=Multiple GPU,Distributed Graph Processing,BFS
star=***
problem=the ratio of high computing power to communication bandwidth makes scaling BFS quite challenging on a GPU cluster
interest=BFS is a basic operator in graph algorithms and its speed is very important
hardness=the communication cost among multiple GPUs
idea=efficient graph representation(divide and store), finish local computation first, reduce communication by separating vertices by out-degrees
future=investigate applications beyond BFS, apply the ideas or explore new ides for optimization
other=IPDPS is a CCF B-class conference in the high performance computing area
---
