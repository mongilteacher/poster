import os
from openai import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


st.title('🎁 제품 홍보 포스터 생성기')
keyword = st.text_input("키워드를 입력하세요.")

if st.button('생성하기🔥'):
    with st.spinner('생성 중입니다.'):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "입력 받은 키워드에 대한 150자 이내의 솔깃한 제품 홍보 문구를 작성해줘.",
                },
                {
                    "role": "user",
                    "content": keyword,
                }

            ],
            model="gpt-4",
        )

        result = chat_completion.choices[0].message.content
        st.write(result)
    with st.spinner('이미지 생성 중입니다.'):
        response = client.images.generate(
            model="dall-e-3",
            prompt=keyword,
            size="1024x1024",
            n=1
        )

        result = chat_completion.choices[0].message.content
        image_url = response.data[0].url
        st.image(image_url)