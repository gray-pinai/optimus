# 配置文件
CONFIG = {
    "twitter_api": {
        "api_key": "yPffO0DYLZgeqbHy00hRxQ23X",
        "api_secret": "fnklqNA17QX1lxpwwEkTYYO88gSNUtpDY9VvsaivuJiNcpSJJQ",
        "access_token": "1860211181652443144-2oT3ZpETdd8J9WaHzCR7nqcqWLQWpo",
        "access_token_secret": "NF6lOLJE9xQUrSdOSX2J38Kbsd5J4npjuL60FZ3VJwKM3",
        "bearer_token": "AAAAAAAAAAAAAAAAAAAAAJKHxAEAAAAAQjcxVZ92OAqv3yfxf8PyWG6RbUw%3DVFOZQSEcBiORAglz6zd5Tw2obvNnwEsSn81FAIG28ousGN6lYC"
    },
    "openai_api": {
        "api_key": "sk-proj-tEK0BXGxntlXBmuiCTNjT3BlbkFJiVBaJ3my0TPrGCIyM4eZ"
    },
    "bot_settings": {
        "check_interval": 300,  # 5分钟
        "analysis_interval": 3600,  # 1小时
        "domain": "crypto",  # 机器人领域
        "key_accounts": [  # 需要关注的关键账号
            "VitalikButerin",
            "cz_binance",
            # ... 其他关键账号
        ]
    },
    "prompt": {
        "en-US": {
            "summary": """You are a data analysis assistant specializing in cryptocurrency markets and social media trends. The following dataset contains tweets from key influencers and participants in the cryptocurrency trading industry. The tweets span the past [timeframe, e.g., 3 months] and include discussions on market trends, predictions, major events, and opinions on regulations.
                       Your task:
                       - Summarize the key themes and insights from these tweets.
                       - Identify recent trends and any emerging patterns in the cryptocurrency market as reflected in the data.
                       - Highlight any critical or notable opinions, shifts in sentiment, or influential moments shared by the participants.
                       - Make your analysis concise but comprehensive, with clear headings or bullet points for each finding
                       At last, please limit the number of words to 220.""",     
        },
        "zh-CN": {
            "summary": """你是一名专注于加密货币市场和社交媒体趋势的数据分析助手。以下数据集包含来自加密货币交易领域关键人物和参与者的推文，这些推文涵盖了过去【时间范围，例如3个月】内的市场趋势、预测、重大事件和对政策法规的讨论。
                        你的任务是：
                        - 总结这些推文的主要主题和核心见解。
                        - 识别加密货币市场中近期的趋势及数据中反映的新兴模式。
                        - 突出参与者提到的任何关键或值得注意的观点、情绪变化以及影响较大的事件。
                        - 请将分析简明扼要，但内容全面，并用清晰的标题或要点列出主要发现。
                        最后，请将字数限制在220字以内
                       """
        }
    },
    "mysql": {
        "host": "127.0.0.1",
        "user": "root",
        "password": "www234root",
        "database": "aigod",
        "port": 3306
    }
} 