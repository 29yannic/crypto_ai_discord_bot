# Crypto AI Discord Bot

A Discord bot that analyzes cryptocurrency charts using AI and technical analysis.

## Features
- Fetches latest crypto data from Binance
- Computes RSI and MACD indicators
- Uses GPT-4 to generate risk and trade setup insights
- Interacts via Discord

## Setup
1. Clone repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your `.env` file:
   ```env
   DISCORD_TOKEN=your_discord_token
   OPENAI_API_KEY=your_openai_key
   ```
4. Run bot:
   ```bash
   python bot.py
   ```

## Commands
- `!analyze BTC/USDT` – Returns insights on the selected trading pair.

## Future Work
- Chart rendering
- Sentiment analysis
- Price alerts

MIT License
