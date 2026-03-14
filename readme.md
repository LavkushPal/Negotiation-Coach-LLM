<h1> Negotiation & Persuasion Coach LLM System </h1>



<h3> Your Negotiation Coach LLM should learn: </h3>

1. persuasion techniques
2. counter arguments (negotiation)
3. conversational negotiation and persuasion


<h3> Required Steps -- </h3>

1. Setup environment
2. Choose base model
3. Run baseline inference
4. Collect datasets
5. Design dataset schema, synthetic data creation
6. Clean & preprocess dataset
7. Fine-tune using QLoRA
8. Evaluate base vs fine-tuned model
9. Deploy with vLLM
10. Build FastAPI backend
11. Build UI
12. Performance optimization



<h3> Task Completed -- </h3>

1. setup and configuration 
2. base model selection : Llama-3.1-8B
3. finetuning knowledge refinement
4. baseline inference (require access permission)
5. dataset collection : ChangeMyView , PersuasionForGood, CaSiNo (Negotiation + Persuasion) 
6. dataset formating : cmy-6912(ChangeMyView), pfg-9583(PersuasionForGood), casino-6966(CaSiNo) - total : 23461 rows in training data
7. SFT(finetuning) training setup and configuration
8. dataset shuffled and splitted to training,validation,testing
9. parameters are finally configured, ready to train our QLoRA model
10. failed(crashes) to download model again and again due to unsufficient available RAM 
11.  again trying : crashed again after downloading 47 percent from disk
12. optimization : direct download to disk, off load gpu into cpu , max seq length reduction 2048 to 1024, batch    size reduction 4 to 1, max positin embedding reduction 8192 to 2048...
13. those optimization still not sufficient so ...................shiting to Llama-3.2-1B



<h3> Encountered issues and challanges -- </h3>

1. Available colab RAM crash during basse model download(12-13 GB)
    1. download quantized base model directly in GPU instead of CPU to GPU (by providing parameter low-cpu-use)
    2. download quantized base model directly in disk then load it to GPU (by using snapshot download)
    3. enable gpu offload to utilize cpu memory too (GPU VRAM is not sufficient(14.56 GB)) 


<h3> Optimization and improvement -- </h3>

1. train on synthetic data
2. train model to ask at most 3 follow ups
3. build system architecture
4. evaluation of responses
5. show up numbers optimized by x percentage
6. organize readme(documentation) in a proper way


