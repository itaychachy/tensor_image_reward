import os
import torch
import TensorImageReward as RM

if __name__ == "__main__":
    prompt = "a painting of an ocean with clouds and birds, day time, low depth field effect"
    img_prefix = "/sci/labs/sagieb/itaychachy/SDS-Bridge/2D_experiments/ImageReward/assets/images"
    generations = [f"{pic_id}.webp" for pic_id in range(1, 5)]
    img_list = [os.path.join(img_prefix, img) for img in generations]
    model = RM.load("ImageReward-v1.0")
    with torch.no_grad():
        images = torch.rand((4, 3, 224, 224)).to("cuda")
        ranking, rewards = model.inference_rank(prompt, images)
        # Print the result
        print("\nPreference predictions:\n")
        print(f"ranking = {ranking}")
        print(f"rewards = {rewards}")
        # for index in range(len(img_list)):
        #     score = model.score(prompt, img_list[index])
        #     print(f"{generations[index]:>16s}: {score:.2f}")
