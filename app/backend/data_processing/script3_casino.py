import json

training_data=[]

with open('../assets/CaSiNo/data/casino_complete.json','r') as file:
    dataset=json.load(file)

    for i in range(len(dataset)):
        chat_list=dataset[i]['chat_logs']
        for i in range(len(chat_list)-1):
            user=chat_list[i]['text']
            ai=chat_list[i+1]['text']

            if (i&1)==False :
                samples={
                    "messages":[
                        {
                            "role":"system",
                            "content":"you are an expert negotiation and persuasion coach"
                        },
                        {
                            "role":"user",
                            "content":f" Argument : {user} \n\n Persuade and Negotiate to argument by giving Strong Counter arguments"
                        },
                        {
                            "role":"asistant",
                            "content":f" Here is strong negotiation strategy : {ai} "
                        }
                    ]
                }

                training_data.append(samples)



with open('training_data_casino.jsonl','w') as file:
    for record in training_data:
        file.write(json.dumps(record) + '\n')



        
