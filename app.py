import streamlit as st
import re

# Title
st.title("Password Strength Checker")

# Description
st.markdown("""
    Welcome to the **Ultimate Password Strength Checker!**
    Ensure your password is secure by checking:
    - ✅ Length
    - ✅ Upper & Lowercase letters
    - ✅ Numbers
    - ✅ Special characters  
            *Improve your password strength by creating a strong password*
""")

# Input field for password
password = st.text_input("Enter your password:", type="password")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    # Uppercase and lowercase letters check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password must contain both uppercase and lowercase letters.")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password must contain at least one digit.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Password must contain at least one special character.")

    return score, feedback

# Button
if st.button("Check Password Strength"):
    if password:
        score, feedback = check_password_strength(password)
        st.write(f"**Password Strength Score:** {score}/4")
        if score == 4:
            st.success("✅ Your password is strong!")
        elif score == 3:
            st.warning("⚠️ Your password is moderate. Consider adding more complexity.")
        elif score == 2:
            st.warning("⚠️ Your password is weak. Please improve it.")
        else:
            st.error("❌ Your password is very weak. Strongly consider changing it.")

        if feedback:
            st.info("**Suggestions to improve your password:**")
            for tips in feedback:
                st.write(f"- {tips}")
    else:
        st.error("Please enter a password to check its strength.")

# Footer
st.markdown("""
    ---
    Made with ❤️ by ***Khubaib Mustafa***
""")
