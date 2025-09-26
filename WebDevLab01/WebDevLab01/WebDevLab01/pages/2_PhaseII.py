import streamlit as st


st.write("Find your ideal country!")

st.image("C:\Elijah\Cs1301\WebDevLab01\WebDevLab01\WebDevLab01\Images\japan.png", caption="Japan", width=50)
st.image("C:\Elijah\Cs1301\WebDevLab01\WebDevLab01\WebDevLab01\Images\italy.png", caption="Italy", width=50)
st.image("C:\Elijah\Cs1301\WebDevLab01\WebDevLab01\WebDevLab01\Images\canada.png", caption="Canada", width=50)


climate = st.radio("Preferred climate:", ["Cold", "Mild", "Warm"])  #NEW
food = st.selectbox("Food you like most:", ["Sushi", "Pasta", "Burgers"])  #NEW
hobbies = st.multiselect("Activities you enjoy:", ["Hiking", "Museums", "Beaches"])  #NEW
vibe = st.slider("Nature ⟵⟶ City (0–10):", 0, 10, 5)  #NEW
budget = st.number_input("Monthly budget (USD):", 500, 8000, 2500, step=100)  #NEW

jp=0
it=0
ca=0
if climate == "Cold": ca += 1
elif climate == "Mild": jp += 1
else: it += 1
if food == "Sushi": jp += 1
elif food == "Pasta": it += 1
else: ca += 1
if "Hiking" in hobbies: ca += 1
if "Museums" in hobbies: jp += 1
if "Beaches" in hobbies: it += 1
if vibe <= 3: ca += 1
elif vibe >= 7: jp += 1
else: it += 1
if budget < 1800: ca += 1
elif budget <= 3500: it += 1
else: jp += 1
result, points = "Japan", jp
if it > points: result, points = "Italy", it
if ca > points: result, points = "Canada", ca

if st.button("Show my country"):
    st.metric("Match score", f"{points}/5")  #NEW
    st.success(f"Your ideal country is **{result}**!")
    if result == "Japan":
        st.image("C:\Elijah\Cs1301\WebDevLab01\WebDevLab01\WebDevLab01\Images\japan.png", width=160)
    elif result == "Italy":
        st.image("C:\Elijah\Cs1301\WebDevLab01\WebDevLab01\WebDevLab01\Images\italy.png", width=160)
    else:
        st.image("C:\Elijah\Cs1301\WebDevLab01\WebDevLab01\WebDevLab01\Images\canada.png", width=160)
    st.balloons()  #NEW
