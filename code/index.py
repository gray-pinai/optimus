import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from llm.openai import OpenAIComponent
from twitter.service import TwitterService

app = FastAPI()


@app.get('/send_tweet')
async def send_tweet():
    openAI = OpenAIComponent()
    tweet_content = await openAI.generate_response(
        '''You are an AI Twitter account named Optimus. Please generate a tweet, without any extra unnecessary text, with the goal of attracting more engagement through fun and sarcastic content. The tweet should have the following characteristics:
Content: Rich and substantial.
Sarcasm & Humor: Make readers feel both teased and amused.
Engagement: Ask questions, reverse common opinions, or mock awkward moments from daily life to spark discussion.
Lighthearted & Fun: Keep the tone relaxed and easy to share, encouraging retweets and comments.'''
    )
    twitter_service = TwitterService()
    response = await twitter_service.send(content=tweet_content)
    return {"message": tweet_content, "response": response}


@app.get('/')
async def hello():
    return HTMLResponse('''<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>Serverless Devs - Powered By Serverless Devs</title>
    <link href="https://example-static.oss-cn-beijing.aliyuncs.com/web-framework/style.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<div class="website">
    <div class="ri-t">
        <h1>Devsapp</h1>
        <h2>这是一个 FastAPI 项目</h2>
        <span>自豪的通过Serverless Devs进行部署</span>
        <br/>
        <p>您也可以快速体验： <br/>
            • 下载Serverless Devs工具：npm install @serverless-devs/s<br/>
            • 初始化项目：s init start-fastapi<br/>

            • 项目部署：s deploy<br/>
            <br/>
            Serverless Devs 钉钉交流群：33947367
        </p>
    </div>
</div>
</body>
</html>
''')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
