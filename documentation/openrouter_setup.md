# OpenRouter API Setup Guide
## Testing Multiple LLMs for Task 05

### Why OpenRouter API?

Based on the task instructions, you need to test **multiple LLMs**:
- **Line 5:** "large language model like Co-Pilot, **Claud**, or **ChatGPT**"
- The research nature requires comparing different models' performance
- OpenRouter provides access to multiple LLMs through a single API

### Available Models Through OpenRouter

Our testing framework includes these models (optimized for cost efficiency):

1. **Cheapest Models (Recommended for Testing):**
   - `mistralai/mistral-7b-instruct` - Mistral 7B (~$0.0002 per 1K tokens)
   - `meta-llama/llama-2-7b-chat` - Llama 2 7B (~$0.0002 per 1K tokens)
   - `meta-llama/llama-2-13b-chat` - Llama 2 13B (~$0.0003 per 1K tokens)

2. **Very Affordable Models:**
   - `google/gemini-pro` - Google Gemini Pro (~$0.0005 per 1K tokens)
   - `openai/gpt-3.5-turbo` - GPT-3.5 Turbo (~$0.0015 per 1K tokens)
   - `anthropic/claude-3-haiku` - Claude 3 Haiku (~$0.0025 per 1K tokens)

3. **Premium Models (for comparison):**
   - `anthropic/claude-3-opus` - Claude 3 Opus (~$0.015 per 1K tokens)
   - `openai/gpt-4` - GPT-4 (~$0.03 per 1K tokens)

### Step-by-Step Setup

#### 1. Get OpenRouter API Key

1. **Visit:** https://openrouter.ai/
2. **Sign up** for a free account
3. **Navigate** to API Keys section
4. **Create** a new API key
5. **Copy** the API key (starts with `sk-or-`)

#### 2. Set Environment Variable

**On macOS/Linux:**
```bash
export OPENROUTER_API_KEY="sk-or-your-api-key-here"
```

**On Windows:**
```cmd
set OPENROUTER_API_KEY=sk-or-your-api-key-here
```

**For permanent setup, add to your shell profile:**
```bash
# Add to ~/.zshrc or ~/.bash_profile
echo 'export OPENROUTER_API_KEY="sk-or-your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

#### 3. Install Required Dependencies

```bash
pip install requests pandas
```

#### 4. Test the Setup

```bash
python3 scripts/llm_tester.py
```

### Testing Strategy

#### Phase 1: Basic Questions (Expected High Accuracy)
- How many players are on the team?
- Who is the leading scorer?
- What is the team's record?

**Models to test:** Mistral 7B, Llama 2 7B, Gemini Pro (cheapest options)

#### Phase 2: Intermediate Questions (Testing Analysis)
- Who are the top 3 scorers?
- Which position has highest average points?
- Who has the most rebounds per game?

**Models to test:** Mistral 7B, Gemini Pro, GPT-3.5 Turbo (affordable options)

#### Phase 3: Advanced Questions (Complex Analysis)
- Define methodology for "most improved player"
- Strategic coaching decisions
- Offense vs defense focus

**Models to test:** Mistral 7B, Gemini Pro, GPT-3.5 Turbo (affordable options)

### Cost Management

OpenRouter pricing (approximate):
- **Mistral 7B:** ~$0.0002 per 1K tokens (cheapest)
- **Llama 2 7B:** ~$0.0002 per 1K tokens (cheapest)
- **Llama 2 13B:** ~$0.0003 per 1K tokens
- **Gemini Pro:** ~$0.0005 per 1K tokens
- **GPT-3.5 Turbo:** ~$0.0015 per 1K tokens
- **Claude 3 Haiku:** ~$0.0025 per 1K tokens
- **Claude 3 Opus:** ~$0.015 per 1K tokens
- **GPT-4:** ~$0.03 per 1K tokens (most expensive)

**Estimated cost for full testing with cheapest models:** $0.50-1.00
**Estimated cost for full testing with premium models:** $5-10

### Expected Results

#### Basic Questions
- **Expected Accuracy:** 90%+
- **Models should easily answer:** Player counts, basic stats, team record

#### Intermediate Questions
- **Expected Accuracy:** 70-80%
- **Challenges:** May need to analyze multiple data points

#### Advanced Questions
- **Expected Accuracy:** 50-70%
- **Challenges:** Requires complex reasoning and methodology development

### Research Value

Testing multiple LLMs provides:

1. **Comparative Analysis:**
   - Which models excel at basic vs complex questions?
   - How do different models approach the same problem?

2. **Prompt Engineering Insights:**
   - What works for one model may not work for another
   - Different models may require different prompt strategies

3. **Research Documentation:**
   - Document both successes and failures
   - Note areas where LLMs struggle
   - Identify model-specific strengths

### Troubleshooting

#### Common Issues:

1. **API Key Not Found:**
   ```bash
   echo $OPENROUTER_API_KEY
   # Should show your API key
   ```

2. **Rate Limiting:**
   - The script includes 1-second delays between requests
   - If you hit limits, increase the delay

3. **Model Availability:**
   - Some models may be temporarily unavailable
   - The script will skip unavailable models

4. **Token Limits:**
   - Basketball dataset is small (~2K tokens)
   - Should fit within all model limits

### Next Steps After Setup

1. **Run Initial Test:**
   ```bash
   python3 scripts/llm_tester.py
   ```

2. **Review Results:**
   - Check `results/llm_testing_results.json`
   - Analyze accuracy by model and question type

3. **Document Findings:**
   - Update project log with results
   - Note prompt engineering strategies that work
   - Document model-specific behaviors

4. **Iterate and Improve:**
   - Refine prompts based on results
   - Test additional question types
   - Experiment with different prompt formats

### Research Questions to Answer

1. **Model Comparison:**
   - Which model performs best on basic questions?
   - Which model handles complex analysis better?
   - Are there consistent patterns across question types?

2. **Prompt Engineering:**
   - What prompt strategies work best?
   - Do different models require different approaches?
   - How does context affect accuracy?

3. **Basketball Analysis:**
   - Can LLMs accurately analyze sports data?
   - How well do they handle statistical reasoning?
   - Can they provide meaningful coaching insights?

---

**Ready to start testing!** Set up your API key and run the testing framework to begin your LLM research. 