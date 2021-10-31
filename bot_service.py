from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# cache_dir - caching path parameter
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium", cache_dir="microsoft_dialogpt_cached_token/")
# Save downloaded tokenizer
tokenizer.save_pretrained("microsoft_dialogpt")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium", cache_dir="microsoft_dialogpt_cached_model/")
# Save downloaded model
model.save_pretrained("microsoft_dialogpt")

history_messages_ids = {} # Save user uds history


def get_message(input_str, uid):
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizer.encode(input_str + tokenizer.eos_token, return_tensors='pt')

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([history_messages_ids[uid], new_user_input_ids],
                              dim=-1) if uid in history_messages_ids else new_user_input_ids

    # generated a response while limiting the total chat history to 1000 tokens,
    history_messages_ids[uid] = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # pretty print last ouput tokens from bot
    return tokenizer.decode(history_messages_ids[uid][:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
