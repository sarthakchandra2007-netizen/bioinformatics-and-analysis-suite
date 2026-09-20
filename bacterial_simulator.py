import numpy as np
import pandas as pd
import streamlit as st


def render_bacterial_simulator():
    st.header("🔬 Universal Bacterial Growth Curve Analyzer")
    st.caption(
        "Drag and drop any lab spreadsheet to visualize data and calculate growth kinetics."
    )

    # Dynamic File Uploader Box
    uploaded_file = st.file_uploader(
        "📂 Upload your lab Excel file (.xlsx) or CSV file:",
        type=["xlsx", "csv"],
        key="bacterial_file_uploader",
    )

    # Read the Data Only If a File is Uploaded
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            st.success("🎉 File uploaded successfully!")
        except Exception as e:
            st.error(f"Error reading the file: {e}")
            return

        # Control Panel (Inline instead of Sidebar)
        all_columns = list(df.columns)
        x_axis = st.selectbox(
            "Select X-Axis Column (Time):",
            options=all_columns,
            index=0,
            key="bac_x_axis",
        )

        remaining_columns = [col for col in all_columns if col != x_axis]
        strain_choice = st.multiselect(
            "Select Columns to Plot (Y-Axis):",
            options=remaining_columns,
            default=remaining_columns[:2]
            if len(remaining_columns) >= 2
            else remaining_columns,
            key="bac_strain_choice",
        )

        # Build Layout Columns for Visualization
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f"### 📈 Interactive Chart ({', '.join(strain_choice)} over {x_axis})"
            )
            if strain_choice:
                st.line_chart(data=df, x=x_axis, y=strain_choice)
            else:
                st.warning("Please select at least one data column to plot.")

        with col2:
            st.markdown("### 📊 Interactive Lab Dataset Grid")
            display_cols = [x_axis] + strain_choice
            st.dataframe(df[display_cols], hide_index=True)

        # KINETICS METRICS BLOCK
        if strain_choice:
            st.markdown("---")
            st.markdown("### 🧬 Automated Growth Kinetics Calculations")
            st.caption(
                "Calculations are derived by finding the steepest exponential growth segment (Log Phase)."
            )

            metric_cols = st.columns(len(strain_choice))
            df_sorted = df.sort_values(by=x_axis).copy()

            for i, strain in enumerate(strain_choice):
                with metric_cols[i]:
                    st.markdown(f"#### **{strain}**")

                    t = df_sorted[x_axis].values
                    od = df_sorted[strain].values

                    if len(t) > 2 and np.all(od > 0):
                        ln_od = np.log(od)
                        delta_ln_od = np.diff(ln_od)
                        delta_t = np.diff(t)

                        delta_t[delta_t == 0] = 0.001
                        growth_rates = delta_ln_od / delta_t
                        mu_max = np.max(growth_rates)

                        if mu_max > 0:
                            doubling_time = np.log(2) / mu_max
                            st.metric(
                                label="Max Growth Rate (μ_max)",
                                value=f"{mu_max:.3f} h⁻¹",
                            )
                            st.metric(
                                label="Doubling Time (t_d)",
                                value=f"{doubling_time:.2f} hours",
                            )
                        else:
                            st.warning("No positive growth detected.")
                    else:
                        st.error(
                            "Data requires positive numerical values to perform log transformations."
                        )

    else:
        st.info(
            "💡 Waiting for a file to be uploaded. Drag and drop your lab spreadsheet here to test it!"
        )