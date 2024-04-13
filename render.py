import streamlit as st
import re


bot_msg_container_html_template = '''
<div style='padding: 10px; border-radius: 5px; margin-bottom: 10px; display: flex; justify-content: flex-start; gap:5px'>
        <img src="data:image/jpeg;base64,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" style="max-height: 50px; max-width: 50px; border-radius: 50%; z-index:3; display: flex; justify-self: flex-start;">
    <div style="background-color: #F0F2F6; color:#262730; justify-content: center; border-radius: 8px; text-align: left; padding-top: 10px; padding-left: 25px; padding-bottom: 0px; padding-right: 20px;">
        $MSG
    </div>
</div>
'''

user_msg_container_html_template = '''
<div style='padding: 10px; border-radius: 5px; margin-bottom: 10px; display: flex; justify-content: flex-end; gap:5px'>
    <div style="width: auto; background-color: #F0F2F6; color:#262730; border-radius: 8px; padding-top: 10px; padding-left: 20px; padding-bottom: 10px; padding-right: 20px">
        $MSG
    </div>
        <img src="https://i.postimg.cc/xdFvvhbG/avatar-default.png" style="max-width: 50px; max-height: 50px; float: right; border-radius: 50%; z-index:3; display: flex; justify-self: flex-end;">   
</div>
'''

def render_article_preview(docs, tickers):
    message = f"<h5>Here are relevant articles for {tickers} that may answer your question. &nbsp; &nbsp;</h5>"
    message += "<div>"
    for d in docs:
        elipse = " ".join(d[2].split(" ")[:140])        
        message += f"<br><a href='{d[1]}'>{d[0]}</a></br>"
        message += f"<p>{elipse} ...</p>"
        message += "<br>"
    message += "</div>"
    return message

def render_earnings_summary(ticker, summary):
    transcript_title = summary["transcript_title"]
    message = f"<h5>Here is summary for {ticker} {transcript_title} </h5>"
    message += "<div>"
    body =  re.sub(r'^-', r'*  ', summary["summary"])
    body =  re.sub(r'\$', r'\\$', body)
    message += f"<p>{body}</p>"
    message += "</div>"
    return message

# def render_stock_question(answer, articles):
#     message = "<div>"
#     message += f"{answer} &nbsp; <br>"
#     message += "Sources: "
#     for a in articles:
#         message += f"<a href='{a[1]}'>{a[0]}</a><br>"
#     message += "</div>"
#     return message

def render_chat(**kwargs):
    """
    Handles is_user 
    """
    if kwargs["is_user"]:
        st.write(
            user_msg_container_html_template.replace("$MSG", kwargs["message"]),
            unsafe_allow_html=True)
    else:
        st.write(
            bot_msg_container_html_template.replace("$MSG", kwargs["message"]),
            unsafe_allow_html=True)

    if "figs" in kwargs:
        for f in kwargs["figs"]:
            st.plotly_chart(f, use_container_width=True)

