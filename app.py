# from langchain_openai import ChatOpenAI

# from langchain.schema import SystemMessage, HumanMessage

# llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# messages = [

#     SystemMessage(content="あなたは優秀なITエンジニアと健康アドバイザーです。ユーザーの質問に対して、的確に答えてください。"),

#     HumanMessage(content={input})
# ]

# result = llm(messages)





# from dotenv import load_dotenv

# load_dotenv()



# import streamlit as st

# st.title("LLM専門家相談アプリ")

# st.write("##### 動作モード1: IT関連での質問に答える")
# st.write("IT関連の質問に対して、LLMを用いて回答します。")
# st.write("##### 動作モード2: 健康関連での質問に答える")
# st.write("健康関連の質問に対して、LLMを用いて回答します。")


# selected_item = st.radio(
#     "動作モードを選択してください。",
#     ["IT関連", "健康関連"]
# )

# st.divider()

# if selected_item == "IT関連":
#     input_message = st.text_input(label="質問を入力してください。")
    

# else:
#     input_message = st.text_input(label="質問を入力してください。")
    
# if st.button("実行"):
#     st.divider()

#     if selected_item == "IT関連":
#         if input_message:
#             return result.content

#         else:
#             st.error("質問を入力してください。")

#     else:
#         if input_massage:
#             return result.content

#         else:
#             st.error("質問を入力してください。")
            
            
            
import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# --- APIキーの読み込み ---
load_dotenv()
# OPENAI_API_KEY は .env または Streamlit Secrets に設定しておく
# ChatOpenAI は自動で APIキーを読み込む

# --- LLMの関数を定義 ---
def get_expert_answer(input_text: str, expert_type: str) -> str:
    """入力テキストと専門家の種類を受け取り、LLMの回答を返す"""

    # 専門家の種類に応じてシステムメッセージを切り替える
    if expert_type == "IT関連":
        system_prompt = "あなたは優秀なITエンジニアです。ユーザーのIT関連の質問に対して、わかりやすく答えてください。"
    elif expert_type == "健康関連":
        system_prompt = "あなたは経験豊富な健康アドバイザーです。ユーザーの健康に関する質問に対して、正確で安全なアドバイスをしてください。ただし診断や治療は行わず、一般的な助言にとどめてください。"
    else:
        system_prompt = "あなたは親切なアシスタントです。ユーザーの質問に答えてください。"

    # LLMインスタンスを作成
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    # メッセージを準備
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=input_text)
    ]

    # LLMから回答を取得
    result = llm(messages)
    return result.content


# --- Streamlit UI部分 ---
st.title("💡 LLM専門家相談アプリ")

st.write("このアプリでは、以下の2種類の専門家に質問できます。")
st.write("- **IT関連**: プログラミングやツールに関する質問に答えます。")
st.write("- **健康関連**: 健康や生活習慣についてアドバイスします。")

# ラジオボタンで選択
selected_item = st.radio(
    "専門家の種類を選んでください：",
    ["IT関連", "健康関連"]
)

# 入力フォーム
input_message = st.text_input("質問を入力してください:")

# 実行ボタン
if st.button("実行"):
    st.divider()

    if input_message:
        answer = get_expert_answer(input_message, selected_item)
        st.subheader("🔎 回答結果")
        st.write(answer)
    else:
        st.error("質問を入力してください。")