# Tuning whisper model on swedish speach 
## Feature Pipeline:
We started with refactoring the code into two separate files: Feature_pipline and Training_pipeline. In the feature pipeline, we created the features and labels which eas stored on gdrive. 

## Training Pipeline
For the training pipeline, we used the GPU on colab and we saved the checkpoints to a drive folder. We then pushed the final model to huggingface so it could be accessible. 

## Huggingface UI 
On huggingface, we fixed the UI interface having two options; Voice to text and video to the text where you can submit any youtube video. 

![Huggingface interface]([https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true](https://github.com/DavidKrugerT/scalable_lab2/blob/main/Huggingface_UI.png)

## Hyperparameter tuning
For the last task we tried hyperparameter tuning with ray[tune] but colab wouldn't give us memory nor GPU power with the free version. We tried doing it in modal but we ran out of credits. Even if we would att credits it would be around 25 hours och run-time to get the parameters.
