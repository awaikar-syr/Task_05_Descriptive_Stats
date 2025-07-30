"""
Simple test script to verify OpenRouter API setup
"""

import os
import requests
import json

def test_openrouter_setup():
    """
    Test basic OpenRouter API connectivity
    """
    print("🔧 Testing OpenRouter API Setup")
    print("=" * 40)
    
    # Check API key
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ OPENROUTER_API_KEY not found in environment variables")
        print("Please set it with: export OPENROUTER_API_KEY='your-key-here'")
        return False
    
    print(f"✅ API Key found: {api_key[:10]}...")
    
    # Test API connectivity
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Simple test prompt
    test_payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": "Say 'Hello, OpenRouter is working!'"
            }
        ],
        "max_tokens": 50
    }
    
    try:
        print("🔄 Testing API connection...")
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=test_payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            message = result["choices"][0]["message"]["content"]
            print(f"✅ API test successful!")
            print(f"Response: {message}")
            return True
        else:
            print(f"❌ API test failed: {response.status_code}")
            print(f"Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return False

def test_basketball_data():
    """
    Test basketball data loading
    """
    print("\n🏀 Testing Basketball Data Loading")
    print("=" * 40)
    
    try:
        import pandas as pd
        df = pd.read_csv("data/syracuse_womens_basketball_2023_24.csv")
        print(f"✅ Basketball data loaded successfully")
        print(f"   Players: {len(df)}")
        print(f"   Columns: {len(df.columns)}")
        print(f"   Games: {df['Games_Played'].max()}")
        return True
    except Exception as e:
        print(f"❌ Basketball data loading failed: {e}")
        return False

def main():
    """
    Run all setup tests
    """
    print("🚀 Task 05: LLM Testing Setup Verification")
    print("=" * 50)
    
    # Test OpenRouter setup
    api_ok = test_openrouter_setup()
    
    # Test basketball data
    data_ok = test_basketball_data()
    
    print("\n" + "=" * 50)
    print("📊 SETUP SUMMARY")
    print("=" * 50)
    
    if api_ok and data_ok:
        print("✅ All tests passed! Ready to run LLM testing.")
        print("\nNext steps:")
        print("1. Run: python3 scripts/llm_tester.py")
        print("2. Check results in results/llm_testing_results.json")
        print("3. Document findings in project log")
    else:
        print("❌ Some tests failed. Please fix issues before proceeding.")
        
        if not api_ok:
            print("\nAPI Issues:")
            print("- Check your OpenRouter API key")
            print("- Ensure it's set as environment variable")
            print("- Visit https://openrouter.ai/ to get a key")
            
        if not data_ok:
            print("\nData Issues:")
            print("- Ensure basketball dataset is in data/ folder")
            print("- Check file permissions")

if __name__ == "__main__":
    main() 