import pandas as pnd
import json

dataset = pnd.read_csv('../assets/PersuasionForGood/full_dialog.csv') 

groups = dataset.groupby('B2')

training_data=[]

for dialouge_id,group in groups:
    group = group.sort_values('Turn')
    turn=group.to_dict('records')

    for i in range(len(turn)-1):
        current=turn[i]
        next=turn[i+1]

        # persuadee and persuader pair
        if current['B4']==1 and next['B4']==0:
            user=current['Unit']
            ai=next['Unit']

            samples={
                "messages":[
                    {
                        "role":"system",
                        "content":"you are an negotiation and persuation expert coach"
                    },
                    {
                        "role":"user",
                        "content":f"Person says: {user} \n\n provide a strong counter arguments"
                    },
                    {
                        "role":"asistant",
                        "content":f" Counter argument: {ai}"
                    }
                ]
            }
            
            training_data.append(samples)
            

with open("training_data_pfg.jsonl",'w') as file:
    for record in training_data:
        file.write(json.dumps(record)+'\n')