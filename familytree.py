import pandas as pd
from graphviz import Digraph

# Load data from Excel
df = pd.read_excel('tree_data.xlsx')

# Convert to string and sort as necessary
df['Family'] = df['Family'].astype(str)
df['Brothers'] = df['Brothers'].astype(str)
df = df.sort_values(by='Brothers')
df = df.sort_values(by='Family')

# Create the main Digraph object
dot = Digraph(comment='The Fraternity Family Tree', format='png', engine='dot')

# Set to keep track of all processed brothers
processed_brothers = set()

# Initialize containers for brothers and littles
all_brothers = set()
all_littles = set()

# Find founders by checking who doesn't have a big
for _, row in df.iterrows():
    brother = row['Brothers'].strip()
    littles = row['Littles'].split(",") if pd.notna(row['Littles']) else []
    all_brothers.add(brother)
    all_littles.update([little.strip() for little in littles])

founders_set = all_brothers - all_littles

# Group brothers by family for creating rows
family_groups = df.groupby('Family')

for family, group in family_groups:
    # Create a subgraph for each family
    with dot.subgraph(name=f'cluster_{family}') as s:
        s.attr(rank='same')  # Set the family members on the same horizontal level
        for _, row in group.iterrows():
            brother = row['Brothers'].strip()
            family_color = row['Family'].lower().strip()
            fontcolor = 'white' if family_color in ['black', 'purple', 'blue'] else 'black'
            node_attrs = {
                'color': 'black',
                'fontcolor': fontcolor,
                'style': 'filled',
                'fillcolor': family_color,
                'penwidth': '2',
                'fontname': 'Arial'
            }
            if brother not in processed_brothers:
                s.node(brother, **node_attrs)
                processed_brothers.add(brother)

            littles = row['Littles'].split(",") if pd.notna(row['Littles']) else []
            for little in littles:
                little = little.strip()
                if little:
                    if little not in processed_brothers:
                        s.node(little, **node_attrs)
                        processed_brothers.add(little)
                    s.edge(brother, little)

# Create invisible edges between the founders to align them in rows
founders = [(brother, family) for brother, family in zip(df['Brothers'], df['Family']) if brother in founders_set]

for i in range(len(founders) - 1):
    for j in range(i + 1, len(founders)):
        if founders[i][1] == founders[j][1]:
            dot.edge(founders[i][0], founders[j][0], style='invis')

# Save or render the graph
dot.render('Theta_Tau_family_tree', view=True)