from typing import Dict
from utils.config import Language

# English strings
EN_STRINGS = {
    # Table headers
    "agent": "Agent",
    "signal": "Signal",
    "confidence": "Confidence",
    "reasoning": "Reasoning",
    "action": "Action",
    "quantity": "Quantity",
    "portfolio_summary": "PORTFOLIO SUMMARY",
    "portfolio_strategy": "Portfolio Strategy",
    "agent_analysis": "AGENT ANALYSIS",
    "trading_decision": "TRADING DECISION",
    
    # Signal types
    "bullish": "BULLISH",
    "bearish": "BEARISH",
    "neutral": "NEUTRAL",
    
    # Actions
    "buy": "BUY",
    "sell": "SELL",
    "hold": "HOLD",
    "cover": "COVER",
    "short": "SHORT",
    
    # Error messages
    "error_in_analysis": "Error in analysis, defaulting to neutral",

    # Financial metrics
    "roe": "ROE",
    "net_margin": "Net Margin",
    "op_margin": "Operating Margin",
    "revenue_growth": "Revenue Growth",
    "earnings_growth": "Earnings Growth",
    "current_ratio": "Current Ratio",
    "debt_to_equity": "Debt to Equity",
    "pe_ratio": "P/E Ratio",
    "pb_ratio": "P/B Ratio",
    "ps_ratio": "P/S Ratio",
    "na": "N/A",

    # Risk management
    "portfolio_value": "Portfolio Value",
    "current_position": "Current Position",
    "position_limit": "Position Limit",
    "remaining_limit": "Remaining Limit",
    "available_cash": "Available Cash",

    "weighted_bullish_signals": "Weighted Bullish signals",
    "weighted_bearish_signals": "Weighted Bearish signals",

    # Technical Analysis
    "trend_following": "Trend Following",
    "mean_reversion": "Mean Reversion",
    "momentum": "Momentum",
    "volatility": "Volatility",
    "statistical_arbitrage": "Statistical Arbitrage",
    "adx": "ADX",
    "trend_strength": "Trend Strength",
    "z_score": "Z-Score",
    "price_vs_bb": "Price vs Bollinger Bands",
    "rsi_14": "RSI (14)",
    "rsi_28": "RSI (28)",
    "momentum_1m": "1M Momentum",
    "momentum_3m": "3M Momentum",
    "momentum_6m": "6M Momentum",
    "volume_momentum": "Volume Momentum",
    "historical_volatility": "Historical Volatility",
    "volatility_regime": "Volatility Regime",
    "volatility_z_score": "Volatility Z-Score",
    "atr_ratio": "ATR Ratio",
    "hurst_exponent": "Hurst Exponent",
    "skewness": "Skewness",
    "kurtosis": "Kurtosis",

    # Valuation Analysis
    "intrinsic_value": "Intrinsic Value",
    "market_cap": "Market Cap",
    "valuation_gap": "Valuation Gap",
    "owner_earnings_value": "Owner Earnings Value",
    "dcf_analysis": "DCF Analysis",
    "owner_earnings_analysis": "Owner Earnings Analysis",
    "bullish_with_gap": "bullish (Undervalued)",
    "bearish_with_gap": "bearish (Overvalued)",
    "neutral_with_gap": "neutral (Fairly Valued)",
}

# Chinese strings
ZH_STRINGS = {
    # Table headers
    "agent": "分析师",
    "signal": "信号",
    "confidence": "置信度",
    "reasoning": "理由",
    "action": "操作",
    "quantity": "数量",
    "portfolio_summary": "投资组合摘要",
    "portfolio_strategy": "投资组合策略",
    "agent_analysis": "分析师分析",
    "trading_decision": "交易决策",
    
    # Signal types
    "bullish": "看涨",
    "bearish": "看跌",
    "neutral": "中性",
    
    # Actions
    "buy": "买入",
    "sell": "卖出",
    "hold": "持有",
    "cover": "平仓",
    "short": "做空",
    
    # Error messages
    "error_in_analysis": "分析出错，使用默认值",

    # Financial metrics
    "roe": "净资产收益率",
    "net_margin": "净利率",
    "op_margin": "营业利润率",
    "revenue_growth": "营收增长率",
    "earnings_growth": "盈利增长率",
    "current_ratio": "流动比率",
    "debt_to_equity": "负债权益比",
    "pe_ratio": "市盈率",
    "pb_ratio": "市净率",
    "ps_ratio": "市销率",
    "na": "无数据",

    # Risk management
    "portfolio_value": "总资本",
    "current_position": "当前持仓",
    "position_limit": "持仓限制",
    "remaining_limit": "剩余限制",
    "available_cash": "可用现金",

    "weighted_bullish_signals": "看涨信号权重",
    "weighted_bearish_signals": "看跌信号权重",

    # Technical Analysis
    "trend_following": "趋势跟踪",
    "mean_reversion": "均值回归",
    "momentum": "动量",
    "volatility": "波动性",
    "statistical_arbitrage": "统计套利",
    "adx": "平均趋向指标",
    "trend_strength": "趋势强度",
    "z_score": "Z分数",
    "price_vs_bb": "价格vs布林带",
    "rsi_14": "RSI (14)",
    "rsi_28": "RSI (28)",
    "momentum_1m": "1月动量",
    "momentum_3m": "3月动量",
    "momentum_6m": "6月动量",
    "volume_momentum": "成交量动量",
    "historical_volatility": "历史波动率",
    "volatility_regime": "波动率状态",
    "volatility_z_score": "波动率Z分数",
    "atr_ratio": "ATR比率",
    "hurst_exponent": "赫斯特指数",
    "skewness": "偏度",
    "kurtosis": "峰度",

    # Valuation Analysis
    "intrinsic_value": "内在价值",
    "market_cap": "市值",
    "valuation_gap": "估值差距",
    "owner_earnings_value": "所有者收益价值",
    "dcf_analysis": "现金流折现分析",
    "owner_earnings_analysis": "所有者收益分析",
    "bullish_with_gap": "看涨(低估)",
    "bearish_with_gap": "看跌(高估)",
    "neutral_with_gap": "中性(合理估值)",
}

def get_string(key: str, language: Language = Language.ENGLISH) -> str:
    """Get a localized string based on the current language setting."""
    strings = ZH_STRINGS if language == Language.CHINESE else EN_STRINGS
    return strings.get(key, key) 