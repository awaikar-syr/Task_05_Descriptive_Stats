# Basketball-Specific LLM Prompts
## Syracuse Women's Basketball 2023-24 Dataset

### Dataset Context for LLMs
```
I have a dataset for the Syracuse Women's Basketball team from the 2023-24 NCAA Division I season. The team had a record of 24-8 (13-5 in ACC conference play), finished 2nd in the ACC, ranked #20 in the final AP poll, and reached the second round of the NCAA tournament.

The dataset contains statistics for 11 players over 32 games, including:
- Player name and position (G=Guard, F=Forward, C=Center)
- Games played and started
- Minutes played
- Points per game and total points
- Field goals made/attempted and percentage
- Three-pointers made/attempted and percentage
- Free throws made/attempted and percentage
- Rebounds per game and total rebounds
- Assists, steals, blocks, and turnovers

Here's the data:
[DATASET_CSV_DATA]
```

---

## Basic Questions (Easy for LLMs)

### B1. Team Overview
**Prompt:**
```
Based on the Syracuse Women's Basketball dataset provided, answer these basic questions:
1. How many players are on the team?
2. How many games did the team play this season?
3. What was the team's overall record?
4. Who was the leading scorer (highest points per game)?
5. What position does the leading scorer play?
```

**Expected Answer:** 
- 11 players
- 32 games
- 24-8 record
- Dyaisha Fair (22.2 PPG)
- Guard (G)

### B2. Top Performers
**Prompt:**
```
Using the basketball dataset, identify:
1. The top 3 scorers by points per game
2. The player with the most rebounds per game
3. The player with the most assists
4. The player with the most steals
5. The player with the most blocks
```

**Expected Answer:**
- Top 3 scorers: Dyaisha Fair (22.2), Georgia Woolley (13.8), Alaina Rice (9.8)
- Most rebounds: Alyssa Latham (7.0 RPG)
- Most assists: Dyaisha Fair (114)
- Most steals: Dyaisha Fair (76)
- Most blocks: Alyssa Latham (42)

### B3. Shooting Statistics
**Prompt:**
```
Analyze the shooting statistics from the basketball dataset:
1. Who has the highest field goal percentage (minimum 50 attempts)?
2. Who has the highest three-point percentage (minimum 20 attempts)?
3. Who has the highest free throw percentage (minimum 10 attempts)?
4. How many players attempted three-pointers?
5. What is the team's overall field goal percentage?
```

---

## Intermediate Questions (Require Analysis)

### I1. Position Analysis
**Prompt:**
```
Analyze the Syracuse Women's Basketball data by position:
1. How many players are in each position (Guard, Forward, Center)?
2. Which position has the highest average points per game?
3. Which position has the highest average rebounds per game?
4. Who is the best player in each position based on points per game?
5. Are there any patterns in shooting percentages by position?
```

### I2. Efficiency Analysis
**Prompt:**
```
Define and calculate player efficiency for the Syracuse Women's Basketball team:
1. Create an efficiency rating that considers points, rebounds, assists, steals, blocks, and turnovers
2. Who are the 3 most efficient players based on your rating?
3. Who are the 3 least efficient players (minimum 10 minutes per game)?
4. Which players have the highest efficiency per minute played?
5. What factors contribute most to a player's efficiency rating?
```

### I3. Performance Trends
**Prompt:**
```
Based on the basketball statistics provided:
1. Which players have the best shooting efficiency (high field goal percentage with significant attempts)?
2. Who are the most well-rounded players (good in multiple statistical categories)?
3. Which players might be underperforming given their playing time?
4. Who are the most consistent performers across different metrics?
5. What patterns do you notice in the relationship between minutes played and performance?
```

---

## Advanced Questions (Complex Analysis)

### A1. Most Improved Player Analysis
**Prompt:**
```
Define a methodology to identify the "most improved player" for the Syracuse Women's Basketball team:
1. What metrics would you use to measure improvement?
2. How would you weight different factors (scoring, efficiency, playing time, etc.)?
3. Based on your methodology, who would you identify as the most improved player?
4. What evidence supports your conclusion?
5. How would you measure improvement if you had data from the previous season?
```

### A2. Strategic Coaching Decision
**Prompt:**
```
As a coach of the Syracuse Women's Basketball team, if you wanted to win 2 more games next season:
1. Should you focus on improving offense or defense? Justify your answer using the data.
2. Which ONE player should you work with most closely to be a "game changer" and why?
3. What specific aspects of that player's game should you focus on improving?
4. How would you measure the success of your coaching intervention?
5. What other factors beyond individual player stats should you consider?
```

### A3. Team Composition Analysis
**Prompt:**
```
Analyze the Syracuse Women's Basketball team composition and strategy:
1. What are the team's strengths based on the statistical data?
2. What are the team's weaknesses or areas for improvement?
3. How well-balanced is the team across different positions?
4. What type of playing style does this data suggest the team employs?
5. If you were building a team to compete against Syracuse, what would be your strategy?
```

---

## Visualization Requests

### V1. Performance Charts
**Prompt:**
```
Create visualizations for the Syracuse Women's Basketball data:
1. A bar chart showing the top 8 scorers by points per game
2. A pie chart showing the distribution of players by position
3. A scatter plot showing the relationship between field goal percentage and points per game
4. A radar chart comparing the top 3 players across multiple statistical categories
```

### V2. Statistical Comparisons
**Prompt:**
```
Generate charts to compare player performance:
1. A horizontal bar chart ranking players by efficiency rating
2. A heatmap showing shooting percentages (FG%, 3P%, FT%) for each player
3. A stacked bar chart showing offensive vs defensive contributions
4. A bubble chart with points per game, rebounds per game, and assists as dimensions
```

---

## Validation Questions

### V3. Data Verification
**Prompt:**
```
Verify the accuracy of these statements about the Syracuse Women's Basketball data:
1. "Dyaisha Fair scored more than 700 total points this season"
2. "The team has more guards than forwards"
3. "Alyssa Latham had the highest field goal percentage"
4. "Georgia Woolley played in all 32 games"
5. "The team's leading scorer also led in assists"

For each statement, provide the correct answer and explain your reasoning.
```

---

## Prompt Engineering Notes

### What Works Well:
- Providing clear context about the team and season
- Specifying minimum thresholds for statistical analysis
- Asking for methodology and reasoning
- Requesting multiple data points for comparison

### What to Test:
- Different ways of presenting the data to LLMs
- Varying levels of detail in the context
- Asking for both quantitative and qualitative analysis
- Testing LLM ability to create and apply custom metrics

### Expected Challenges:
- LLMs may struggle with complex efficiency calculations
- Visualizations may be limited by LLM capabilities
- Strategic analysis requires basketball knowledge beyond the data
- Improvement analysis is difficult without historical data 