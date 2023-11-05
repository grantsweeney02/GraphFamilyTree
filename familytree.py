import pandas as pd
from graphviz import Digraph

df = pd.read_excel('tree_data.xlsx')
df['Family'] = df['Family'].astype(str)
df['Brothers'] = df['Brothers'].astype(str)
df = df.sort_values(by='Brothers')
df = df.sort_values(by='Family')
dot = Digraph(comment='The Fraternity Family Tree', format='png', engine='dot')
processed_brothers = set()
all_brothers = set()
all_littles = set()
for _, row in df.iterrows():
    brother = str(row['Brothers']) if pd.notna(row['Brothers']) else ""
    littles = str(row['Littles']).split(",") if pd.notna(row['Littles']) else []
    all_brothers.add(brother)
    all_littles.update([little.strip() for little in littles])
founders_set = all_brothers - all_littles
founders = []
for _, row in df.iterrows():
    brother = str(row['Brothers']) if pd.notna(row['Brothers']) else ""
    family_color = str(row['Family']) if pd.notna(row['Family']) else "red"
    family_color = family_color.lower().strip()

    fontcolor = 'white' if family_color == 'black' or family_color == 'purple' or family_color == 'blue' else 'black'
    node_attrs = {'color': 'black', 'fontcolor': fontcolor, 'style': 'filled', 'fillcolor': family_color, 'penwidth': '2', 'fontname': 'Arial'}
    
    if brother not in processed_brothers:
        dot.node(brother, **node_attrs)
        processed_brothers.add(brother)
        if brother in founders_set:
            founders.append((brother, family_color))

    littles = str(row['Littles']).split(",") if pd.notna(row['Littles']) else []  # Assuming littles are comma-separated
    for little in littles:
        little = little.strip()
        if little:
            if little not in processed_brothers:
                dot.node(little, **node_attrs)
                processed_brothers.add(little)
            dot.edge(brother, little)

for i, (founder1, color1) in enumerate(founders):
    for j, (founder2, color2) in enumerate(founders):
        if i < j and color1 == color2:
            dot.edge(founder1, founder2, style='invis')
dot.render('Theta_Tau_family_tree', view=True)
