import json

dataset=[]
training_data=[]

with open("train_pair_data.jsonlist") as file:
    for line in file:
        dataset.append(json.loads(line))



# .................strategy to learn model................

# input : opinion , output: strong counter argument
# input : weak argumnet + opinion , output : strong argument

for record in dataset:
    op_title=record['op_title']
    op_text=record['op_text']

    # print("type is", type(record['positive']))


    if(len(record['positive'])>0):
        samples={
            "messages":[
                {
                    "role":"system",
                    "content":"you are an expert negotiation and persuasion coach"
                },
                {
                    "role":"user",
                    "content":f"Opinion: {op_title} \n\n Explanation: {op_text}\n\n Provide strong persuasive and negotiative counterargument."
                },
                {
                    "role":"assistant",
                    "content":f"{record['positive']['comments'][0]['body']}"
                }
            ]
        }

    if len(record['positive']['comments'][0]['body'].split()) < 20: 
            continue
    training_data.append(samples)

    if(len(record['negative'])>0):
        samples={
            "messages":[
                {
                    "role":"system",
                    "content":"you are an expert negotiation and persuasion coach"
                },
                {
                    "role":"user",
                    "content":f" Opinion: {op_title} \n\n Explanation: {op_text}\n\n Weak argument: {record['negative']['comments'][0]['body']} \n\n Provide strong persuasive and negotiative argument."
                },
                {
                    "role":"assistant",
                    "content":f"{record['positive']['comments'][0]['body']}"
                }
            ]
        }
    if len(record['negative']['comments'][0]['body'].split()) < 20: 
            continue
    training_data.append(samples)


with open('training_data_cmy.jsonl','w') as file :
    for record in training_data:
        file.write(json.dumps(record)+'\n')