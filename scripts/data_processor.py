"""
Data Processing and Analysis Script
For Task 05: Descriptive Statistics and Large Language Models

This script provides functions to:
1. Load and clean sports data
2. Calculate basic descriptive statistics
3. Generate baseline analysis for LLM validation
4. Create visualizations for comparison
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Tuple
import json
from datetime import datetime

class SportsDataAnalyzer:
    """
    A class to handle sports data analysis and provide baseline statistics
    for validating LLM responses.
    """
    
    def __init__(self, data_path: str = None):
        """
        Initialize the analyzer with optional data path.
        
        Args:
            data_path (str): Path to the dataset file
        """
        self.data = None
        self.data_path = data_path
        self.analysis_results = {}
        
        if data_path:
            self.load_data(data_path)
    
    def load_data(self, data_path: str) -> bool:
        """
        Load data from various file formats.
        
        Args:
            data_path (str): Path to the data file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if data_path.endswith('.csv'):
                self.data = pd.read_csv(data_path)
            elif data_path.endswith('.xlsx'):
                self.data = pd.read_excel(data_path)
            elif data_path.endswith('.json'):
                self.data = pd.read_json(data_path)
            else:
                print(f"Unsupported file format: {data_path}")
                return False
            
            print(f"Data loaded successfully. Shape: {self.data.shape}")
            return True
            
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
    
    def basic_descriptive_stats(self) -> Dict:
        """
        Calculate basic descriptive statistics for the dataset.
        
        Returns:
            Dict: Dictionary containing basic statistics
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return {}
        
        stats = {
            'dataset_info': {
                'total_records': len(self.data),
                'columns': list(self.data.columns),
                'data_types': self.data.dtypes.to_dict()
            },
            'basic_stats': self.data.describe().to_dict(),
            'missing_values': self.data.isnull().sum().to_dict()
        }
        
        self.analysis_results['basic_stats'] = stats
        return stats
    
    def team_performance_analysis(self) -> Dict:
        """
        Analyze team performance metrics.
        
        Returns:
            Dict: Team performance analysis
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return {}
        
        # This will be customized based on the actual dataset structure
        # Placeholder for team performance analysis
        performance = {
            'total_games': 0,
            'wins': 0,
            'losses': 0,
            'win_percentage': 0.0,
            'average_score': 0.0,
            'best_performance': None,
            'worst_performance': None
        }
        
        self.analysis_results['team_performance'] = performance
        return performance
    
    def player_analysis(self) -> Dict:
        """
        Analyze individual player performance.
        
        Returns:
            Dict: Player performance analysis
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return {}
        
        # This will be customized based on the actual dataset structure
        # Placeholder for player analysis
        players = {
            'top_scorers': [],
            'most_consistent': [],
            'most_improved': None,
            'player_stats': {}
        }
        
        self.analysis_results['player_analysis'] = players
        return players
    
    def generate_visualizations(self, save_path: str = None) -> List[str]:
        """
        Generate basic visualizations for the dataset.
        
        Args:
            save_path (str): Path to save visualizations
            
        Returns:
            List[str]: List of generated plot filenames
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return []
        
        plots = []
        
        # Example visualizations (to be customized based on data)
        try:
            # 1. Data distribution plot
            plt.figure(figsize=(10, 6))
            self.data.hist(bins=20, figsize=(10, 6))
            plt.title('Data Distribution')
            if save_path:
                plot_path = f"{save_path}/data_distribution.png"
                plt.savefig(plot_path)
                plots.append(plot_path)
            plt.show()
            
            # 2. Correlation heatmap (if numeric data)
            numeric_cols = self.data.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 1:
                plt.figure(figsize=(8, 6))
                sns.heatmap(self.data[numeric_cols].corr(), annot=True, cmap='coolwarm')
                plt.title('Correlation Heatmap')
                if save_path:
                    plot_path = f"{save_path}/correlation_heatmap.png"
                    plt.savefig(plot_path)
                    plots.append(plot_path)
                plt.show()
                
        except Exception as e:
            print(f"Error generating visualizations: {e}")
        
        return plots
    
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
            print(f"Analysis exported to {filepath}")
            return True
        except Exception as e:
            print(f"Error exporting analysis: {e}")
            return False
    
    def get_llm_validation_data(self) -> Dict:
        """
        Get structured data for LLM validation.
        
        Returns:
            Dict: Data formatted for LLM validation
        """
        return {
            'dataset_summary': {
                'total_records': len(self.data) if self.data is not None else 0,
                'columns': list(self.data.columns) if self.data is not None else [],
                'sample_data': self.data.head().to_dict() if self.data is not None else {}
            },
            'analysis_results': self.analysis_results
        }

def main():
    """
    Main function to demonstrate usage of the SportsDataAnalyzer.
    """
    print("Sports Data Analyzer - Task 05")
    print("=" * 40)
    
    # Example usage (to be customized with actual data)
    analyzer = SportsDataAnalyzer()
    
    # Load data when available
    # analyzer.load_data("path/to/your/dataset.csv")
    
    # Perform analysis
    # analyzer.basic_descriptive_stats()
    # analyzer.team_performance_analysis()
    # analyzer.player_analysis()
    
    # Generate visualizations
    # analyzer.generate_visualizations("results/")
    
    # Export results
    # analyzer.export_analysis("results/baseline_analysis.json")
    
    print("Analysis complete!")

if __name__ == "__main__":
    main() 