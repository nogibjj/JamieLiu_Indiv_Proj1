"""
Main cli or app entry point
"""

from mylib.lib import *

def g_describe():
    g = load_dataset()
    return g.describe()

def general_viz_combined(general_df, jupyter_render):
    """saves all the figures at once"""
    bar_visual(general_df, 'incidents_85_99', jupyter_render)
    hist_visual(general_df, 'incidents_85_99', jupyter_render)
    bar_visual(general_df, 'fatal_accidents_85_99', jupyter_render)
    hist_visual(general_df, 'fatal_accidents_85_99', jupyter_render)
    bar_visual(general_df, 'fatalities_85_99', jupyter_render)
    hist_visual(general_df, 'fatalities_85_99', jupyter_render)
    bar_visual(general_df, 'incidents_00_14', jupyter_render)
    hist_visual(general_df, 'incidents_00_14', jupyter_render)
    bar_visual(general_df, 'fatal_accidents_00_14', jupyter_render)
    hist_visual(general_df, 'fatal_accidents_00_14', jupyter_render)
    bar_visual(general_df, 'fatalities_00_14', jupyter_render)
    hist_visual(general_df, 'fatalities_00_14', jupyter_render)


def save_to_md():
    """save to markdown"""
    df = load_dataset()
    general_viz_combined(df, False)
    markdown_table = g_describe().to_markdown()
    with open ('graph.md', 'w') as file:
        file.write(f'# Report\n\n')
        file.write(f'## General Description\n\n')   
        file.write(f'{markdown_table}\n\n')
        file.write(f'## Visualizations\n\n')
        file.write(f'### Incidents 85-99\n\n')
        file.write(f'![Incidents 85-99](incidents_85_99 over Airlines.png)\n\n')
        file.write(f'![Incidents 85-99](Frequency of incidents_85_99 histogram.png)\n\n')
        file.write(f'### Fatal Accidents 85-99\n\n')
        file.write(f'![Fatal Accidents 85-99](fatal_accidents_85_99 over Airlines.png)\n\n')
        file.write(f'![Fatal Accidents 85-99](Frequency of fatal accidents_85_99 histogram.png)\n\n')
        file.write(f'### Fatalities 85-99\n\n')
        file.write(f'![Fatalities 85-99](fatalities_85_99 over Airlines.png)\n\n')
        file.write(f'![Fatalities 85-99](Frequency of fatalities_85_99 histogram.png)\n\n')
        file.write(f'### Incidents 00-14\n\n')
        file.write(f'![Incidents 00-14](incidents_00_14 over Airlines.png)\n\n')
        file.write(f'![Incidents 00-14](Frequency of incidents_00_14 histogram.png)\n\n')
        file.write(f'### Fatal Accidents 00-14\n\n')
        file.write(f'![Fatal Accidents 00-14](fatal_accidents_00_14 over Airlines.png)\n\n')
        file.write(f'![Fatal Accidents 00-14](Frequency of fatal accidents_00_14 histogram.png)\n\n')
        file.write(f'### Fatalities 00-14\n\n')
        file.write(f'![Fatalities 00-14](fatalities_00_14 over Airlines.png)\n\n')
        file.write(f'![Fatalities 00-14](Frequency of fatalities_00_14 histogram.png)\n\n')

if __name__ == "__main__":
    save_to_md()

