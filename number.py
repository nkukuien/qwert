import streamlit as st

st.title("🔢 Number Type Checker")

num = st.number_input("Enter any number:")

if st.button("Check Number Type"):
    # Check Integer or Decimal
    if num % 1 == 0:
        number_type = "Integer"
    else:
        number_type = "Decimal"

    # Check Even or Odd (only for integers)
    if number_type == "Integer":
        if int(num) % 2 == 0:
            parity = "Even"
        else:
            parity = "Odd"
    else:
        parity = "Not applicable (Decimal)"

    # Check Positive, Negative, or Zero
    if num > 0:
        sign = "Positive"
    elif num < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    # Display results
    st.write(f"🔹 Type: **{number_type}**")
    st.write(f"🔹 Parity (Even/Odd): **{parity}**")
    st.write(f"🔹 Sign: **{sign}**")
