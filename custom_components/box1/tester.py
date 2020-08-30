import Tree
import pandas as pd

tree = Tree.DecisionTree()

print(tree.train_and_validate('CSV_txt.txt'))
#{'col1': [1, 2], 'col2': [3, 4]}
#df = {'user': ["user_rick"], 'address' : ["304_perry_street"] ,'action' : ["lights_livingroom_on"], 'time' : ["080000"], 'date' : ["09302019"] , 'weekday' : ["monday"] , 'holiday' : ["0"]}
df = {'action' : ["lights_livingroom_on"], 'time' : ["080000"], 'weekday' : ["monday"] , 'holiday' : ["0"]}
df = pd.DataFrame(data=df)
print(tree.predict(df))