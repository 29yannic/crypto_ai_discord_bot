import pandas_ta as ta

def compute_indicators(df):
    df['rsi'] = ta.rsi(df['close'], length=14)
    macd = ta.macd(df['close'])
    df['macd'] = macd['MACD_12_26_9']
    return df

def summarize_data(df, indicators):
    return f"Latest Close: {df['close'].iloc[-1]}, RSI: {df['rsi'].iloc[-1]}, MACD: {df['macd'].iloc[-1]}"
