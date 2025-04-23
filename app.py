import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="تحليل لعبة Crash", layout="centered")

st.title("تحليل لعبة Crash 1xBet")
st.write("تحليل مبسط للنتائج وتوصيات للعب القادم")

# بيانات سابقة (مثال مبدأي)
results = [1.1, 1.3, 1.2, 1.8, 1.6, 2.0, 1.7]
rounds = list(range(1, len(results)+1))

# توقع النتيجة القادمة باستخدام الانحدار الخطي
model = LinearRegression()
model.fit(np.array(rounds).reshape(-1,1), np.array(results))
next_round = [[len(results) + 1]]
prediction = model.predict(next_round)[0]

# رسم النتائج
fig, ax = plt.subplots()
ax.plot(rounds, results, marker='o', label='النتائج السابقة')
ax.plot(len(results) + 1, prediction, 'ro', label='التوقع القادم')
ax.set_xlabel("الجولة")
ax.set_ylabel("الضرب")
ax.legend()
st.pyplot(fig)

# عرض التوقع
st.success(f"التوقع للجولة القادمة: {prediction:.2f}")

# إحصائيات
mean_result = np.mean(results)
st.info(f"المتوسط: {mean_result:.2f}")
st.info(f"أقصى نتيجة: {max(results):.2f}")
st.info(f"أقل نتيجة: {min(results):.2f}")

# توصية بسيطة
if prediction > 2:
    st.warning("احتمال كبير للهبوط! كن حذرًا.")
elif prediction > 1.5:
    st.success("فرصة جيدة للعب!")
else:
    st.info("الوضع متوسط. العب بحذر.")

st.caption("تحليل تجريبي لأغراض تعليمية فقط")
