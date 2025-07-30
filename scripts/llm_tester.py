"""
LLM Testing Framework for Task 05: Descriptive Statistics and Large Language Models
Using OpenRouter API to test multiple LLMs with Syracuse Women's Basketball dataset
"""

import requests
import json
import time
import pandas as pd
from typing import Dict, List, Tuple, Optional
from datetime import datetime
import os
from dataclasses import dataclass
from enum import Enum

class LLMProvider(Enum):
    """Available LLM providers through OpenRouter"""
    OPENAI_GPT4 = "openai/gpt-4"
    OPENAI_GPT35 = "openai/gpt-3.5-turbo"
    ANTHROPIC_CLAUDE = "anthropic/claude-3-opus"
    ANTHROPIC_CLAUDE_SONNET = "anthropic/claude-3-sonnet"
    GOOGLE_GEMINI = "google/gemini-pro"
    META_LLAMA = "meta-llama/llama-2-70b-chat"
    MISTRAL = "mistralai/mistral-7b-instruct"

@dataclass
class LLMResponse:
    """Structure for storing LLM responses"""
    provider: str
    model: str
    prompt: str
    response: str
    accuracy_score: Optional[float] = None
    response_time: Optional[float] = None
    tokens_used: Optional[int] = None
    cost: Optional[float] = None
    timestamp: str = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().isoformat()

class LLMTester:
    """
    A comprehensive LLM testing framework for sports data analysis
    """
    
    def __init__(self, api_key: str, base_url: str = "https://openrouter.ai/api/v1"):
        """
        Initialize the LLM tester with OpenRouter API credentials
        
        Args:
            api_key (str): OpenRouter API key
            base_url (str): OpenRouter API base URL
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/your-repo/Task_05_Descriptive_Stats",
            "X-Title": "Task 05 Descriptive Statistics Research"
        }
        self.responses = []
        self.test_results = {}
        
    def load_basketball_data(self, data_path: str = "data/syracuse_womens_basketball_2023_24.csv") -> str:
        """
        Load basketball data and format it for LLM prompts
        
        Args:
            data_path (str): Path to the basketball dataset
            
        Returns:
            str: Formatted data string for LLM prompts
        """
        try:
            df = pd.read_csv(data_path)
            
            # Create a formatted string representation
            data_str = "Syracuse Women's Basketball 2023-24 Season Statistics:\n\n"
            data_str += "Team Overview: 24-8 record (13-5 ACC), #20 AP ranking, NCAA tournament second round\n\n"
            data_str += "Player Statistics:\n"
            data_str += "-" * 80 + "\n"
            
            for _, row in df.iterrows():
                data_str += f"Player: {row['Player']}\n"
                data_str += f"Position: {row['Position']}\n"
                data_str += f"Games: {row['Games_Played']} (Started: {row['Games_Started']})\n"
                data_str += f"Minutes: {row['Minutes_Played']}\n"
                data_str += f"Points: {row['Points_Per_Game']} PPG ({row['Total_Points']} total)\n"
                data_str += f"Rebounds: {row['Rebounds_Per_Game']} RPG ({row['Total_Rebounds']} total)\n"
                data_str += f"Assists: {row['Assists']}, Steals: {row['Steals']}, Blocks: {row['Blocks']}, Turnovers: {row['Turnovers']}\n"
                data_str += f"Shooting: FG {row['Field_Goal_Percentage']:.3f} ({row['Field_Goals_Made']}/{row['Field_Goals_Attempted']}), "
                data_str += f"3P {row['Three_Point_Percentage']:.3f} ({row['Three_Pointers_Made']}/{row['Three_Pointers_Attempted']}), "
                data_str += f"FT {row['Free_Throw_Percentage']:.3f} ({row['Free_Throws_Made']}/{row['Free_Throws_Attempted']})\n"
                data_str += "-" * 80 + "\n"
            
            return data_str
            
        except Exception as e:
            print(f"Error loading basketball data: {e}")
            return ""
    
    def send_prompt(self, model: str, prompt: str, max_tokens: int = 2000) -> Dict:
        """
        Send a prompt to a specific LLM via OpenRouter API
        
        Args:
            model (str): Model identifier
            prompt (str): The prompt to send
            max_tokens (int): Maximum tokens for response
            
        Returns:
            Dict: API response
        """
        payload = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": max_tokens,
            "temperature": 0.1  # Low temperature for more consistent responses
        }
        
        try:
            start_time = time.time()
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload
            )
            end_time = time.time()
            
            if response.status_code == 200:
                result = response.json()
                return {
                    "success": True,
                    "response": result["choices"][0]["message"]["content"],
                    "usage": result.get("usage", {}),
                    "response_time": end_time - start_time,
                    "model": model
                }
            else:
                return {
                    "success": False,
                    "error": f"API Error {response.status_code}: {response.text}",
                    "response_time": end_time - start_time,
                    "model": model
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": f"Request failed: {str(e)}",
                "model": model
            }
    
    def test_basic_questions(self, data_str: str) -> List[LLMResponse]:
        """
        Test basic questions with multiple LLMs
        
        Args:
            data_str (str): Formatted basketball data
            
        Returns:
            List[LLMResponse]: List of responses from different LLMs
        """
        basic_questions = [
            {
                "question": "How many players are on the Syracuse Women's Basketball team?",
                "expected": "11 players",
                "category": "basic_count"
            },
            {
                "question": "How many games did the team play this season?",
                "expected": "32 games",
                "category": "basic_count"
            },
            {
                "question": "Who is the leading scorer (highest points per game)?",
                "expected": "Dyaisha Fair",
                "category": "basic_ranking"
            },
            {
                "question": "What position does the leading scorer play?",
                "expected": "Guard (G)",
                "category": "basic_position"
            },
            {
                "question": "What was the team's overall record?",
                "expected": "24-8",
                "category": "basic_record"
            }
        ]
        
        models_to_test = [
            LLMProvider.OPENAI_GPT4.value,
            LLMProvider.ANTHROPIC_CLAUDE.value,
            LLMProvider.GOOGLE_GEMINI.value
        ]
        
        responses = []
        
        for model in models_to_test:
            print(f"\nTesting {model} with basic questions...")
            
            for q in basic_questions:
                full_prompt = f"{data_str}\n\nQuestion: {q['question']}\n\nPlease provide a clear, concise answer based on the data provided."
                
                result = self.send_prompt(model, full_prompt)
                
                if result["success"]:
                    response = LLMResponse(
                        provider=model.split('/')[0],
                        model=model,
                        prompt=q['question'],
                        response=result["response"],
                        response_time=result["response_time"],
                        tokens_used=result["usage"].get("total_tokens", 0) if "usage" in result else 0
                    )
                    responses.append(response)
                    print(f"✓ {q['question'][:50]}... - {result['response_time']:.2f}s")
                else:
                    print(f"✗ Error with {model}: {result['error']}")
                
                time.sleep(1)  # Rate limiting
        
        return responses
    
    def test_intermediate_questions(self, data_str: str) -> List[LLMResponse]:
        """
        Test intermediate questions requiring analysis
        
        Args:
            data_str (str): Formatted basketball data
            
        Returns:
            List[LLMResponse]: List of responses from different LLMs
        """
        intermediate_questions = [
            {
                "question": "Who are the top 3 scorers by points per game? List them in order.",
                "category": "ranking_analysis"
            },
            {
                "question": "Which position (Guard, Forward, Center) has the highest average points per game?",
                "category": "position_analysis"
            },
            {
                "question": "Who has the most rebounds per game and what is their position?",
                "category": "statistical_analysis"
            },
            {
                "question": "Which player has the highest field goal percentage (minimum 50 attempts)?",
                "category": "efficiency_analysis"
            }
        ]
        
        models_to_test = [
            LLMProvider.OPENAI_GPT4.value,
            LLMProvider.ANTHROPIC_CLAUDE.value
        ]
        
        responses = []
        
        for model in models_to_test:
            print(f"\nTesting {model} with intermediate questions...")
            
            for q in intermediate_questions:
                full_prompt = f"{data_str}\n\nQuestion: {q['question']}\n\nPlease analyze the data and provide a detailed answer with reasoning."
                
                result = self.send_prompt(model, full_prompt, max_tokens=1000)
                
                if result["success"]:
                    response = LLMResponse(
                        provider=model.split('/')[0],
                        model=model,
                        prompt=q['question'],
                        response=result["response"],
                        response_time=result["response_time"],
                        tokens_used=result["usage"].get("total_tokens", 0) if "usage" in result else 0
                    )
                    responses.append(response)
                    print(f"✓ {q['question'][:50]}... - {result['response_time']:.2f}s")
                else:
                    print(f"✗ Error with {model}: {result['error']}")
                
                time.sleep(1)
        
        return responses
    
    def test_advanced_questions(self, data_str: str) -> List[LLMResponse]:
        """
        Test advanced questions requiring complex analysis
        
        Args:
            data_str (str): Formatted basketball data
            
        Returns:
            List[LLMResponse]: List of responses from different LLMs
        """
        advanced_questions = [
            {
                "question": "Define a methodology to identify the 'most improved player' for this team. What metrics would you use and who would you select?",
                "category": "methodology_development"
            },
            {
                "question": "As a coach, if you wanted to win 2 more games next season, should you focus on improving offense or defense? Justify your answer using the data.",
                "category": "strategic_analysis"
            },
            {
                "question": "Which ONE player should you work with most closely to be a 'game changer' and why? What specific aspects should you focus on?",
                "category": "coaching_decision"
            }
        ]
        
        models_to_test = [
            LLMProvider.OPENAI_GPT4.value,
            LLMProvider.ANTHROPIC_CLAUDE.value
        ]
        
        responses = []
        
        for model in models_to_test:
            print(f"\nTesting {model} with advanced questions...")
            
            for q in advanced_questions:
                full_prompt = f"{data_str}\n\nQuestion: {q['question']}\n\nPlease provide a comprehensive analysis with clear reasoning and methodology."
                
                result = self.send_prompt(model, full_prompt, max_tokens=1500)
                
                if result["success"]:
                    response = LLMResponse(
                        provider=model.split('/')[0],
                        model=model,
                        prompt=q['question'],
                        response=result["response"],
                        response_time=result["response_time"],
                        tokens_used=result["usage"].get("total_tokens", 0) if "usage" in result else 0
                    )
                    responses.append(response)
                    print(f"✓ {q['question'][:50]}... - {result['response_time']:.2f}s")
                else:
                    print(f"✗ Error with {model}: {result['error']}")
                
                time.sleep(1)
        
        return responses
    
    def evaluate_accuracy(self, responses: List[LLMResponse]) -> Dict:
        """
        Evaluate accuracy of responses against expected answers
        
        Args:
            responses (List[LLMResponse]): List of responses to evaluate
            
        Returns:
            Dict: Accuracy evaluation results
        """
        # Define expected answers for basic questions
        expected_answers = {
            "How many players are on the Syracuse Women's Basketball team?": "11",
            "How many games did the team play this season?": "32",
            "Who is the leading scorer (highest points per game)?": "Dyaisha Fair",
            "What position does the leading scorer play?": "Guard",
            "What was the team's overall record?": "24-8"
        }
        
        evaluation_results = {}
        
        for response in responses:
            if response.prompt in expected_answers:
                expected = expected_answers[response.prompt].lower()
                actual = response.response.lower()
                
                # Simple keyword matching for accuracy
                if expected in actual:
                    accuracy = 1.0
                elif any(word in actual for word in expected.split()):
                    accuracy = 0.7
                else:
                    accuracy = 0.0
                
                response.accuracy_score = accuracy
                
                if response.model not in evaluation_results:
                    evaluation_results[response.model] = {"correct": 0, "total": 0, "accuracy": 0.0}
                
                evaluation_results[response.model]["total"] += 1
                if accuracy > 0.5:
                    evaluation_results[response.model]["correct"] += 1
        
        # Calculate overall accuracy for each model
        for model in evaluation_results:
            if evaluation_results[model]["total"] > 0:
                evaluation_results[model]["accuracy"] = (
                    evaluation_results[model]["correct"] / evaluation_results[model]["total"]
                )
        
        return evaluation_results
    
    def export_results(self, filename: str = "results/llm_testing_results.json"):
        """
        Export all testing results to JSON file
        
        Args:
            filename (str): Output filename
        """
        # Convert responses to dictionaries
        response_data = []
        for response in self.responses:
            response_data.append({
                "provider": response.provider,
                "model": response.model,
                "prompt": response.prompt,
                "response": response.response,
                "accuracy_score": response.accuracy_score,
                "response_time": response.response_time,
                "tokens_used": response.tokens_used,
                "timestamp": response.timestamp
            })
        
        # Create results summary
        results_summary = {
            "test_date": datetime.now().isoformat(),
            "dataset": "Syracuse Women's Basketball 2023-24",
            "total_responses": len(self.responses),
            "models_tested": list(set([r.model for r in self.responses])),
            "responses": response_data,
            "evaluation": self.test_results
        }
        
        # Ensure results directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with open(filename, 'w') as f:
            json.dump(results_summary, f, indent=2)
        
        print(f"\nResults exported to {filename}")
    
    def run_comprehensive_test(self):
        """
        Run comprehensive testing across all question types and models
        """
        print("🏀 Syracuse Women's Basketball LLM Testing Framework")
        print("=" * 60)
        
        # Load basketball data
        print("\n1. Loading basketball dataset...")
        data_str = self.load_basketball_data()
        if not data_str:
            print("❌ Failed to load basketball data")
            return
        
        print("✅ Basketball data loaded successfully")
        
        # Test basic questions
        print("\n2. Testing basic questions...")
        basic_responses = self.test_basic_questions(data_str)
        self.responses.extend(basic_responses)
        
        # Test intermediate questions
        print("\n3. Testing intermediate questions...")
        intermediate_responses = self.test_intermediate_questions(data_str)
        self.responses.extend(intermediate_responses)
        
        # Test advanced questions
        print("\n4. Testing advanced questions...")
        advanced_responses = self.test_advanced_questions(data_str)
        self.responses.extend(advanced_responses)
        
        # Evaluate accuracy
        print("\n5. Evaluating accuracy...")
        self.test_results = self.evaluate_accuracy(self.responses)
        
        # Export results
        print("\n6. Exporting results...")
        self.export_results()
        
        # Print summary
        print("\n" + "=" * 60)
        print("📊 TESTING SUMMARY")
        print("=" * 60)
        
        for model, results in self.test_results.items():
            print(f"\n{model}:")
            print(f"  Accuracy: {results['accuracy']:.1%} ({results['correct']}/{results['total']})")
        
        print(f"\nTotal responses collected: {len(self.responses)}")
        print("Results saved to results/llm_testing_results.json")

def main():
    """
    Main function to run LLM testing
    """
    # Get API key from environment variable
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    if not api_key:
        print("❌ Please set OPENROUTER_API_KEY environment variable")
        print("You can get an API key from: https://openrouter.ai/")
        return
    
    # Initialize tester
    tester = LLMTester(api_key)
    
    # Run comprehensive test
    tester.run_comprehensive_test()

if __name__ == "__main__":
    main() 