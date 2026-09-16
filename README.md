# Banking-Stock-Knowledge-Graph (Banking Stock Knowledge Graph: Visualization & QA System)
Built a knowledge graph using Neo4j and Cypher covering 4,140 stocks, 3,014 shareholders, and 360 concepts, with ECharts visualization and a FastText-based QA system.
## Demo

###

## Core Features

- Knowledge graph construction using Neo4j with Cypher, modeling stock–shareholder–concept relationships
- Interactive visualization with ECharts + JavaScript: full graph view, node search, China map, pie charts, and A-share trend line charts
- QA system with FastText-based intent classification and semantic parsing
- Multi-turn dialogue with context-aware auto-completion
- Flask backend with ECharts-based web interface

## Tech Stack

Python, Neo4j, Cypher, FastText, ECharts, JavaScript, Tushare API, Flask

## How to run

**Prerequirements**:Python 3.9+, Neo4j installed and running

```bash
neo4j.bat console                #Start Neo4j
pip install -r requirements.txt  #Install dependencies
python app.py                    #Run the app
```
