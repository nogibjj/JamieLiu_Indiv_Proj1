import os
import pandas as pd
from main import g_describe, general_viz_combined, save_to_md
from mylib.lib import load_dataset


def test_g_describe():
    """Test the g_describe function."""
    print("Testing g_describe...")
    description = g_describe()
    assert isinstance(description, pd.DataFrame), "g_describe should return a DataFrame"
    assert (
        "incidents_85_99" in description.columns
    ), "DataFrame should contain 'incidents_85_99' column"
    print("g_describe passed the test.\n")


def test_general_viz_combined():
    """Test the general_viz_combined function."""
    print("Testing general_viz_combined...")
    df = load_dataset()

    # Ensure the function runs without errors (basic test)
    try:
        general_viz_combined(df, jupyter_render=False)
        print("general_viz_combined executed without errors.")
    except Exception as e:
        print(f"general_viz_combined raised an error: {e}")

    # Check if the figures are generated
    files_to_check = [
        "incidents_85_99.png",
        "Frequency_incidents_85_99_hist.png",
        "fatal_accidents_85_99.png",
        "Frequency_fatal_accidents_85_99_hist.png",
        "fatalities_85_99.png",
        "Frequency_fatalities_85_99_hist.png",
        "incidents_00_14.png",
        "Frequency_incidents_00_14_hist.png",
        "fatal_accidents_00_14.png",
        "Frequency_fatal_accidents_00_14_hist.png",
        "fatalities_00_14.png",
        "Frequency_fatalities_00_14_hist.png",
    ]

    for file in files_to_check:
        assert os.path.exists(
            file
        ), f"File {file} was not generated by general_viz_combined"

    print("general_viz_combined passed the test.\n")


def test_save_to_md():
    """Test the save_to_md function."""
    print("Testing save_to_md...")

    # Ensure the function runs and generates the markdown file without errors
    try:
        save_to_md()
        print("save_to_md executed without errors.")
    except Exception as e:
        print(f"save_to_md raised an error: {e}")

    # Check if the markdown file is generated
    assert os.path.exists("report.md"), "graph.md file was not created by save_to_md"

    print("save_to_md passed the test.\n")


if __name__ == "__main__":
    # Run tests
    test_g_describe()
    test_general_viz_combined()
    test_save_to_md()
