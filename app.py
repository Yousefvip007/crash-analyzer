import streamlit as st

def analyze_crash_data(crash_values):
    if len(crash_values) < 5:
        return "ادخل على الأقل 5 نتائج كراش للتحليل."

    avg = sum(crash_values) / len(crash_values)
    low_crashes = [x for x in crash_values if x < 1.5]
    low_ratio = len(low_crashes) / len(crash_values)

    recommendation = "اسحب عند 1.8x أو أقل."
    if low_ratio > 0.6:
        recommendation = "احترس! نسبة الكراش السريع عالية، اسحب عند 1.3x أو أقل."
    elif low_ratio < 0.3:
        recommendation = "فرص جيدة للربح! ممكن تسحب عند 2.0x أو أكتر بحذر."

    result = f"""### التحليل:
- **المتوسط:** {avg:.2f}
- **نسبة الكراش تحت 1.5x:** {low_ratio*100:.1f}%
- **التوصية:** {recommendation}
"""
    return result

st.title("أداة تحليل لعبة Crash")

user_input = st.text_input("اكتب نتائج الكراش مفصولة بفواصل (مثال: 1.2, 2.1, 1.4, 1.8)")

if user_input:
    try:
        crash_values = [float(x.strip()) for x in user_input.split(",") if x.strip()]
        result = analyze_crash_data(crash_values)
        st.markdown(result)
    except:
        st.error("تأكد إنك كتبت الأرقام بشكل صحيح ومفصولة بفواصل.")
