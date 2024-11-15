from streamlit_tags import st_tags
import streamlit as st

def export_vision_to_txt(core_values, core_purpose, bhag, vivid_description):
    """Create a vision statement text file."""
    vision_content = f"""
    Vision Statement
    -----------------
    **Core Values**:
    {', '.join(core_values)}

    **Core Purpose**:
    {core_purpose}

    **BHAG (Big Hairy Audacious Goal)**:
    {bhag}

    **Vivid Description**:
    {vivid_description}
    """
    return vision_content

def main():
    st.title("Vision Setting: Built to Last Framework")
    st.subheader("Define your organization's enduring vision.")

    # Core Ideology Inputs
    st.header("Core Ideology")
    core_values = st_tags(
        label="Core Values:",
        text="Press Enter after typing each value.",
        value=[],
        suggestions=["Integrity", "Innovation", "Excellence", "Teamwork"],
        maxtags=10,
        key="core_values",
    )
    core_purpose = st.text_area("What is your organization's Core Purpose?", "")

    # Envisioned Future Inputs
    st.header("Envisioned Future")
    bhag = st.text_input("What is your BHAG (Big Hairy Audacious Goal)?", "")
    vivid_description = st.text_area("Describe your envisioned future vividly:", "")

    # Preview Vision Statement
    if st.button("Preview Vision Statement"):
        st.subheader("Vision Statement Preview")
        st.write("### Core Values")
        st.write(", ".join(core_values))
        st.write("### Core Purpose")
        st.write(core_purpose)
        st.write("### BHAG")
        st.write(bhag)
        st.write("### Vivid Description")
        st.write(vivid_description)

    # Export Vision Statement
    if st.button("Export Vision Statement"):
        vision_text = export_vision_to_txt(core_values, core_purpose, bhag, vivid_description)
        st.download_button(
            label="Download Vision Statement",
            data=vision_text,
            file_name="vision_statement.txt",
            mime="text/plain",
        )

if __name__ == "__main__":
    main()
