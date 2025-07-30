"""
Syracuse Women's Basketball Data Analyzer
For Task 05: Descriptive Statistics and Large Language Models

This script provides specialized analysis for the Syracuse Women's Basketball 2023-24 dataset.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Tuple
import json
from datetime import datetime

class BasketballAnalyzer:
    """
    A specialized class for analyzing Syracuse Women's Basketball data
    and providing baseline statistics for validating LLM responses.
    """
    
    def __init__(self, data_path: str = "data/syracuse_womens_basketball_2023_24.csv"):
        """
        Initialize the basketball analyzer.
        
        Args:
            data_path (str): Path to the basketball dataset
        """
        self.data = None
        self.data_path = data_path
        self.analysis_results = {}
        
        if data_path:
            self.load_data(data_path)
    
    def load_data(self, data_path: str) -> bool:
        """
        Load the basketball dataset.
        
        Args:
            data_path (str): Path to the CSV file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.data = pd.read_csv(data_path)
            print(f"Basketball data loaded successfully. Shape: {self.data.shape}")
            print(f"Players: {len(self.data)}")
            print(f"Columns: {list(self.data.columns)}")
            return True
            
        except Exception as e:
            print(f"Error loading basketball data: {e}")
            return False
    
    def basic_team_stats(self) -> Dict:
        """
        Calculate basic team statistics.
        
        Returns:
            Dict: Basic team statistics
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return {}
        
        # Team totals
        total_games = self.data['Games_Played'].max()  # Should be 32 for all players
        total_points = self.data['Total_Points'].sum()
        total_rebounds = self.data['Total_Rebounds'].sum()
        total_assists = self.data['Assists'].sum()
        total_steals = self.data['Steals'].sum()
        total_blocks = self.data['Blocks'].sum()
        total_turnovers = self.data['Turnovers'].sum()
        
        # Team averages
        avg_points_per_game = total_points / total_games
        avg_rebounds_per_game = total_rebounds / total_games
        avg_assists_per_game = total_assists / total_games
        
        # Shooting percentages (weighted by attempts)
        total_fg_attempted = self.data['Field_Goals_Attempted'].sum()
        total_fg_made = self.data['Field_Goals_Made'].sum()
        team_fg_percentage = total_fg_made / total_fg_attempted if total_fg_attempted > 0 else 0
        
        total_3pt_attempted = self.data['Three_Pointers_Attempted'].sum()
        total_3pt_made = self.data['Three_Pointers_Made'].sum()
        team_3pt_percentage = total_3pt_made / total_3pt_attempted if total_3pt_attempted > 0 else 0
        
        total_ft_attempted = self.data['Free_Throws_Attempted'].sum()
        total_ft_made = self.data['Free_Throws_Made'].sum()
        team_ft_percentage = total_ft_made / total_ft_attempted if total_ft_attempted > 0 else 0
        
        stats = {
            'team_overview': {
                'total_players': len(self.data),
                'total_games': int(total_games),
                'season_record': '24-8 (13-5 ACC)',  # From context provided
                'ncaa_tournament': 'Reached second round',
                'final_ranking': '#20 AP'
            },
            'team_totals': {
                'total_points': int(total_points),
                'total_rebounds': int(total_rebounds),
                'total_assists': int(total_assists),
                'total_steals': int(total_steals),
                'total_blocks': int(total_blocks),
                'total_turnovers': int(total_turnovers)
            },
            'team_averages': {
                'points_per_game': round(avg_points_per_game, 1),
                'rebounds_per_game': round(avg_rebounds_per_game, 1),
                'assists_per_game': round(avg_assists_per_game, 1),
                'steals_per_game': round(total_steals / total_games, 1),
                'blocks_per_game': round(total_blocks / total_games, 1),
                'turnovers_per_game': round(total_turnovers / total_games, 1)
            },
            'team_shooting': {
                'field_goal_percentage': round(team_fg_percentage * 100, 1),
                'three_point_percentage': round(team_3pt_percentage * 100, 1),
                'free_throw_percentage': round(team_ft_percentage * 100, 1)
            }
        }
        
        self.analysis_results['basic_team_stats'] = stats
        return stats
    
    def player_rankings(self) -> Dict:
        """
        Create player rankings by various metrics.
        
        Returns:
            Dict: Player rankings
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return {}
        
        # Top scorers
        top_scorers = self.data.nlargest(5, 'Points_Per_Game')[['Player', 'Points_Per_Game', 'Total_Points']].to_dict('records')
        
        # Top rebounders
        top_rebounders = self.data.nlargest(5, 'Rebounds_Per_Game')[['Player', 'Rebounds_Per_Game', 'Total_Rebounds']].to_dict('records')
        
        # Top assist leaders
        top_assists = self.data.nlargest(5, 'Assists')[['Player', 'Assists']].to_dict('records')
        
        # Top steal leaders
        top_steals = self.data.nlargest(5, 'Steals')[['Player', 'Steals']].to_dict('records')
        
        # Top block leaders
        top_blocks = self.data.nlargest(5, 'Blocks')[['Player', 'Blocks']].to_dict('records')
        
        # Most efficient shooters (minimum 50 attempts)
        min_attempts = 50
        efficient_shooters = self.data[self.data['Field_Goals_Attempted'] >= min_attempts].nlargest(5, 'Field_Goal_Percentage')[['Player', 'Field_Goal_Percentage', 'Field_Goals_Made', 'Field_Goals_Attempted']].to_dict('records')
        
        # Best 3-point shooters (minimum 20 attempts)
        min_3pt_attempts = 20
        best_3pt_shooters = self.data[self.data['Three_Pointers_Attempted'] >= min_3pt_attempts].nlargest(5, 'Three_Point_Percentage')[['Player', 'Three_Point_Percentage', 'Three_Pointers_Made', 'Three_Pointers_Attempted']].to_dict('records')
        
        rankings = {
            'top_scorers': top_scorers,
            'top_rebounders': top_rebounders,
            'top_assists': top_assists,
            'top_steals': top_steals,
            'top_blocks': top_blocks,
            'most_efficient_shooters': efficient_shooters,
            'best_3pt_shooters': best_3pt_shooters
        }
        
        self.analysis_results['player_rankings'] = rankings
        return rankings
    
    def position_analysis(self) -> Dict:
        """
        Analyze performance by position.
        
        Returns:
            Dict: Position-based analysis
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return {}
        
        # Group by position
        position_stats = self.data.groupby('Position').agg({
            'Points_Per_Game': ['mean', 'sum'],
            'Rebounds_Per_Game': ['mean', 'sum'],
            'Assists': ['mean', 'sum'],
            'Steals': ['mean', 'sum'],
            'Blocks': ['mean', 'sum'],
            'Field_Goal_Percentage': 'mean',
            'Three_Point_Percentage': 'mean',
            'Free_Throw_Percentage': 'mean'
        }).round(2)
        
        # Convert multi-level column names to strings for JSON serialization
        position_stats.columns = [f"{col[0]}_{col[1]}" if isinstance(col, tuple) else col for col in position_stats.columns]
        
        # Player count by position
        position_counts = self.data['Position'].value_counts().to_dict()
        
        # Best player by position
        best_by_position = {}
        for position in self.data['Position'].unique():
            pos_data = self.data[self.data['Position'] == position]
            best_player = pos_data.loc[pos_data['Points_Per_Game'].idxmax()]
            best_by_position[position] = {
                'player': best_player['Player'],
                'points_per_game': best_player['Points_Per_Game'],
                'total_points': best_player['Total_Points']
            }
        
        analysis = {
            'position_counts': position_counts,
            'position_stats': position_stats.to_dict(),
            'best_by_position': best_by_position
        }
        
        self.analysis_results['position_analysis'] = analysis
        return analysis
    
    def efficiency_analysis(self) -> Dict:
        """
        Analyze player efficiency and improvement potential.
        
        Returns:
            Dict: Efficiency analysis
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return {}
        
        # Calculate efficiency metrics
        self.data['efficiency_rating'] = (
            self.data['Points_Per_Game'] + 
            self.data['Rebounds_Per_Game'] * 1.2 + 
            self.data['Assists'] / self.data['Games_Played'] * 2 + 
            self.data['Steals'] / self.data['Games_Played'] * 2 + 
            self.data['Blocks'] / self.data['Games_Played'] * 2 - 
            self.data['Turnovers'] / self.data['Games_Played']
        )
        
        # Minutes per game
        self.data['minutes_per_game'] = self.data['Minutes_Played'] / self.data['Games_Played']
        
        # Efficiency per minute
        self.data['efficiency_per_minute'] = self.data['efficiency_rating'] / self.data['minutes_per_game']
        
        # Most efficient players (minimum 10 minutes per game)
        min_minutes = 10
        most_efficient = self.data[self.data['minutes_per_game'] >= min_minutes].nlargest(5, 'efficiency_per_minute')[['Player', 'efficiency_per_minute', 'efficiency_rating', 'minutes_per_game']].to_dict('records')
        
        # Players with most room for improvement (high minutes, lower efficiency)
        improvement_candidates = self.data[self.data['minutes_per_game'] >= 15].nsmallest(3, 'efficiency_per_minute')[['Player', 'efficiency_per_minute', 'minutes_per_game', 'Points_Per_Game']].to_dict('records')
        
        efficiency = {
            'most_efficient_players': most_efficient,
            'improvement_candidates': improvement_candidates,
            'efficiency_metrics': {
                'avg_efficiency': round(self.data['efficiency_rating'].mean(), 2),
                'avg_efficiency_per_minute': round(self.data['efficiency_per_minute'].mean(), 3)
            }
        }
        
        self.analysis_results['efficiency_analysis'] = efficiency
        return efficiency
    
    def generate_basketball_visualizations(self, save_path: str = "results/") -> List[str]:
        """
        Generate basketball-specific visualizations.
        
        Args:
            save_path (str): Path to save visualizations
            
        Returns:
            List[str]: List of generated plot filenames
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return []
        
        plots = []
        
        try:
            # Set style
            plt.style.use('default')
            sns.set_palette("husl")
            
            # 1. Points per game by player
            plt.figure(figsize=(12, 8))
            top_players = self.data.nlargest(8, 'Points_Per_Game')
            plt.barh(top_players['Player'], top_players['Points_Per_Game'])
            plt.xlabel('Points Per Game')
            plt.title('Top Scorers - Syracuse Women\'s Basketball 2023-24')
            plt.gca().invert_yaxis()
            if save_path:
                plot_path = f"{save_path}/top_scorers.png"
                plt.savefig(plot_path, bbox_inches='tight', dpi=300)
                plots.append(plot_path)
            plt.show()
            
            # 2. Position distribution
            plt.figure(figsize=(8, 6))
            position_counts = self.data['Position'].value_counts()
            plt.pie(position_counts.values, labels=position_counts.index, autopct='%1.1f%%')
            plt.title('Player Distribution by Position')
            if save_path:
                plot_path = f"{save_path}/position_distribution.png"
                plt.savefig(plot_path, bbox_inches='tight', dpi=300)
                plots.append(plot_path)
            plt.show()
            
            # 3. Shooting efficiency scatter plot
            plt.figure(figsize=(10, 8))
            plt.scatter(self.data['Field_Goal_Percentage'], self.data['Points_Per_Game'], 
                       s=self.data['Minutes_Played']/20, alpha=0.7)
            for i, player in enumerate(self.data['Player']):
                plt.annotate(player, (self.data['Field_Goal_Percentage'].iloc[i], 
                                    self.data['Points_Per_Game'].iloc[i]), 
                           fontsize=8, alpha=0.8)
            plt.xlabel('Field Goal Percentage')
            plt.ylabel('Points Per Game')
            plt.title('Shooting Efficiency vs Scoring')
            if save_path:
                plot_path = f"{save_path}/shooting_efficiency.png"
                plt.savefig(plot_path, bbox_inches='tight', dpi=300)
                plots.append(plot_path)
            plt.show()
            
            # 4. Player comparison radar chart (top 3 players)
            top_3 = self.data.nlargest(3, 'Points_Per_Game')
            categories = ['Points_Per_Game', 'Rebounds_Per_Game', 'Assists', 'Steals', 'Blocks']
            
            fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(projection='polar'))
            
            angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
            angles += angles[:1]  # Complete the circle
            
            for i, player in enumerate(top_3['Player']):
                values = []
                for cat in categories:
                    val = top_3[top_3['Player'] == player][cat].iloc[0]
                    # Normalize values for radar chart
                    if cat == 'Points_Per_Game':
                        val = val / 25  # Normalize to 0-1 scale
                    elif cat == 'Rebounds_Per_Game':
                        val = val / 10
                    elif cat in ['Assists', 'Steals', 'Blocks']:
                        val = val / 100
                    values.append(val)
                values += values[:1]  # Complete the circle
                
                ax.plot(angles, values, 'o-', linewidth=2, label=player)
                ax.fill(angles, values, alpha=0.25)
            
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(categories)
            ax.set_ylim(0, 1)
            ax.set_title('Top 3 Players - Performance Comparison')
            ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
            if save_path:
                plot_path = f"{save_path}/player_comparison_radar.png"
                plt.savefig(plot_path, bbox_inches='tight', dpi=300)
                plots.append(plot_path)
            plt.show()
            
        except Exception as e:
            print(f"Error generating visualizations: {e}")
        
        return plots
    
    def get_llm_validation_data(self) -> Dict:
        """
        Get structured data for LLM validation.
        
        Returns:
            Dict: Data formatted for LLM validation
        """
        return {
            'dataset_summary': {
                'team': 'Syracuse Women\'s Basketball 2023-24',
                'total_players': len(self.data) if self.data is not None else 0,
                'total_games': 32,
                'season_record': '24-8 (13-5 ACC)',
                'columns': list(self.data.columns) if self.data is not None else [],
                'sample_data': self.data.head().to_dict() if self.data is not None else {}
            },
            'analysis_results': self.analysis_results
        }
    
    def export_analysis(self, filepath: str) -> bool:
        """
        Export analysis results to JSON file.
        
        Args:
            filepath (str): Path to save the analysis results
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(filepath, 'w') as f:
                json.dump(self.analysis_results, f, indent=2, default=str)
            print(f"Basketball analysis exported to {filepath}")
            return True
        except Exception as e:
            print(f"Error exporting analysis: {e}")
            return False

def main():
    """
    Main function to demonstrate usage of the BasketballAnalyzer.
    """
    print("Syracuse Women's Basketball Analyzer - Task 05")
    print("=" * 50)
    
    # Initialize analyzer
    analyzer = BasketballAnalyzer()
    
    # Perform comprehensive analysis
    print("\n1. Basic Team Statistics...")
    team_stats = analyzer.basic_team_stats()
    
    print("\n2. Player Rankings...")
    rankings = analyzer.player_rankings()
    
    print("\n3. Position Analysis...")
    position_analysis = analyzer.position_analysis()
    
    print("\n4. Efficiency Analysis...")
    efficiency = analyzer.efficiency_analysis()
    
    print("\n5. Generating Visualizations...")
    plots = analyzer.generate_basketball_visualizations()
    
    print("\n6. Exporting Results...")
    analyzer.export_analysis("results/basketball_analysis.json")
    
    print("\nAnalysis complete!")
    print(f"Generated {len(plots)} visualizations")
    print("Results saved to results/basketball_analysis.json")

if __name__ == "__main__":
    main() 