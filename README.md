# Banking-Stock-Knowledge-Graph (Banking Stock Knowledge Graph: Visualization & QA System)
Built a knowledge graph using Neo4j and Cypher covering 4,140 stocks, 3,014 shareholders, and 360 concepts, with ECharts visualization and a FastText-based QA system.

## Demo

### Node Search Interface

#### Search "CITIC Securities" under the Shareholder entity to display all stocks held by CITIC Securities

<img width="1920" height="1015" alt="image" src="https://github.com/user-attachments/assets/7e1af52a-1f8d-44a6-8527-b2326c71cf08" />

### Search "Ping An Bank" under the Stock entity to display its associated concepts and shareholders

<img width="1920" height="1000" alt="image" src="https://github.com/user-attachments/assets/ea28d784-dbb3-40fb-b1c4-af5aedb0bc7e" />

### Search "Bank" under the Concept entity to display all stocks classified under the Bank concept

<img width="1920" height="985" alt="image" src="https://github.com/user-attachments/assets/0016fc5a-32f7-4956-960b-65d87cc3135f" />

### Full Graph View

### Enter 25 under the "Holds" relationship to display a graph of stock–shareholder relationships

<img width="1920" height="876" alt="image" src="https://github.com/user-attachments/assets/a32ab254-3c12-4a05-8f89-31c97e4ebe2f" />

### Enter 25 under the "Belongs-to" relationship to display a graph of stock–concept relationships

<img width="1920" height="975" alt="image" src="https://github.com/user-attachments/assets/c2e2b15e-aacd-48a8-9180-e2e5b5cb3753" />

### Bank Distribution by Province — displayed with both a map and a pie chart

<img width="1920" height="995" alt="image" src="https://github.com/user-attachments/assets/db722629-5021-438e-a8df-e9d6d8476974" />

### A-share trading data - displayed with a color-coded line chart (green/black/blue/red by price range)

<img width="1920" height="1015" alt="image" src="https://github.com/user-attachments/assets/4403651d-9f20-4c97-b6ad-1b3bae3df276" />

### QA System Interface — generates Cypher queries to retrieve answers from the Neo4j knowledge graph and supports context-aware multi-turn dialogue for follow-up questions.

<img width="1400" height="1020" alt="image" src="https://github.com/user-attachments/assets/251c9db0-51a6-4b49-a12a-a965816eca04" />

## Core Features

- Knowledge graph construction using Neo4j with Cypher, modeling stock–shareholder–concept relationships
- Interactive visualization with ECharts + JavaScript: full graph view, node search, China map, pie charts, and A-share trend line charts
- QA system with FastText-based intent classification and semantic parsing
- Multi-turn dialogue with context-aware auto-completion
- Flask backend with ECharts-based web interface

## Tech Stack

Python, Neo4j, Cypher, FastText, ECharts, JavaScript, Tushare API, Flask

## How to run

**Prerequisites：** Python 3.9+, Neo4j installed and running

```bash
neo4j console                    # Start Neo4j
pip install -r requirements.txt  # Install dependencies
python app.py                    # Run the app
```
